# app/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io
from app.model import get_prediction

app = FastAPI()



@app.post("/predict")
async def predict(image: UploadFile = File(...), question: str = "How many cats are there?"):
    try:
        image_data = await image.read()
        image = Image.open(io.BytesIO(image_data))
        predicted_answer = get_prediction(image, question)
        return JSONResponse(content={"predicted_answer": predicted_answer})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI ML Docker app!"}