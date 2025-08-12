

https://github.com/user-attachments/assets/ce57cf89-45f9-4436-9385-1fd61690dad0

# 🎥 YouTube Agent with Memory (LangGraph + Streamlit)

This project is a **YouTube AI Assistant** built with:
- **LangGraph** for stateful conversation
- **Google Gemini API** for LLM responses
- **SQLite Memory Checkpointing** for persistent chat history
- **Streamlit** for a simple interactive UI

The agent can:
- Fetch **YouTube video transcripts** (via tool integration)
- Answer questions about the video
- Summarize content
- Maintain **conversation memory** using a fixed `thread_id`

---

## 🚀 Features
- ✅ **LangGraph State Machine** for tool orchestration
- ✅ **Google Generative AI** integration
- ✅ **Custom Tools** (`get_yt_transcript`)
- ✅ **Persistent Conversation Memory** (SQLite-based)
- ✅ **Streamlit Frontend** for interaction

---

## 📂 Project Structure
├── app.py # Streamlit UI
├── youtube_agent.py # YoutubeAgent class (LangGraph implementation)
├── youtube.py # YouTube transcript fetch logic
├── prompt.py # Contains system prompt
├── checkpoints.sqlite # Memory persistence DB
├── requirements.txt # Python dependencies
└── README.md # This file



## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/youtube-agent.git
cd youtube-agent
```



2. **Install dependencies** 
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
3. **Create .env file and paste your api key**

GOOGLE_API_KEY=your_google_api_key_here

**Run the application**
streamlit run app.py
