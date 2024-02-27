

# import requests
# url = 'http://0.0.0.0:4890'

from fastapi import FastAPI, Query
app = FastAPI()

@app.get("/")
async def reverse_name(name:str= Query(...)):
        rev_name = name[::-1]
        data ={
        "name":name,
        "reverse_name":rev_name 
        }
        return data