# AgentForge

Production SaaS platform with 20 AI agents powered by OpenAI and Anthropic.

## Agents

| # | Agent | Category | Provider |
|---|-------|----------|----------|
| 1 | Customer Support | starter | OpenAI |
| 2 | Investment Analyst | starter | OpenAI |
| 3 | Travel Planner | starter | OpenAI |
| 4 | Data Analyst | starter | OpenAI |
| 5 | Personal Finance | starter | OpenAI |
| 6 | AI Journalist | starter | OpenAI |
| 7 | Medical Scan Educator | starter | OpenAI |
| 8 | Meeting Assistant | starter | OpenAI |
| 9 | Reasoning Engine | starter | Anthropic |
| 10 | Health & Fitness | starter | OpenAI |
| 11 | Legal Assistant | multi-agent | Anthropic |
| 12 | Recruitment Assistant | multi-agent | OpenAI |
| 13 | Real Estate Advisor | multi-agent | OpenAI |
| 14 | Startup Analyst | starter | OpenAI |
| 15 | Chat with PDF | rag | OpenAI |
| 16 | Chat with YouTube | rag | OpenAI |
| 17 | Chat with GitHub | rag | OpenAI |
| 18 | Blog Search | rag | OpenAI |
| 19 | Code Reviewer | multi-agent | Anthropic |
| 20 | Movie Production | starter | OpenAI |

## Quick Start

```bash
# Backend
cd backend
cp .env.example .env  # Add your API keys
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

## Deploy

- Frontend: Vercel (root directory: `frontend`)
- Backend: Railway (root directory: `backend`)

Set `VITE_API_URL` in Vercel to your Railway backend URL.

## API

- `GET /api/v1/agents` - List all agents
- `GET /api/v1/agents/:id` - Get agent info
- `POST /api/v1/chat` - Send message `{ agent_id, message, session_id? }`
- `POST /api/v1/chat/file` - Send message with file upload
