# VectorDB test program
# Date: 2024/10/04
# Author: araobp@github.com

import sys
sys.path.append("../rag")

import chat 

def callback(chunk):
    print(chunk, end="")

chat_completion = chat.chat("Please explain Einstein's theory of relativity in 300 characters.") 
print(chat_completion)

print('--- Streaming ---')
chat.chat("Please explain Einstein's theory of relativity in 800 characters.", callback)
