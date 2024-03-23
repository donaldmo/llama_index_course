import os
from dotenv import load_dotenv
from llama_index import SimpleWebPageReader, VectorStoreIndex


load_dotenv()

def main(url: str) -> None:
    documents = SimpleWebPageReader()
    index = VectorStoreIndex.from_documents(
        documents=documents
    )
    query_engine = index.as_query_engine()
    response = query_engine.query("What is llamaIndex?")
    print(response)


if __name__ == "__main__":
    main('https://cbarkinozer.medium.com/an-overview-of-the-llamaindex-framework-9ee9db787d16')
    
