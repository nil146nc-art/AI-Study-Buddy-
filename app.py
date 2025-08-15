import streamlit as st
import re

st.title("📚 Simple Offline AI Study Buddy")

# Upload notes
uploaded_file = st.file_uploader("Upload your TXT notes", type=["txt"])
notes_text = ""
if uploaded_file:
    notes_text = uploaded_file.read().decode("utf-8")
    st.success("File uploaded successfully!")

# Type your question
question = st.text_input("Type your question here:")

if st.button("Get Answer"):
    if not question.strip() or not notes_text:
        st.warning("Upload a file and type a question first!")
    else:
        # Split notes into sentences
        sentences = re.split(r'(?<=[.!?]) +', notes_text)
        question_words = question.lower().split()

        # Pick the sentence with most matching words
        best_sentence = ""
        best_score = 0
        for sentence in sentences:
            score = sum(word in sentence.lower() for word in question_words)
            if score > best_score:
                best_score = score
                best_sentence = sentence

        if best_score > 0:
            st.write("Answer:")
            st.write(best_sentence)
        else:
            st.write("Sorry, no matching sentence found. Try different words from your notes.")

