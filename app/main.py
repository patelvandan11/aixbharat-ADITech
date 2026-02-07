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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(application, host="0.0.0.0", port=8000)