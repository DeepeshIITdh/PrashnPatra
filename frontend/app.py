import streamlit as st
import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv('API_URL')

st.set_page_config(page_title="Quiz Generator", page_icon="🧠")
st.title("🧠 Quiz Generator")

# --- Step 1: Quiz input form ---
with st.form("quiz_input_form"):
    topic = st.text_input("Enter a topic", placeholder="e.g. Photosynthesis")
    q_type = st.selectbox("Select question type", [
        "Multiple Choice Question",
        "Fill in the Blanks",
        "True/False",
        "One Word Question"
    ]).lower()
    submit = st.form_submit_button("Generate Question...")

if submit:
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating Question..."):
            try:
                response = requests.post(API_URL, json={
                    "topic": topic,
                    "question_type": q_type
                }, timeout=60)

                data = response.json()

                if "error" in data:
                    st.error("⚠️ Failed to parse model output.")
                    st.text(data.get("raw", "No output returned."))
                else:
                    question_text = data["question"].strip()
                    answer_text = data["answer"].strip()

                    # Handle MCQ option splitting (e.g., A) ..., B) ..., etc.)
                    options = []
                    main_question = question_text

                    if q_type == "multiple choice question":
                        parts = re.split(r"\s*[A-Da-d]\)\s*", question_text)
                        if len(parts) > 1:
                            main_question = parts[0].strip()
                            options = [opt.strip() for opt in parts[1:] if opt.strip()]
                    elif q_type == "true/false":
                        main_question = question_text
                        options = ["True", "False"]

                    st.session_state["question"] = main_question
                    st.session_state["answer"] = answer_text
                    st.session_state["options"] = options
                    st.session_state["quiz_ready"] = True

            except requests.exceptions.RequestException as e:
                st.error(f"❌ Error contacting backend: {e}")

# --- Step 2: Quiz answering form ---
if st.session_state.get("quiz_ready", False):
    st.markdown("### ❓ Quiz Question")
    st.write(st.session_state["question"])

    with st.form("answer_form"):
        if st.session_state["options"]:
            user_answer = st.radio("Choose your answer:", st.session_state["options"])
        else:
            user_answer = st.text_input("Your Answer:")
        check = st.form_submit_button("Submit Answer")

    if check:
        actual = st.session_state["answer"].strip().lower()
        user = user_answer.strip().lower()

        if user == actual:
            st.success("✅ Correct Answer!")
        elif user in actual or actual in user:
            st.info(f"Almost correct! ✅\n\nCorrect answer: **{st.session_state['answer']}**")
        else:
            st.error("❌ Incorrect.")
            st.markdown(f"**Correct answer:** {st.session_state['answer']}")