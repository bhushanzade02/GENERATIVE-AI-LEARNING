from pydantic import BaseModel ,EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name : str = "Bhushan"
    age : Optional[int] = None
    email : EmailStr = None
    cgpa : float = Field(gt =0 , lt =10 , default =6 ,description = 'cpga value')


new_student ={"age":'32','email':'bhuhan@gmail.com', 'cgpa':5}

student = Student(**new_student)

print(student)