import openai
import numpy as np

openai.api_key = ""

# Function to get embeddings from OpenAI
def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.Embedding.create(
        input=[text],
        model=model
    )
    return response['data'][0]['embedding']

# Function to calculate cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Sample assignments
assignment = ""

assignment_all = ""

embedding1 = get_embedding(assignment1)
embedding2 = get_embedding(assignment2)

similarity = cosine_similarity(embedding1, embedding2)

print(f"Similarity Score: {similarity:.2f}")
