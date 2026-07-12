# 🤖 Python Autonomous AI Agent

An Autonomous AI Agent built using **Python, FastAPI, Google Gemini, Streamlit, and python-docx** that can understand natural language requests, generate its own execution plan, execute tasks autonomously, perform self-reflection, and generate professional Microsoft Word documents.

---

## 🚀 Features

- 🧠 Autonomous Task Planning
- ⚙️ AI Task Execution
- 🔍 Reflection & Self-Review
- 📄 Automatic Microsoft Word (.docx) Generation
- 🌐 FastAPI REST API
- 🎨 Streamlit User Interface
- 🤖 Google Gemini 2.5 Flash Integration
- ✅ Request Validation using Pydantic

---

## 🏗️ Architecture

```
User Request
      │
      ▼
 FastAPI API
      │
      ▼
 Planner (Gemini)
      │
      ▼
 Execution Plan
      │
      ▼
 Executor
      │
      ▼
 Reflection
      │
      ▼
 Word Document Generator
      │
      ▼
 API Response
```

---

## 📂 Project Structure

```
python-ai-autonomous-agent/
│
├── app.py                  # FastAPI Backend
├── ui.py                   # Streamlit UI
├── config.py               # API Keys & Configuration
├── planner.py              # Autonomous Planner
├── executor.py             # Task Executor
├── reflection.py           # Self Review Module
├── document.py             # Word Document Generator
├── prompts.py              # AI Prompts
├── models.py               # Pydantic Models
├── requirements.txt
├── README.md
│
├── output/
│     └── report.docx
│
└── utils/
      └── helpers.py
```

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Streamlit
- Google Gemini 2.5 Flash
- python-docx
- Pydantic
- Requests

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-ai-autonomous-agent.git
```

Move into the project

```bash
cd python-ai-autonomous-agent
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run FastAPI

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000
```

Swagger API

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Streamlit UI

Open another terminal

```bash
streamlit run ui.py
```

Open

```
http://localhost:8501
```

---

## 📮 API Endpoint

### POST `/agent`

### Request

```json
{
  "request": "Create a business proposal for an AI-powered hospital chatbot."
}
```

---

### Response

```json
{
  "request": "...",
  "plan": [
    "Analyze Requirements",
    "Generate Proposal",
    "Review Content"
  ],
  "status": "completed",
  "document": "output/report.docx",
  "output": "Generated document..."
}
```

---

## 📄 Example Requests

### Business Proposal

```
Create a professional business proposal for an AI-powered hospital chatbot including executive summary, implementation strategy, budget estimation and conclusion.
```

### Meeting Minutes

```
Generate meeting minutes for a product planning meeting discussing the launch of an AI customer support chatbot.
```

### Technical Design

```
Create a technical design document for an AI-powered resume screening platform.
```

---

## 🔄 Agent Workflow

1. Accept User Request
2. Generate Autonomous Task Plan
3. Execute Each Task
4. Combine Results
5. Perform AI Reflection
6. Generate Word Document
7. Return API Response

---

## ⭐ Engineering Improvement

Implemented **Reflection / Self-Check**.

The Reflection module reviews the generated content to improve:

- Grammar
- Formatting
- Logical Flow
- Completeness
- Professional Writing Quality

This improves the overall quality before generating the final Word document.

---

## 📸 Demo

### FastAPI

```
http://127.0.0.1:8000/docs
```

### Streamlit

```
http://localhost:8501
```

---

## 📁 Output

Generated documents are automatically saved in

```
output/
```

Example

```
output/report.docx
```

---

## 📌 Future Improvements

- Conversation Memory
- Multi-Agent Workflow
- Tool Calling
- Vector Database (RAG)
- LangGraph Integration
- Docker Deployment
- Authentication
- PDF Export
- Cloud Deployment

---

## 👨‍💻 Author

**Santosh Tambe**

- GitHub: https://github.com/TAMBESANTOSH077
- LinkedIn: https://www.linkedin.com/in/santosh-tambe-637914293/

---

## 📄 License

This project is licensed under the MIT License.
