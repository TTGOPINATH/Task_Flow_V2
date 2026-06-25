# services/auth_service.py

from multiprocessing.dummy import connection

from database.db import get_connection
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)


def register_user(data):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE Mail=%s
        """,
        (data.user_email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:

        connection.close()

        return {
            "success": False,
            "message": "Email already registered"
        }

    hashed_password = pwd_context.hash(
        data.password
    )

    cursor.execute(
        """
    INSERT INTO users(

        Username,
        Mail,
        Password,
        Role

    )

    VALUES(%s,%s,%s,%s)
    """,
        (data.username, data.user_email, hashed_password, data.role),
    )

    connection.commit()

    connection.close()

    return {
        "success": True,
        "message": "User Registered Successfully"
    }


def login_user(email, password):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE Mail=%s
        """,
        (email,)
    )

    user = cursor.fetchone()

    connection.close()

    if not user:

        return None

    if not pwd_context.verify(
        password,
        user["Password"]
    ):

        return None

    return user


def get_user_profile(email):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT

            User_id,
            Username,
            Mail,
            Role

        FROM users

        WHERE Mail=%s
        """,
        (email,)
    )

    user = cursor.fetchone()
    connection.close()

    return user
