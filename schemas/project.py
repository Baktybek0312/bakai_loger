from pydantic import BaseModel, Field


class ProjectBase(BaseModel):
    code: str = Field(gt=2, lt=220)
    name: str = Field(gt=2)


class ProjectList(ProjectBase):
    class Config:
        orm_mode = True
