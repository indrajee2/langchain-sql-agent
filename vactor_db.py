from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def vactor_store(row_query):
    documents=[Document(page_content=text) for text in row_query]
    db_vector_store = FAISS.from_documents(documents, embeddings)
    print(db_vector_store)
    db_vector_store.save_local("faiss_index")

    return "vactor store saved."


def vactor_similarity_search(query,k=3):
    vactor_db=FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)
    docs=vactor_db.similarity_search(query,k=k)
    return docs