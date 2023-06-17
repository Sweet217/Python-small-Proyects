import os
import openai
from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex

APIKEY = ""
openai.api_key = APIKEY

os.environ['OPENAI_API_KEY'] = APIKEY

document = SimpleDirectoryReader('./data').load_data()
index = GPTVectorStoreIndex.from_documents(document)

query_engine = index.as_query_engine()
response = query_engine.query("What is rice?")

print(response)