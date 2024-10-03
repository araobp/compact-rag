from openai import OpenAI

EMBEDDING_MODEL = "text-embedding-3-small"

_DIMENSIONS = {
        "text-embedding-3-small": 1536,
        "text-embedding-3-large": 3072
        }

DIMENSION = _DIMENSIONS[EMBEDDING_MODEL]

client = OpenAI()

def get_embedding(text, model=EMBEDDING_MODEL):
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def ui():

    while True:
        print("Text: ", end="")
        text = input()
        print("")
        vector = get_embedding(text)
        print(f"Embeddings: \n{vector}", end="\n\n")


if __name__ == '__main__':
    ui()