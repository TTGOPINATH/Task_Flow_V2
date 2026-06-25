from pydantic import BaseModel

class TaskCreate(BaseModel):

    project_id:int

    task_name:str

    description:str

    assigned_by:str

    assigned_to:str

    deadline:str

    status:str