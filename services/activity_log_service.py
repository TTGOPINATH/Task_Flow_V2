
from database.db import get_connection


def log_activity(
    username,
    activity
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO activity_logs(

            Username,
            Activity

        )

        VALUES(%s,%s)
        """,

        (
            username,
            activity
        )
    )

    connection.commit()

    connection.close()