from database.db import get_connection

def add_comment(
    task_id,
    username,
    comment
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO task_comments(

            Task_id,
            Username,
            Comment_Text

        )

        VALUES(%s,%s,%s)
        """,

        (
            task_id,
            username,
            comment
        )
    )

    connection.commit()

    connection.close()