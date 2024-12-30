from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - fastapi-coll-9ed5e7acb9334f1bb4eecb2984b78c4a',debug=False,docs_url='/sharp-wiles-f3610ffec67611ef8cac0242ac12000559/docs',openapi_url='/sharp-wiles-f3610ffec67611ef8cac0242ac12000559/openapi.json')

app.include_router(router, prefix='/sharp-wiles-f3610ffec67611ef8cac0242ac12000559/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()