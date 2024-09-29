import pathlib

from config.settings import settings
from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get("/")
def root() -> str:
    """Return the root message of the application."""
    return "root of application"

@app.post("/upload_document/")
async def create_upload_file(file: UploadFile) -> dict[str,str]:
    """Handle the upload of a document and save it to the specified folder."""
    folder = settings.upload_folder_path

    p = pathlib.Path(folder)
    p.mkdir(parents=True, exist_ok=True) # Create the folder if it doesn't exist

    file_loc = folder+ "/" + file.filename
    with pathlib.Path.open(file_loc, "wb+") as file_object:
        file_object.write(await file.read())  # Write the file to the directory

    return {"info": "File saved", "filename": file.filename, "path": file_loc}
