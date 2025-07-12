# 💬 Bajaj Finserv Banking Assistant (Offline GenAI Chatbot)

A fully offline, banking-style GenAI chatbot built using **Streamlit**, **Llama.cpp**, and **LangChain**. It answers questions about Bajaj Finserv based on:
- Quarterly earnings transcripts (PDF)
- Historical stock price data (CSV)

## ✨ Features

- 🧠 **Local LLM**: Powered by `phi-2` model via `llama-cpp-python` (no OpenAI needed)
- 📊 **Stock Intelligence**: Ask about average/high/low prices or compare time periods
- 📄 **Transcript QA**: Retrieves context from Q1–Q4 FY25 investor calls
- 🖼️ **Beautiful Banking UI**: True blue theme, chat bubbles, bottom input bar
- 🔒 **Fully Offline**: Works without internet or cloud APIs
- 🧩 Built with LangChain + FAISS + HuggingFace

---

## 📁 Project Structure
bajaj_chatbot/
│
├── app.py # Streamlit UI (chat)
├── build_db.py # FAISS vector builder for PDFs
├── config.py # Paths and settings
├── requirements.txt # Python dependencies
│
├── styles/
│ └── banking.css # Custom CSS for banking UI
│
├── models/
│ └── phi-2.Q4_K_M.gguf # Local LLM model (downloaded separately)
│
├── data/
│ ├── BFS_Share_Price.csv # Stock data
│ └── transcripts/ # Q1–Q4 FY25 PDF earnings call transcripts
│
├── modules/
│ ├── price_qa.py # Handles stock-related queries
│ ├── transcript_qa.py # Loads vector DB and LLM
│ └── response_router.py # Routes queries to the correct engine
│
└── vectorstore/ # FAISS vector index (auto-generated)

yaml
Copy
Edit

---

## 🚀 How to Run Locally

### 1. 🔧 Install Dependencies
```bash
pip install -r requirements.txt
2. 🧠 Download the LLM Model

Download the phi-2.Q4_K_M.gguf model from Hugging Face
Place it in the models/ folder.

3. 🏗️ Build the Vectorstore
bash
Copy
Edit
python build_db.py
4. 🧪 Launch the Chatbot
bash
Copy
Edit
streamlit run app.py