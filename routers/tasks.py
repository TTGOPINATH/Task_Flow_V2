from fastapi import APIRouter, Request

from models.task import TaskCreate
from services.task_service import edit_task
from services.role_service import admin_only

from services.task_service import (
get_tasks,
get_completed_tasks,
create_task,
delete_task,
update_task_status,
get_tasks_by_project,
get_tasks_by_employee,
get_recent_tasks
)

router = APIRouter(
prefix="/tasks",
tags=["Tasks"]
)

@router.get("/")
def tasks():
    return get_tasks()


@router.get("/completed")
def completed_tasks():
    return get_completed_tasks()


@router.post("/")
def add_task(
    data: TaskCreate,
    request: Request
):
    admin_only(
        request.session.get("user")
    )

    return create_task(data)


@router.delete("/{task_id}")
def remove_task(
    task_id: int,
    request: Request
):
    admin_only(
        request.session.get("user")
    )

    return delete_task(
        task_id
    )


@router.put("/{task_id}")
def update_status(
    task_id: int,
    status: str,
    request: Request
):
    if not request.session.get(
        "user"
    ):

        return {
            "message":
            "Unauthorized"
        }

    return update_task_status(
        task_id,
        status
    )


@router.get("/mytasks")
def my_tasks(request: Request):

    user = request.session.get("user")

    if not user:
        return []

    return get_tasks_by_employee(user["email"])


@router.get("/project/{project_id}")
def project_tasks(
    project_id: int
):
    return get_tasks_by_project(
        project_id
    )


@router.get("/recent")
def recent_tasks():
    return get_recent_tasks()


@router.get("/employee/{email}")
def employee_tasks(
    email: str
):
    return get_tasks_by_employee(
        email
    )


@router.put("/edit/{task_id}")
def update_task(task_id: int, data: TaskCreate, request: Request):

    admin_only(request.session.get("user"))

    return edit_task(task_id, data)
