# uagents8-demo-agent

A minimal, dependency-light agent you can fork or clone to try the
[uagents8](https://uagents8.com) git-to-live deploy workflow in a couple of
minutes — push code, get a running agent with a public HTTPS URL.

## What this is

A tiny [FastAPI](https://fastapi.tiangolo.com/) app (`main.py`) with two
routes:

- `GET /` — returns a JSON greeting and the current UTC time.
- `GET /health` — a basic health check.

No `Dockerfile`, no framework-specific manifest. uagents8 detects this as a
Python project (no `go.mod` / `pom.xml` / `build.gradle` / `Cargo.toml` /
`package.json` at the top level) and builds it from `requirements.txt`
automatically.

## Deploy it on uagents8

1. Fork this repo (or just point uagents8 at it directly — it's public).
2. On [uagents8](https://uagents8.com), create a new agent and connect this
   GitHub repository.
3. Deploy. uagents8 builds the image, runs a security scan, and starts the
   app — you'll get a live `https://agent-<name>-<id>.uagents8.io` URL in
   about 90 seconds.
4. Push any change to `main` and watch it redeploy automatically.

## Try breaking the deploy (to see AI Fix)

Want to see uagents8's AI Fix in action? Introduce a small, realistic build
or startup error — for example, add an import for a package that isn't in
`requirements.txt`, or typo an environment variable name your code depends
on — and push it. The deploy will fail with a plain-language reason; open
the agent and use **Fix with AI** to see it diagnose and redeploy a patched
copy automatically, without touching your repository.

## Local run (optional)

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Why this exists

This repo is maintained by the uagents8 team as a quick, safe way for anyone
— press, partners, curious developers — to test the platform's deploy flow
without needing an existing project. See [uagents8.com](https://uagents8.com)
for the full platform: framework support (LangGraph, OpenAI Agents SDK and
any HTTP-serving process), zero-downtime deploys, custom domains, team
collaboration, and AI Fix for failed builds and deploys.
