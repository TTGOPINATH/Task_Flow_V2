from fastapi import HTTPException

def admin_only(user):

    if user["role"] != "Admin":

        raise HTTPException(

            status_code=403,

            detail="Admin Only"
        )
        
def admin_only(user):

    if user["role"] != "Admin":

        raise HTTPException(
            status_code=403,
            detail="Admin Access Only"
        )


def employee_or_admin(user):

    if user["role"] not in [
        "Admin",
        "Employee"
    ]:

        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )