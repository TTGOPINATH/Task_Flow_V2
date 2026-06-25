# models/project.py

from pydantic import BaseModel


class ProjectCreate(BaseModel):

    project_name: str

    description: str

    created_on: str

    deadline: str
