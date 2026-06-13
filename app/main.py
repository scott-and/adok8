from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# User input 
class TextInput(BaseModel):
    text: str

app = FastAPI()

# Model is loaded prior to all requests; prevents reloading on a per-request basis
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# ------------------------------------------
# Endpoints
# ------------------------------------------

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(input: TextInput):
    return classifier(input.text)[0]