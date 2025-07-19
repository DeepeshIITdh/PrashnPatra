from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
import os

model_path = os.path.join('models', 'tinyllama_finetuned_on_quizgen')

def load_tinyllama_pipeline():
    pipe = pipeline(
        "text-generation",
        model=model_path,
        tokenizer=model_path,
        max_length=200,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.1,
        do_sample=True
    )
    return HuggingFacePipeline(pipeline=pipe)