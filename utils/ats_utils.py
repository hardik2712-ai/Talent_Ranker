# ✅ utils/ats_utils.py (SIMPLIFIED: Showing only ATS, Similarity, Final Score + RANK)
import re
import spacy
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from fuzzywuzzy import fuzz

nlp = spacy.load("en_core_web_sm")

important_sections = [
    "experience",
    "projects",
    "skills",
    "certifications",
    "education",
    "technical competencies",
    "professional summary",
    "training"
]

def extract_relevant_text(resume_text):
    lines = resume_text.splitlines()
    selected_text = []
    section = ""
    for line in lines:
        line_lower = line.strip().lower()
        if any(sec in line_lower for sec in important_sections):
            section = line_lower
        if section:
            selected_text.append(line)
    return " ".join(selected_text)

def extract_keywords(text):
    doc = nlp(text.lower())
    keywords = [chunk.text.strip() for chunk in doc.noun_chunks if chunk.text.strip() not in ENGLISH_STOP_WORDS]
    blacklist = {"job", "summary", "skills", "role", "team", "experience", "applications", "document", "portfolio", "design", "a passionate", "present results"}
    return list(set([kw for kw in keywords if len(kw) > 2 and kw.lower() not in blacklist]))

def fuzzy_keyword_match(jd_keywords, resume_text, threshold=85):
    resume_words = resume_text.split()
    matched, unmatched = [], []
    for kw in jd_keywords:
        if any(fuzz.token_set_ratio(kw.lower(), word.lower()) >= threshold for word in resume_words):
            matched.append(kw)
        else:
            unmatched.append(kw)
    return matched, unmatched

def get_ats_score(jd_text, resume_text):
    jd_clean = re.sub(r"[^\w\s]", " ", jd_text.lower())
    stop_phrases = [
        "excellent communication skills", "job summary", "key responsibilities",
        "ownership", "team player", "familiarity", "preferred qualifications",
        "3 6 months", "industry", "edtech", "healthcare"
    ]
    for phrase in stop_phrases:
        jd_clean = jd_clean.replace(phrase.lower(), "")

    jd_keywords = extract_keywords(jd_clean)

    filtered_resume = extract_relevant_text(resume_text)
    resume_clean = re.sub(r"[^\w\s]", " ", filtered_resume.lower())

    matched_keywords, missing_keywords = fuzzy_keyword_match(jd_keywords, resume_clean)

    ats_score = len(set([kw.lower() for kw in matched_keywords])) / len(set([kw.lower() for kw in jd_keywords])) if jd_keywords else 0
    similarity_score = fuzz.token_set_ratio(jd_clean, resume_clean) / 100
    final_score = round((0.5 * similarity_score + 0.5 * ats_score), 2)

    return round(final_score, 2), round(similarity_score * 100, 2), round(ats_score * 100, 2)

def rank_resumes(resume_scores):
    sorted_scores = sorted(resume_scores, key=lambda x: x['Final Score'], reverse=True)
    for idx, entry in enumerate(sorted_scores, 1):
        entry['Rank'] = idx
    return sorted_scores
