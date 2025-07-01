from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_similarity_score(jd, resume):
    embeddings = model.encode([jd, resume])
    sim_score = util.cos_sim(embeddings[0], embeddings[1])[0].item()
    return sim_score


def get_final_score(similarity, ats):
    return round(0.7 * similarity + 0.3 * ats, 2)
