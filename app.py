import streamlit as st
import pandas as pd
from utils.resume_parser import extract_multiple_resumes
from utils.matcher import get_similarity_score, get_final_score
from utils.ats_utils import get_ats_score, rank_resumes

st.set_page_config(page_title="Talent Ranker", layout="wide")
st.title(" Resume Matcher & ATS Screener")

job_description = st.text_area("Paste the Job Description (JD) here", height=200)
uploaded_files = st.file_uploader("Upload multiple resumes (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files and job_description:
    with st.spinner("Processing resumes..."):
        resumes = extract_multiple_resumes(uploaded_files)
        results = []

        for file_name, resume_text in resumes.items():
            similarity = get_similarity_score(job_description, resume_text)
            ats_score, _, _ = get_ats_score(job_description, resume_text)
            final_score = get_final_score(similarity, ats_score)

            results.append({
                "Resume": file_name,
                "Final Score": final_score,
                "Similarity %": round(similarity * 100, 2),
                "ATS %": round(ats_score * 100, 2)
            })

        # ✅ Rank resumes
        ranked_results = rank_resumes(results)
        df = pd.DataFrame(ranked_results).sort_values("Rank")

        st.subheader("📊 Ranked Resumes")
        st.dataframe(df, use_container_width=True)

else:
    st.info("Please upload resumes and paste a job description.")
