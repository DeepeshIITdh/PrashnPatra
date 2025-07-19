from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
import os
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv('MODEL_PATH')

def load_tinyllama_pipeline():
    pipe = pipeline(
        "text-generation",
        model=MODEL_PATH,
        tokenizer=MODEL_PATH,
        max_length=200,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.1,
        do_sample=True
    )
    return HuggingFacePipeline(pipeline=pipe)