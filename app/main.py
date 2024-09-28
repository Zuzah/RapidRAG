from fastapi import FastAPI, File, UploadFile
from config.settings import settings
from typing import Annotated
import os

app = FastAPI()

@app.get("/")
def root():
    return "root of application"

@app.post("/upload_document/")
async def create_upload_file(file: UploadFile):
    folder = settings.upload_folder_path
    
    os.makedirs(folder, exist_ok=True)  # Create the folder if it doesn't exist

    file_location = os.path.join(folder, file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())  # Write the file to the directory

    return {"info": "File saved", "filename": file.filename}
