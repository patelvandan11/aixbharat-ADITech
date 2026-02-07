import os
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path
BASE_DIR = Path(__file__).parent
AUDIO_FILE = BASE_DIR / "speech.mp3"
from app.services.speech import text_to_speech
from app.services.translate import translate_speech
from fastapi import FastAPI
from app.ai.rag import answer_query

application = FastAPI()

@application.get("/")
def read_root():
    return {"message": "Welcome to the Aadhar Card Information API!"}

@application.get("/query")
def query_info(q: str):
    answer = answer_query(q)
    return {"query": q, "answer": answer}


@application.get("/speechtoanswer")
def speech_to_answer():
    """
    speech -> text -> answer
    """

    # 1️⃣ Speech → Text
    question_text = translate_speech(str(AUDIO_FILE))

    # 2️⃣ RAG Answer
    answer = answer_query(question_text)

    return {
        "recognized_text": question_text,
        "answer": answer
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(application, host="0.0.0.0", port=8000)