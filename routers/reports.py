from fastapi import APIRouter, Request

from fastapi.responses import StreamingResponse

from services.role_service import admin_only

from services.report_service import generate_project_report

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/projects")
def projects_report(request: Request):

    admin_only(request.session.get("user"))

    pdf = generate_project_report()

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=projects_report.pdf"},
    )
