from pydantic import BaseModel
from typing import Optional

class WorkspaceBase(BaseModel):
    name: str
    description: Optional[str] = None

class WorkspaceCreate(WorkspaceBase):
    pass

class Workspace(WorkspaceBase):
    id: int

    class Config:
        from_attributes = True # This is important for SQLAlchemy