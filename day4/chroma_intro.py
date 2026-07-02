import chromadb
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()

collection = client.create_collection(
    name="my_documents"
)
documents = [
    "Python is a programming language.",
    "Dogs are loyal animals.",
    "Cats enjoy sleeping in the sun.",
    "BMW manufactures luxury cars.",
    "Artificial Intelligence uses machine learning."
]

ids = ["1", "2", "3", "4", "5"]

embeddings = model.encode(documents).tolist()

collection.add(
    documents=documents,
    ids=ids,
    embeddings=embeddings
)



query = "Which document talks about cars?"

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print("\nQuery:")
print(query)

print("\nMost relevant documents:")

for doc in results["documents"][0]:
    print("-", doc)