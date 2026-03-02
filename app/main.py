from fastapi import FastAPI, HTTPException
from pydantic import BaseModel      #to define the  shape of data
from app.llm_service import generate_response
from app.logger import logger


# creating fast api app

app = FastAPI(title = "Simple Groq Chat")

class ChatRequest(BaseModel):
    message : str       # user message
    temperature :float = 0.7

class ChatResponse(BaseModel):
    response:str # ai reply

@app.post("/chat",response_model = ChatResponse)
def chat(request:ChatRequest):

    try:
        logger.info(f"New message recieved: {request.message}")
        ai_reply = generate_response(request.message,request.temperature)
        return ChatResponse(response = ai_reply)
    
    except Exception as e:
        logger.error(f"Error while processing request:{str(e)}")

        raise HTTPException(status_code = 500, detail="Something went wrong. Please try again later.")
