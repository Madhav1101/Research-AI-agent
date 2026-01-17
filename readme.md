# 🤖 Research AI Agent

A Python-based AI assistant that generates structured research summaries on any topic.  
It leverages **Wikipedia** and **DuckDuckGo** to gather information and produces clean, human-readable summaries saved in text files. 📄

---

## ✨ Features

- 📝 Accepts user queries for research topics  
- 🌐 Fetches relevant content from Wikipedia and the web (DuckDuckGo)  
- 🤖 Uses OpenAI models to generate concise, structured summaries  
- 💾 Saves research output in readable `.txt` format  
- 🧾 Wraps summaries for easy reading

---

## 🛠 Tech Stack

- 🐍 **Python** – Core programming language  
- 🔗 **LangChain** – Orchestrates prompts, LLMs, and tool integrations  
- 🧠 **OpenAI** – Generates natural language research summaries  
- 🌍 **DuckDuckGo Search** – Provides web-based information  
- 📚 **Wikipedia API** – Fetches structured content from Wikipedia

---

## ⚡ Run Locally on System
Step 1:
```bash
git clone https://github.com/Madhav1101/Research-AI-agent.git

cd Research
```
step 2:
```bash
python -m venv venv
```
step 3:
```bash
venv\Scripts\activate  # Windows
```
### or
```bash
source venv/bin/activate  # Linux / macOS
```

Step 4:
### create new .env file
At least one LLM Model API KEY Required
```bash
ANTHROPIC_API_KEY=YOUR_API_Key
OPENAI_API_KEY=YOUR_API_Key
```
Step 5:
```bash
pip install -r requirements.txt
```

step 6:
# Run
```bash 
python .\main.py
```

### Generate one text file with name of `reasearch_output.txt`.

