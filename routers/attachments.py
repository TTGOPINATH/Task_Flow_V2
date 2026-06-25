from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from services.attachment_service import (
    save_attachment,
    get_task_files
)

import os


router = APIRouter(
    prefix="/attachments",
    tags=["Attachments"]
)


UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post(
    "/{task_id}"
)
async def upload_file(

    task_id:int,

    file:UploadFile=File(...)
):

    filepath = os.path.join(

        UPLOAD_DIR,

        file.filename
    )

    with open(
        filepath,
        "wb"
    ) as f:

        content = await file.read()

        f.write(content)

    return save_attachment(

        task_id,

        file.filename,

        filepath
    )


@router.get(
    "/{task_id}"
)
def task_files(
    task_id:int
):

    return get_task_files(
        task_id
    )