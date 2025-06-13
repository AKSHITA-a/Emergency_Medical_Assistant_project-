# modules/nlp_matcher.py

from sentence_transformers import SentenceTransformer, util

class SymptomNLPMatcher:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Small & fast model
        self.symptom_db = {
            "You may have a viral infection or the flu.": ["fever", "chills", "high temperature"],
            "You might be experiencing a migraine or dehydration.": ["headache", "pain in head"],
            "You may have a cold or respiratory infection.": ["cough", "sneezing", "congestion"],
            "This could be due to low blood pressure or dehydration.": ["dizziness", "lightheaded"],
            "You might be overworked, or it could be early signs of anemia.": ["fatigue", "weakness", "tired"]
        }

        self.known_phrases = list(self.symptom_db.keys())
        self.known_embeddings = self.model.encode(self.known_phrases, convert_to_tensor=True)

    def get_nlp_suggestion(self, user_input):
        user_embedding = self.model.encode(user_input, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(user_embedding, self.known_embeddings)[0]
        top_match_index = cos_scores.argmax().item()

        return self.known_phrases[top_match_index]
