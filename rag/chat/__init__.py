from openai import OpenAI

client = OpenAI()

IMG_TYPE = "jpeg"

def chat(text, b64image=None, callback=None):

    def _content(text, b64image=None):
        return [
                {"type": "text", "text": text},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:{IMG_TYPE};base64,{b64image}"},
                },
               ] if b64image is not None else text 

    if callback:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": _content(text, b64image)}],
            stream=True,
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                callback(content)

        callback('\n')

    else:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": _content(text, b64image)}]
        )

        return resp.choices[0].message.content

