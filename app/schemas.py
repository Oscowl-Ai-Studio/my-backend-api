from pydantic import BaseModel

class WorkspaceBase(BaseModel):
    name: str
    description: str = None

class WorkspaceCreate(WorkspaceBase):
    pass

class Workspace(WorkspaceBase):
    id: int

    class Config:
        orm_mode = True