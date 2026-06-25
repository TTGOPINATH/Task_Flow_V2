from fastapi import APIRouter, Request

from models.project import ProjectCreate

from services.role_service import admin_only

from services.project_service import (
    get_dashboard_stats,
    get_projects,
    create_project,
    delete_project,
    get_completed_projects,
    get_project_progress,
    update_project
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.get("/")
def projects():

    return get_projects()


@router.post("/")
def add_project(
    data: ProjectCreate,
    request: Request
):

    admin_only(
        request.session.get("user")
    )

    return create_project(data)


@router.delete("/{project_id}")
def remove_project(
    project_id: int,
    request: Request
):

    admin_only(
        request.session.get("user")
    )

    return delete_project(project_id)


@router.get("/completed")
def completed_projects(
    request: Request
):

    admin_only(
        request.session.get("user")
    )

    return get_completed_projects()


@router.get("/dashboard/stats")
def dashboard_stats(
    request: Request
):

    admin_only(
        request.session.get("user")
    )

    return get_dashboard_stats()


@router.get("/progress/{project_id}")
def project_progress(
    project_id: int
):

    return get_project_progress(
        project_id
    )


@router.get("/recent")
def recent_projects():

    projects = get_projects()

    return projects[:5]


@router.put("/{project_id}")
def edit_project(project_id: int, data: ProjectCreate, request: Request):

    admin_only(request.session.get("user"))

    return update_project(project_id, data)
