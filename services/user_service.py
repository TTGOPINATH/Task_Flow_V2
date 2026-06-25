from database.db import get_connection

def get_users():
    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT

            User_id,
            Username,
            Mail,
            Role

        FROM users

        ORDER BY User_id
        """
    )

    users = cursor.fetchall()

    connection.close()

    return users
