from fastapi import APIRouter
from fastapi import Request

from services.user_service import (
get_users
)

from services.role_service import (
admin_only
)

router = APIRouter(
prefix="/users",
tags=["Users"]
)

@router.get("/")
def all_users(
    request: Request
):
    admin_only(
        request.session.get(
            "user"
        )
    )

    return get_users()

