# chat
#
# Author: araobp@github.com
# Date: 2024/10/08

from openai import OpenAI

DEFAULT_ASSISTANT_MESSAGE = "You are an AI assistant."
DEFAULT_SYSTEM_MESSAGE = "You are good at analyzing images."

client = OpenAI()

def invoke(user_message, assistant_message=DEFAULT_ASSISTANT_MESSAGE, system_message=DEFAULT_SYSTEM_MESSAGE, b64image=None, json_output=False, callback=None):

    content_user = [
                {
                    "type": "text",
                    "text": user_message 
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{b64image}"},
                },
               ] if b64image is not None else user_message 

    messages = [
            {"role": "assistant", "content": assistant_message},
            {"role": "user", "content": content_user}
            ]
    
    if system_message:
        messages.append({"role": "system", "content": system_message})

    response_format = {"type": "json_object"} if json_output else None 

    if callback:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
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
            messages=messages,
            response_format=response_format
        )

        return resp.choices[0].message.content

