from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return { "status": "OK" }

@app.get("/health")
def check_health():
    return { "status": "OK" }
