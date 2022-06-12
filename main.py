import imp
from importlib.metadata import metadata
import re
from fastapi import FastAPI
import os
import cal_crud

app = FastAPI()


@app.get("/creator")
async def creater():
    cal_crud.inserter(2022,6,11,23,30,"hello testing","location ","short description",24*60,2)


#inserter takes arguments as (year,month,day,hour(24 hour format), minute,name,location,description, how many minuts before email, how many minutes before pop up)

@app.delete("/delete")
async def deleter():
    cal_crud.deleter()

@app.patch('/patch')
async def updater():
    cal_crud.updater()