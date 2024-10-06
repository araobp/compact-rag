# Chat test program
# Date: 2024/10/04
# Author: araobp@github.com

import sys
sys.path.append("../../rag")

import chat 
import unittest

def callback(chunk):
    print(chunk, end="")

class TestChat(unittest.TestCase):
    """Test chat package
    """

    def test_chat(self):
        result = chat.chat("Please explain Einstein's theory of relativity in 300 characters.") 
        print(result)
        self.assertTrue("relativity" in result.lower()) 

    def test_chat_streaming(self):
        print("---streaming---")
        self.result = ""
        
        def _callback(text):
            self.result += text
            print(text, end="")

        # Note: this is a synchronous method
        chat.chat("Please explain Einstein's theory of relativity in 800 characters.", _callback)
        print()
        self.assertTrue("relativity" in self.result.lower())

if __name__ == "__main__":
    unittest.main()
