# 📄 Resume Matcher & ATS Screener

This is a smart HR tool built with **Streamlit** that allows HR teams or recruiters to upload multiple resumes and a custom Job Description (JD), and it will:
- Compute **ATS compatibility score**
- Measure **semantic similarity** between resume and JD
- Generate a **final matching score**
- Rank all resumes accordingly
- Suggest keyword gaps (if enabled)

---

## 🚀 Features

- 📝 **Upload multiple resumes (PDF/DOCX)**
- 📋 **Paste any Job Description (JD)**
- 🤖 **ATS Score** based on keyword matching
- 🧠 **Similarity Score** using fuzzy NLP comparison
- 🏆 **Final Score & Resume Ranking**
- 📊 **Clean tabular view with sorting**

---

## 🧪 Technologies Used

| Tool/Library     | Purpose                            |
|------------------|-------------------------------------|
| Streamlit        | Interactive Web UI                  |
| spaCy            | Natural Language Processing         |
| FuzzyWuzzy       | Fuzzy keyword similarity            |
| PyPDF2, python-docx | Resume parsing                   |
| scikit-learn     | Utility functions for scoring       |
| pandas           | Table creation and manipulation     |

---
