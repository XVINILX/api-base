from fastapi import APIRouter

from src.base_project_user.schemas.auth import EsqueciASenha, Login, NovaSenha, Register

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register")
async def register(data: Register):
    print(data)
    return data

@router.post("/login")
async def login(data: Login):
    print(data)
    return data

@router.post("/nova_senha")
async def nova_senha(data: NovaSenha):
    print(data)
    
@router.post("/esqueci_a_senha")
async def esqueci_a_senha(data: EsqueciASenha):
    print(data)