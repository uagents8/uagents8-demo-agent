from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="uagents8 demo agent")


@app.get("/")
def root():
    return {
        "message": "Hello from a live AI agent, deployed on uagents8.",
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/health")
def health():
    return {"status": "ok"}
