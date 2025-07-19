from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from peft import PeftModel
import torch
import os
from langchain_huggingface import HuggingFacePipeline

def load_tinyllama_pipeline():
    base_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    adapter_path = os.path.join('models', 'tinyllama_finetuned_on_quizgen')

    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    base_model = AutoModelForCausalLM.from_pretrained(base_model_name, torch_dtype=torch.float16)
    
    # Apply LoRA adapter
    model = PeftModel.from_pretrained(base_model, adapter_path)
    model.eval()

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=200,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.1,
        do_sample=True
    )

    return HuggingFacePipeline(pipeline=pipe)