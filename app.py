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

#route for students

@router_v1.get('/students')
async def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()
    
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
    newstudent = models.Student( id=student['id'], firstname=student['firstname'], lastname=student['lastname'], dob=student['dob'], gender=student['gender'])
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


#route for books
@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

#route for coffees
@router_v1.get('/coffees')
async def get_coffess(db: Session = Depends(get_db)):
    return db.query(models.Coffee).all()

#route for orderDetail 
@router_v1.get('/orderDetail')
async def get_orderDetails(db: Session = Depends(get_db)):
    return db.query(models.OrderDetail).all()

@router_v1.get('/orderDetail/{order_id}')
async def get_orderDetail(order_id: int,db: Session = Depends(get_db)):
    return db.query(models.OrderDetail).filter(models.OrderDetail.order_id == order_id).all()

#route for order
@router_v1.get('/order')
async def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router_v1.get('/order/{order_id}')
async def get_order(order_id: int,db: Session = Depends(get_db)):
    return db.query(models.OrderDetail).filter(models.OrderDetail.order_id == order_id).all()

# class createOrderRequst():
#     note: int
#     coffees_list: dict
    
# example data body
# {
#         "note": "i think we should do this",
#         "order_list": 
#             [
#                 {
#                 "coffee_id": 1,
#                 "quantity": 3
#             },
            
#             {
#                 "coffee_id": 3,
#                 "quantity": 2
#             }
#             ]
#     }




@router_v1.post('/createOrder') #createOrder
async def create_order(request: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newOrderDetail = list()
    newOrder = models.Order(id=db.query(models.Order).count()+1, note=request["note"])
    db.add(newOrder)
    
    for data in request["order_list"]:
        newCoffee = models.OrderDetail(order_id=newOrder.id, coffee_id=data["coffee_id"], quantity=data["quantity"])
        db.add(newCoffee)
        newOrderDetail.append(data)
        
    db.commit()
    return newOrderDetail



app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)


