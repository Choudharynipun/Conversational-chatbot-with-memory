# Conversational Chatbot with Memory

## Overview
This project is a sophisticated conversational chatbot application built using **Flask**, **LangChain**, and **FAISS** vector store for memory. It is designed to simulate a human-like conversation by retaining memory of the previous exchanges and retrieving relevant knowledge from a vector database. The chatbot leverages OpenAI's GPT-3.5 for generating coherent and contextually accurate responses.

## Features
- **Conversational Memory:** Uses FAISS vector search to retrieve contextually relevant conversation snippets.
- **LangChain Integration:** Utilizes LangChain's chains and retrievers to structure multi-turn dialogue flow.
- **FastAPI backend:** (if applicable) For fast asynchronous handling of API requests.
- **Interactive UI:** Clean and user-friendly chat interface with real-time message display.
- **Context-Aware Responses:** The chatbot understands the conversation context to give accurate answers.
- **Expandable Knowledge Base:** FAISS vector store supports addition of new knowledge documents for continuous improvement.

## Technologies Used
- Python 3.10+
- Flask (for API and web server)
- LangChain (for LLM chain management)
- FAISS (for fast vector similarity search)
- OpenAI GPT-4 API (for advanced natural language understanding)
- HTML5, CSS3

