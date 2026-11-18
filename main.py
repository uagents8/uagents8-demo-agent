import os
from datetime import datetime, timezone

import uvicorn
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ["PORT"]))
