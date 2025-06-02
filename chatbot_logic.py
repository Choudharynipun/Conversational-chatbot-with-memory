# chatbot_logic.py

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os

# Load FAISS vector store
print("Loading FAISS index from 'faiss_store/chatbot_index.faiss'...")
vectorstore = FAISS.load_local("faiss_store", OpenAIEmbeddings(), index_name="chatbot_index")
print("FAISS index loaded successfully!")

# Initialize memory
print("Initializing conversation memory...")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
print("Conversation memory initialized.")

# Initialize OpenAI LLM
print("Loading OpenAI language model...")
llm = ChatOpenAI(temperature=0.5)
print("OpenAI LLM loaded.")

# Build Conversational QA chain
print("Building Conversational Retrieval Chain using LangChain...")
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    memory=memory
)
print("Conversational Retrieval Chain created successfully!")


def get_chat_response(user_query):
    try:
        print("Received user query:", user_query)
        # You can just call qa_chain.run() now
        response = qa_chain.run(user_query)
        print("Generated response:", response)
        return response
    except Exception as e:
        print("Error during response generation:", str(e))
        return "Sorry, something went wrong while generating the response."
