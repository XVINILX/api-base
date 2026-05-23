import re

from pydantic import BaseModel, EmailStr, field_validator

class PasswordValidator:
    """Classe separada para validação de senha"""
    
    @staticmethod
    def validate(password: str) -> tuple[bool, list[str]]:
        errors = []
        
        # Regras
        if len(password) < 8:
            errors.append('Mínimo 8 caracteres')
        
        if len(password) > 128:
            errors.append('Máximo 128 caracteres')
        
        if not re.search(r'[A-Z]', password):
            errors.append('Pelo menos 1 letra maiúscula')
        
        if not re.search(r'[a-z]', password):
            errors.append('Pelo menos 1 letra minúscula')
        
        if not re.search(r'\d', password):
            errors.append('Pelo menos 1 número')
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append('Pelo menos 1 caractere especial')
        
        # Não permite espaços
        if ' ' in password:
            errors.append('Não pode conter espaços')
        
        # Não permite caracteres repetidos em sequência (ex: "aaa")
        if re.search(r'(.)\1{2,}', password):
            errors.append('Evite caracteres repetidos em sequência')
        
        return len(errors) == 0, errors

class Login(BaseModel):
    password: str
    email: EmailStr
    
class Register(BaseModel):
    email: EmailStr
    name: str
    password: str
    
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        is_valid, errors = PasswordValidator.validate(v)
        
        if not is_valid:
            error_msg = "Senha inválida:\n- " + "\n- ".join(errors)
            raise ValueError(error_msg)
        
        return v
    
class NovaSenha(BaseModel):
    password: str
    
class EsqueciASenha(BaseModel):
    email: EmailStr