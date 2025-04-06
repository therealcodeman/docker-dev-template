import redis
import debugpy
from fastapi import FastAPI

app = FastAPI()

redis_service = redis.Redis(host='redis', port=6379)

debugpy.listen(('0.0.0.0', 5678))

@app.get("/")
def root():
    return {"message": "hello world"}

@app.get("/hits")
def redis_service_backend():
    redis_service.incr("hits")
    return {"times_accessed": redis_service.get("hits")}