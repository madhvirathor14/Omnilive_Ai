from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.gemini_engine import generate_response
from app.routes import router   # 👈 routes import करना जरूरी है

app = FastAPI(title="OmniLive AI")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 router connect
app.include_router(router)

@app.get("/")
def root():
    return {"status": "OmniLive AI Running 🚀"}

@app.get("/test")
def test():
    return {
        "response": generate_response(
            "Say hello like a confident real-time AI performance coach."
        )
    }