


from fastapi import FastAPI
app = FastAPI()

@app.get("/reverse/{input}")
async def reverse_name(input:str):
    return {"reverse_string":input[::-1]}