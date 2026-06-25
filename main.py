from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from routers import users
from utils.auth import admin_only
from utils.auth import employee_only
from routers import auth
from routers import projects
from routers import tasks
from starlette.middleware.sessions import SessionMiddleware
from routers import reports
from routers import attachments
from services.project_service import update_project

app = FastAPI()

# APIs
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(
    users.router
)
app.add_middleware(
    SessionMiddleware,
    secret_key="taskflow2026_demo_project_secret"
)
app.include_router(auth.router)
app.include_router(
    reports.router
)
app.include_router(
    attachments.router
)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Static Files
app.mount(

    "/uploads",

    StaticFiles(
        directory="uploads"
    ),

    name="uploads"
)

# Dashboard Page
@app.get("/")
def dashboard(
    request: Request
):

    if not request.session.get("user"):

        return RedirectResponse(
            "/login",
            status_code=302
        )

    return FileResponse(
        "frontend/dashboard.html"
    )
# Projects Page
@app.get("/projects-page")
def projects_page(
    request: Request
):

    admin_only(
        request.session.get(
            "user"
        )
    )

    return FileResponse(
        "frontend/projects.html"
    )

# Tasks Page
@app.get("/tasks-page")
def tasks_page(
    request: Request
):

    admin_only(
        request.session.get(
            "user"
        )
    )

    return FileResponse(
        "frontend/tasks.html"
    )

# Project Details Page
@app.get("/project-details")
def project_details(
    request: Request
):

    if not request.session.get("user"):

        return RedirectResponse(
            "/login",
            status_code=302
        )

    return FileResponse(
        "frontend/project-details.html"
    )

@app.get("/logout")
def logout(
    request: Request
):

    request.session.clear()

    return RedirectResponse(
        "/login",
        status_code=302
    )

@app.get("/users-page")
def users_page(
    request: Request
):

    admin_only(
        request.session.get(
            "user"
        )
    )

    return FileResponse(
        "frontend/users.html"
    )

@app.get(
    "/completed-projects-page"
)
def completed_projects_page(
    request: Request
):

    admin_only(
        request.session.get(
            "user"
        )
    )

    return FileResponse(
        "frontend/completed-projects.html"
    )

@app.get("/login")
def login_page():

    return FileResponse(
        "frontend/login.html"
    )

@app.get(
    "/employee-dashboard"
)
def employee_dashboard(
    request: Request
):

    employee_only(
        request.session.get(
            "user"
        )
    )

    return FileResponse(
        "frontend/employee-dashboard.html"
    )

@app.get(
    "/reports-page"
)
def reports_page(
    request: Request
):

    admin_only(
        request.session.get(
            "user"
        )
    )

    return FileResponse(
        "frontend/reports.html"
    )


@app.get("/register")
def register_page():

    return FileResponse("frontend/register.html")


from fastapi.responses import FileResponse


@app.get("/favicon.ico")
async def favicon():

    return FileResponse("static/task.png")
