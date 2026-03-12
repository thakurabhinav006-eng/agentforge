from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import get_settings
from routes.agents import router as agents_router

app = FastAPI(title="AgentForge API", version="1.0.0")

settings = get_settings()
origins = [o.strip() for o in settings.cors_origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agents_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to AgentForge API", "docs": "/docs", "health": "/health"}


@app.get("/health")
def health():
    return {"status": "ok", "agents": 20}
