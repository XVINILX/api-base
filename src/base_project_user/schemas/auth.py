from pydantic import BaseModel, EmailStr


class Login(BaseModel):
    password: str
    email: EmailStr
    
class Register(BaseModel):
    email: EmailStr
    name: str
    password: str
    
class NovaSenha(BaseModel):
    password: str
    
class EsqueciASenha(BaseModel):
    email: EmailStr