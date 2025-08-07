
from llama_index.readers.web import SimpleWebPageReader  # ✅ Corrected import 
from  llama_index.core import VectorStoreIndex,Settings

# adddirtionala things toi omport if you wan to use ollama models for lalamindex.
# pip install llama-index-llms-ollama
# pip install llama-index-embeddings-ollama
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from dotenv import load_dotenv
#  
#  ollama pull nomic-embed-text you need to pull it into your pc

load_dotenv()
def main(url:str)->None:

    llm=Ollama(model="gemma3",request_timeout=120)
    embed_model=  OllamaEmbedding(model_name="nomic-embed-text")
    Settings.llm=llm
    Settings.embed_model=embed_model    

    documents=SimpleWebPageReader(html_to_text=True).load_data([url])
    index=VectorStoreIndex.from_documents(documents)
    query_engine=index.as_query_engine()
    response=query_engine.query("summarize this in 100 words")
    print(response)


if __name__=="__main__" :
    main(url="https://medium.com/aimonks/who-taught-the-bot-to-smile-generative-ai-trust-theatre-and-the-ux-illusion-00d4bb21bbe7")   
