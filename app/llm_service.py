from groq import Groq


from app.config import Settings
from app.logger import logger # logging tool made in the logger file in the same folder

# this is like logging in to the Groq
client = Groq(api_key=Settings.GROQ_API_KEY)

def generate_response(user_message:str,temperature:float = 0.7):

    try:
        logger.info(f"sending request to model: {Settings.MODEL_NAME}")

        # two messages are sent to the model one is system message and other is user message
        completion = client.chat.completions.create(
            model = Settings.MODEL_NAME,
            messages=[{"role":"system","content":Settings.SYSTEM_PROMPT},{"role":"user","content":user_message}],
            temperature = temperature)
        
        ai_reply = completion.choices[0].message.content
        return ai_reply
    
    except Exception as e:
        logger.exception("something gone wrong while calling groq api")
        raise RuntimeError(f"Ai service failed {str(e)}")
