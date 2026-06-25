# routers/auth.py

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Response
from fastapi import Cookie
from fastapi import Request
from models.login import LoginRequest


from models.user import UserCreate

from services.auth_service import (
    register_user,
    login_user,
    get_user_profile
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")

def register(data: UserCreate):

    result = register_user(data)

    if not result["success"]:

        raise HTTPException(
            status_code=400,
            detail=result["message"]
        )

    return result

from fastapi import Form


@router.post("/login")
def login(
    request: Request,
    response: Response,
    email: str = Form(...),
    password: str = Form(...),
):
    user = login_user(
        email,
        password
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    request.session["user"] = {

        "id":
        user["User_id"],

        "username":
        user["Username"],

        "email":
        user["Mail"],

        "role":
        user["Role"]
    }

    response.set_cookie(

        key="user_email",

        value=user["Mail"],

        httponly=True,

        max_age=86400
    )

    return {

    "message":
    "Login Success",

    "role":
    user["Role"]
}


@router.get("/logout")

def logout(
    request:Request
):

    request.session.clear()

    return {

        "message":
        "Logged Out"
    }

@router.get("/")
def auth_test():

    return {
        "message": "Auth API Working"
    }


@router.get("/me")
def current_user(request: Request):

    user = request.session.get("user")

    if not user:
        raise HTTPException(status_code=401, detail="Not Logged In")

    return user


@router.get("/check-employee")
def check_employee(
    request: Request
):

    user = request.session.get(
        "user"
    )

    if not user:

        return {
            "authorized":False
        }

    return {

        "authorized":

        user["role"]=="Employee"
    }
