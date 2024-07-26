from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import delete, update

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/students')
async def get_students(db: Session = Depends(get_db)):
    #return db.query(models.Student).all()
    return "อิอิ"

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()


@router_v1.post('/students/testbody')
async def get_student(student: dict, db: Session = Depends(get_db)):
    print()
    return student

@router_v1.get('/students/{student_id}') #read
async def get_student(student_id: str, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

@router_v1.post('/students') #create
async def create_student(student: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newstudent = models.Student(id=student['id'], firstname=student['firstname'], lastname=student['lastname'], dob=student['dob'], gender=student['gender'])
    db.add(newstudent)
    db.commit()
    db.refresh(newstudent)
    response.status_code = 201
    return newstudent

@router_v1.patch('/students/{student_id}') #update
async def update_student(student_id: str, student: dict, response: Response, db: Session = Depends(get_db)):
    result = db.execute(update(models.Student).where(models.Student.id == student_id).values(student))
    db.commit()
    response.status_code = 201
    return db.query(models.Student).all()


@router_v1.delete('/students/{student_id}') #delete
async def delete_student(student_id: str, response: Response, db: Session = Depends(get_db)):
    result = db.execute(delete(models.Student).where(models.Student.id == str(student_id)))
    db.commit()
    response.status_code = 200
    return db.query(models.Student).all()



app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
