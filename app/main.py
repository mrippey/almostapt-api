from fastapi import FastAPI
import groups


app = FastAPI()

app.include_router(groups.routers)


@app.get('/', tags=['Root'])
async def root_url():
    return {"message": "Welcome!"}
