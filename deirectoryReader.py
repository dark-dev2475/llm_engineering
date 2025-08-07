from llama_index.readers.web import SimpleDirectoryReader  # ✅ Corrected import
from  llama_index.core import VectorStoreIndex,Settings

# adddirtionala things toi omport if you wan to use ollama models for lalamindex.
# pip install llama-index-llms-ollama
# pip install llama-index-embeddings-ollama
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from dotenv import load_dotenv


load_dotenv()

def main(url:str)->None:
    llm=Ollama(model="gemma3",request_timeout=120)
    embed_model=  OllamaEmbedding(model_name="nomic-embed-text")
    Settings.llm=llm
    Settings.embed_model=embed_model
    documnets= SimpleDirectoryReader(url).load_data()
    index=VectorStoreIndex.from_documents(documnets)
    query_engine=index.as_query_engine()
    response=query_engine.query("who is the author of this book")
    print(response)


if __name__=="__main__" :
    main(url="C:\\Users\\gagan\\OneDrive\\Documents\\ration card .pdf")
