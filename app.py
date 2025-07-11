import streamlit as st
from pdf_reader import extract_text_from_pdf
from generator import generate_test_artifacts
from utils import save_to_csv

st.set_page_config(page_title="QA Assistant", layout="centered")
st.title("🧵 QA Test Case Assistant")

uploaded_file = st.file_uploader("Upload a requirements document (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.success("Document processed.")

    action = st.radio(
        "What do you want to generate?",
        ["User Stories", "Test Scenarios", "Test Cases"],
    )

    if st.button("Generate"):
        with st.spinner("Generating with OpenAI..."):
            results = generate_test_artifacts(text, action)
            st.text_area("Generated Output", results, height=300)

            csv_path = save_to_csv(results, action)
            st.success("Done!")
            st.download_button(
                "Download as CSV",
                open(csv_path, "rb"),
                file_name=f"{action.replace(' ', '_').lower()}.csv",
            )
