from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class ProjectBase(BaseModel):
    id: int
    code: str = Field(gt=2, lt=220)
    name: str = Field(gt=2)


class TablesBase(BaseModel):
    id: int
    project_id: int
    table_name: str

    class Config:
        orm_mode = True


class Manager(BaseModel):
    id: int
    name: str
    branch: str


