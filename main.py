import os
import time
from typing import List
from fastapi import FastAPI, HTTPException, status
from fastapi import Form, File, UploadFile

app = FastAPI()


@app.post("/contact")
async def contact(subject: str = Form(...), msg: str = Form(...)):
    return {
        "subject": subject,
        "message": msg
    }

@app.post("/create_user")
async def create_user(username: str = Form(...), password: str = Form(...), photo: UploadFile = File(...)):

    if photo.content_type != 'image/jpeg':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Invalid format {photo.content_type} only valid images with format jpg'
        )

    await save_image(photo)

    return {
        "username": username,
        "password": password,
        "photo": {
            'filename': photo.filename,
            'content_type': photo.content_type
        }
    }

async def save_image(photo):
    tmp_folder = './tmp'
    if not os.path.exists(tmp_folder):
        os.mkdir(tmp_folder)

    content = await photo.read()

    print(f'{tmp_folder}/{time.time()}.jpg')
    with open(f'{tmp_folder}/{time.time()}.jpg', 'wb') as f:
        f.write(content)


# Python 3.6 o mayor
@app.post("/upload_multiple_files/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}

# A partir de Python 3.9
@app.post("/upload_multiple_files_v2/")
async def create_upload_files_v2(files: list[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}