from llama_index.readers import SimpleDirectoryReader
from llama_index import VectorStoreIndex

from dotenv import load_dotenv
import logging
import sys

load_dotenv()

def main(url:str)->None:
    documents = SimpleDirectoryReader(url).load_data()
    index=VectorStoreIndex.from_documents(documents)
    query_engine=index.as_query_engine()
    response=query_engine.query("who is the author of this book")
    print(response)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python directoryReader.py <directory_path>")
        sys.exit(1)
    directory_path = sys.argv[1]
    main(directory_path)