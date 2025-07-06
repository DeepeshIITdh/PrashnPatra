# PrashnPatra

**PrashnPatra** is an AI-powered quiz generation engine built to revolutionize how questions are created, adapted, and delivered in educational and assessment systems. The project aims to provide a highly customizable and intelligent platform for generating structured question-answer pairs across various subjects, question types, and complexity levels.

The long-term vision is to build a complete system that understands contextual information, adapts to student needs, and integrates with educational platforms through APIs and UI apps.

---

## 🌐 Current Version: v1.0

> Version 1.0 is the seed stage of PrashnPatra — establishing the foundation with a dataset and fine-tuning logic.

### What's Included:
- A **custom quiz dataset** in JSONL format with structured input/output for fine-tuning  
- LoRA and QLoRA-based **fine-tuning notebooks** using TinyLLaMA  
- Minimal working project structure, `.gitignore`, and `requirements.txt`  

### Dataset Format (`custom_quiz_dataset.jsonl`):
Each line is a JSON object like:

```json
{
  "input": "Generate a one-word question on Chemistry",
  "output": {
    "Question": "What is the chemical symbol for Sodium?",
    "Answer": "Na"
  }
}
```

---

## 🔄 Contextual Capabilities - Coming Soon

Next versions will explore:
- Inputting longer context (paragraphs or passages)  
- Extractive and abstractive QA mixed with quiz generation   
- Chunking and embedding of **contexts with retrieval** for relevance  

---

## 📁 Project Structure

```
.  
├── data/  
│ └── custom_quiz_dataset.jsonl
├── notebooks/
│ ├── fine_tuning_tinyllama_LoRA.ipynb
│ └── fine_tuning_tinyllama_QLoRA.ipynb
├── .gitignore
└── requirements.txt 
``` 

---

## 🗓️ Version History

### v1.0 - 
- **First functional prototype of PrashnPatra** 
- Created a custom `.jsonl` dataset with input-output pairs 
- Fine-tuned TinyLLaMA on this custom dataset    
- Implemented **LoRA** and **QLoRA** training notebooks  

---

## 💫 A Note from the Creator

> *"PrashnPatra started as an idea — a simple tool to generate quiz questions — but it aspires to become a powerful, context-aware engine that democratizes intelligent content creation in education."*

---

Made with ❤️ and curiosity.