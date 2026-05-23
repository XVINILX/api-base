from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

from schemas.auth import Register
from schemas.user import User


ph = PasswordHasher(memory_cost=65536,  # 64 MiB (64 * 1024)
                    time_cost=3,        # 3 iterações
                    parallelism=1)  
        
class AuthService:
    
    @staticmethod
    def hash_password(password:str) -> str:
        

        
        hash_senha = ph.hash(password=password)
        
        return hash_senha
    
    @staticmethod
    def verify_password(password: str, hash_password) -> bool:
        try:
            ph.verify(hash_password, password)
            
            return True
        except VerificationError:
            return False
        
    @staticmethod
    def register(user: Register) -> User:
        
        return User(name="")