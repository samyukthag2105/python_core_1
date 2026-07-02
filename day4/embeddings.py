from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity




model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love dogs.",
    "Puppies are adorable.",
    "I enjoy programming in Python.",
    "The weather is sunny today.",
    "Cats are wonderful pets."
]

embeddings = model.encode(sentences)

similarity = cosine_similarity(embeddings)

print(similarity)


best_score = -1
best_pair = ()

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):

        if similarity[i][j] > best_score:
            best_score = similarity[i][j]
            best_pair = (i, j)

print("\nMost similar sentences:\n")

print(sentences[best_pair[0]])
print(sentences[best_pair[1]])

print(f"\nSimilarity: {best_score:.3f}")
