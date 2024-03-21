from fastapi import FastAPI
from profiling.threads import execute_task as task_with_threads
from profiling.processes import execute_task as task_with_processes
from profiling.asyncios import execute_task as task_with_asyncio

app = FastAPI()


@app.get("/threads")
def execute_threads():
    task_with_threads()    
    return {"message": "jobs executed"}


@app.get("/processes")
def execute_processes():
    task_with_processes()    
    return {"message": "jobs executed"}

@app.get("/asyncio")
async def execute_asyncio():
    await task_with_asyncio()    
    return {"message": "jobs executed"}
