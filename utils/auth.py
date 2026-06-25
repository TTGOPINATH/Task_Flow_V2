from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def admin_only(user):

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Login Required"
        )

    if user["role"] != "Admin":

        raise HTTPException(
            status_code=403,
            detail="Admin Access Only"
        )


def employee_only(user):

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Login Required"
        )