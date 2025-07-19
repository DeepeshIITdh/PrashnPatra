from fastapi import FastAPI
from pydantic import BaseModel
from utils import load_tinyllama_pipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = FastAPI()

# Load model once
llm = load_tinyllama_pipeline()

# Prompt template
tinyllama_prompt = PromptTemplate.from_template(
    "Generate a {question_type} question on {topic}.\n"
)
parser = StrOutputParser()
chain = tinyllama_prompt | llm | parser

# Request schema
class QuizRequest(BaseModel):
    topic: str
    question_type: str  # e.g., "Fill in the Blanks"

@app.post("/generate")
async def generate_quiz(request: QuizRequest):
    inputs = {
        "topic": request.topic,
        "question_type": request.question_type
    }

    result = chain.invoke(inputs).strip()

    # Try to parse the result into structured format
    try:
        parts = result.split("Question:")[1].split("Answer:")
        question = parts[0].strip()
        answer = parts[1].strip()
        return {"question": question, "answer": answer}
    except Exception:
        return {"error": "Failed to parse model output.", "raw": result}