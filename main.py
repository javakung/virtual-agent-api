from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def main():
    return 'Deploy Model Tutorial'

@app.get("/test")
async def test():
    return 'Test Tutorial'

@app.get("/add")
async def add(a: int = 0, limit: b = 0):
    return a+b

if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True) 
