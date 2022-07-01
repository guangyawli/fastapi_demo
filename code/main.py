from fastapi import FastAPI, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from db import session
from model import FileInfoTable
from pathlib import Path


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    tmp_size = len(contents)
    final_size = ''
    save_path = "/upload_files/"
    target_path = save_path+file.filename
    with open(target_path, 'wb') as f:
        f.write(contents)

    if tmp_size/(1024**3) > 1:
        final_size = str(('%.2f'%(tmp_size/(1024**3)))) + "GB"
    elif tmp_size/(1024**2) > 1:
        final_size = str(('%.2f'%(tmp_size/(1024**2)))) + "MB"
    elif tmp_size/1024 > 1:
        final_size = str(('%.2f'%(tmp_size/1024))) + "KB"

    newfile = FileInfoTable()
    newfile.file_name = str(file.filename)
    newfile.file_size = str(final_size)
    newfile.file_type = str(file.content_type)
    newfile.file_path = str(save_path)
    session.add(newfile)
    session.commit()

    return {"file_name": file.filename,
            "file_size": final_size,
            "file_type": file.content_type,
            "file_path": save_path
            }


@app.get("/listFiles")
def read_users():
    all_file = session.query(FileInfoTable).all()
    json_body = jsonable_encoder(all_file)
    target = []
    for tmp_item in json_body:
        del tmp_item['id']
        del tmp_item['file_path']
        target.append(tmp_item)

    return JSONResponse(target)


