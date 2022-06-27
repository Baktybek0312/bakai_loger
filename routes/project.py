from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from schemas.project import ProjectBase, ProjectList
from db.database import get_db

router = APIRouter(
    tags=['Project'],
    prefix='/project'
)


@router.post('/create', status_code=status.HTTP_200_OK)
async def create_project(project: ProjectBase, db: Session = Depends(get_db)):
    pass
