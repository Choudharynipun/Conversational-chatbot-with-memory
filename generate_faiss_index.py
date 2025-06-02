# generate_faiss_index.py

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

# ✅ Make sure OpenAI API key is set
if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("❌ Please set the OPENAI_API_KEY environment variable.")

# ✅ Load your knowledge base file
loader = TextLoader("docs/knowledge_base.txt", encoding='utf-8')
documents = loader.load()

# ✅ Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = splitter.split_documents(documents)

# ✅ Embed and create FAISS index
embedding_model = OpenAIEmbeddings()
vector_store = FAISS.from_documents(texts, embedding_model)

# ✅ Save FAISS index
os.makedirs("faiss_store", exist_ok=True)
vector_store.save_local("faiss_store", index_name="chatbot_index")

print("✅ FAISS index created successfully and saved to 'faiss_store/chatbot_index.faiss'")
