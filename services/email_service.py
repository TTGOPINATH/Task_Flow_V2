import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart


def send_task_email(

    employee_email,
    task_name,
    project_id,
    deadline

):

    sender_email = "yourgmail@gmail.com"

    sender_password = "YOUR_APP_PASSWORD"

    subject = "New Task Assigned"

    body = f"""
Hello,

A new task has been assigned to you.

Task Name : {task_name}

Project ID : {project_id}

Deadline : {deadline}

Please login to TaskFlow and begin your work.

Regards,
TaskFlow Team
"""

    message = MIMEMultipart()

    message["From"] = sender_email

    message["To"] = employee_email

    message["Subject"] = subject

    message.attach(
        MIMEText(
            body,
            "plain"
        )
    )

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        sender_email,
        sender_password
    )

    server.send_message(
        message
    )

    server.quit()
    
def send_completion_email(

    admin_email,
    task_name

):

    sender_email = "yourgmail@gmail.com"

    sender_password = "YOUR_APP_PASSWORD"

    message = MIMEMultipart()

    message["From"] = sender_email

    message["To"] = admin_email

    message["Subject"] = "Task Completed"

    body = f"""

Task Completed

Task:

{task_name}

has been completed.

Regards,
TaskFlow
"""

    message.attach(
        MIMEText(
            body,
            "plain"
        )
    )

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        sender_email,
        sender_password
    )

    server.send_message(
        message
    )

    server.quit()