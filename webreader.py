from llama_index.readers.web import SimpleWebPageReader  # ✅ Corrected import
from llama_index.core import VectorStoreIndex

from dotenv import load_dotenv
import logging
import sys
 # thisis by default script for runnign llammainde but llamainde by default need  opene apii key to run op wee will create a different script to run the ollama models with llamaindex.
load_dotenv()

def main(url: str) -> None:
    documents = SimpleWebPageReader(html_to_text=True).load_data([url])  # ✅ Note: expects a list
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("summarize this in 100 words")
    print(response)

if __name__ == "__main__":
    main(url="https://medium.com/aimonks/who-taught-the-bot-to-smile-generative-ai-trust-theatre-and-the-ux-illusion-00d4bb21bbe7")
