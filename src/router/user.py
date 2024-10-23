from fastapi import APIRouter,HTTPException
from src.models.user import User
from database.database import SessionLocal
from src.schemas.user import User_Create_Schema,User_Return_Schema
db=SessionLocal()


user_router = APIRouter()




import uuid

@user_router.post("/create_user",response_model=User_Return_Schema)
def create_user(user: User_Create_Schema):
    new_user = User(id = str(uuid.uuid4()),name=user.name, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    return new_user


@user_router.get("/get_all_user",response_model=list[User_Return_Schema])
def get_all_user():
    find_all_user = db.query(User).all()
    return find_all_user


@user_router.get("/get_user/{id}", response_model=User_Return_Schema)
def get_user(id: str):
    find_user = db.query(User).filter(User.id == id).first()
    if not find_user:
        raise HTTPException(status_code=404,detail="user id not found")
    return find_user

@user_router.put("/update_user/{id}", response_model=User_Return_Schema)
def update_user(id: str, user: User_Create_Schema):
    find_user = db.query(User).filter(User.id == id).first()
    if not find_user:
        raise HTTPException(status_code=404, detail="user id not found")
    find_user.name = user.name
    find_user.email = user.email
    find_user.password = user.password
    db.commit()
    return find_user




@user_router.delete("/delete_user/{id}")
def delete_user(id: str):
    find_user = db.query(User).filter(User.id == id).first()
    if not find_user:
        raise HTTPException(status_code=404, detail="user id not found")
    db.delete(find_user)
    db.commit()
    return {"message": "user deleted successfully"}


@user_router.patch("/update_user_partial", response_model=PatchUserSchema)
def update_user_partial(user_id: str, user: PatchUserSchema):
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Use the new Pydantic v2 `model_dump` to get fields that are not None
    user_data = user.model_dump(exclude_unset=True)
    print(type(user_data))
    breakpoint()

    # Iterate through the fields and update them dynamically
    for key, value in user_data.items():
        # if key == "password":
        #     # Special case for password: hash it before storing
        #     setattr(db_user, key, pwd_context.hash(value))
        # else:
            setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    
    return db_user