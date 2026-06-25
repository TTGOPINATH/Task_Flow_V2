from database.db import get_connection


def save_attachment(

    task_id,
    filename,
    filepath

):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """
        INSERT INTO attachments(

            Task_id,
            File_name,
            File_path

        )

        VALUES(%s,%s,%s)
        """,

        (
            task_id,
            filename,
            filepath
        )
    )

    connection.commit()

    connection.close()

    return {

        "message":
        "File Uploaded"
    }


def get_task_files(
    task_id
):

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(

        """
        SELECT *
        FROM attachments
        WHERE Task_id=%s
        """,

        (task_id,)
    )

    files = cursor.fetchall()

    connection.close()

    return files