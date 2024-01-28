from fastapi import  FastAPI 
app = FastAPI()

@app.get("mysql+pymysql://root@localhot:3306/test")