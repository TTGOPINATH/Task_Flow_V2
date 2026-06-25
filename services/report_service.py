from io import BytesIO

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime

from database.db import get_connection


def generate_project_report():

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("TaskFlow Project Report", styles["Title"]))

    elements.append(
        Paragraph(
            f"Generated On : {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"],
        )
    )

    elements.append(Spacer(1, 20))

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM projects
        ORDER BY Project_id
        """)

    projects = cursor.fetchall()

    elements.append(Paragraph(f"Total Projects : {len(projects)}", styles["Heading2"]))

    elements.append(Spacer(1, 10))

    table_data = [["ID", "Project Name", "Status", "Created On", "Deadline"]]

    for project in projects:

        table_data.append(
            [
                str(project["Project_id"]),
                str(project["Project_name"]),
                str(project["Project_Status"]),
                str(project["Created_on"]),
                str(project["Deadline"]),
            ]
        )

    table = Table(table_data)

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )

    elements.append(table)

    doc.build(elements)

    buffer.seek(0)

    connection.close()

    return buffer
