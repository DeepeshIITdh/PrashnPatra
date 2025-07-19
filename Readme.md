# PrashnPatra

**PrashnPatra** is an AI-powered quiz generation engine built to revolutionize how questions are created, adapted, and delivered in educational and assessment systems. The project aims to provide a highly customizable and intelligent platform for generating structured question-answer pairs across various *subjects*, *question types*, and *complexity levels*.

The long-term vision is to build a complete system that understands contextual information, adapts to student needs, and integrates with educational platforms through APIs and UI apps.

---

## 🌐 Current Version: v1.1

> Version 1.1 introduces a functional local application — combining model inference with API and UI layers.

### What's Included:
- A **custom quiz dataset** in JSONL format with structured input/output for fine-tuning  
- LoRA and QLoRA based **fine-tuning notebooks** using TinyLLaMA  
- A **FastAPI backend API** to serve quiz generation from the fine-tuned model  
- A **Streamlit-based UI** to interact with the API in real time 

## 🚀 How to Run the Application Locally

#### 1. Clone the Repository

```bash
git clone https://github.com/DeepeshIITdh/PrashnPatra.git
cd PrashnPatra
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Create a `.env` File

```bash
MODEL_PATH = models/tinyllama_finetuned_on_quizgen
API_URL = http://127.0.0.1:8000/generate
```

#### 4. Run the Backend (FastAPI)

```bash
uvicorn api:app --reload
```

#### 5. Run the Frontend (Streamlit) 

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
.
├── data/  
│   └── custom_quiz_dataset.jsonl
├── models/
│   └── tinyllama_finetuned_on_quizgen/
|          # lora adapter model files
├── notebooks/  
│   ├── fine_tuning_tinyllama_LoRA.ipynb  
│   └── fine_tuning_tinyllama_QLoRA.ipynb  
├── .env  
├── .gitignore  
├── api.py         
├── app.py             
├── utils.py           
├── requirements.txt  
└── Readme.md
``` 

---

## 🗓️ Version History

### v1.1 - 
- Added **FastAPI** backend to serve the fine-tuned model
- Built a **Streamlit-based UI** for local quiz generation
- Added demo-ready instructions for local testing and usage

### v1.0 - 
- **First functional prototype of PrashnPatra** 
- Created a custom `.jsonl` dataset with input-output pairs 
- Fine-tuned TinyLLaMA on this custom dataset    
- Implemented **LoRA** and **QLoRA** training notebooks  

---

## Dataset Format (`custom_quiz_dataset.jsonl`):
Dataset **used for fine-tuning**. Each line is a JSON object like:

```json
{
  "input": "Generate a one-word question on Chemistry",
  "output": {
    "Question": "What is the chemical symbol for Sodium?",
    "Answer": "Na"
  }
}
```

## 🔮 Coming in Next Versions

Future updates will focus on **deep contextual understanding** and **multi-question quiz generation**, enabling:

- Feeding longer context like **paragraphs, articles, or textbook sections**
- Generating **multiple structured questions** (like a complete quiz) from a single context
- Supporting both **extractive** (from passage) and **abstractive** (creative) quiz generation
- Integrating **context chunking, vector embeddings, and retrieval** for relevance-driven question generation

This will mark the transition from single QA generation to full-fledged, intelligent quiz creation engines.

---

## 💫 A Note from the Creator

> *"PrashnPatra started as an idea — a simple tool to generate quiz questions — but it aspires to become a powerful, context-aware engine that democratizes intelligent content creation in education."*

---

Made with ❤️ and curiosity.