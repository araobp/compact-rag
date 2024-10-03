from openai import OpenAI

EMBEDDINGS_MODEL = "text-embedding-3-small"

client = OpenAI()

def get_embedding(text, model=EMBEDDINGS_MODEL):
   return client.embeddings.create(input = [text], model=model).data[0].embedding


if __name__ == '__main__':
    print(get_embedding('hello world'))
