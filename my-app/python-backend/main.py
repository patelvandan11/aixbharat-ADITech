from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI(title="AI for Communities API")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserIn(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    email: str
    token: str


class Blog(BaseModel):
    id: int
    title: str
    summary: str
    content: str
    tags: List[str]


FAKE_USER_DB = {
    "demo@community.ai": {
        "password": "password123",  # demo only, do NOT use in prod
        "token": "demo-token-123",
    }
}

BLOGS = [
    Blog(
        id=1,
        title="AI for Local Language Access",
        summary="Using AI to bridge language gaps for public services.",
        content="We explore how speech-to-text and translation models can make government services accessible in local languages...",
        tags=["accessibility", "local-language", "public-services"],
    ),
    Blog(
        id=2,
        title="Voice-First Assistants for Rural Communities",
        summary="Designing low-bandwidth, voice-first interfaces for communities with limited digital literacy.",
        content="Voice-first AI assistants can help people access schemes, health info, and learning resources even on basic phones...",
        tags=["voice-first", "rural", "inclusion"],
    ),
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/auth/login", response_model=UserOut)
def login(user: UserIn):
    existing = FAKE_USER_DB.get(user.email)
    if not existing or existing["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return UserOut(email=user.email, token=existing["token"])


@app.post("/auth/register", response_model=UserOut)
def register(user: UserIn):
    if user.email in FAKE_USER_DB:
        raise HTTPException(status_code=400, detail="User already exists")
    FAKE_USER_DB[user.email] = {"password": user.password, "token": "token-" + user.email}
    return UserOut(email=user.email, token=FAKE_USER_DB[user.email]["token"])


@app.get("/blogs", response_model=List[Blog])
def list_blogs():
    return BLOGS


@app.get("/blogs/{blog_id}", response_model=Blog)
def get_blog(blog_id: int):
    for blog in BLOGS:
        if blog.id == blog_id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

