import streamlit as st
import openai

openai.api_key = "your-api-key-here"  # ← yahan apna OpenAI API key daalo

st.title("🧠 Smart Resume Analyzer (Day 1)")
st.write("Upload your resume (text format) and get AI feedback.")

resume_text = st.text_area("Paste your resume here:")

if st.button("Analyze"):
    if resume_text.strip() != "":
        with st.spinner("Analyzing..."):
            prompt = f"Analyze this resume and suggest improvements:\n\n{resume_text}"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            ai_feedback = response['choices'][0]['message']['content']
            st.success("✅ Analysis Complete!")
            st.write(ai_feedback)
    else:
        st.warning("Please paste your resume text.")

