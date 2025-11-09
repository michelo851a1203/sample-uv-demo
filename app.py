from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return { "status": "OK" }

def main():
    uvicorn.run(app, host="0.0.0.0", port=8080, proxy_headers=True)

main()
