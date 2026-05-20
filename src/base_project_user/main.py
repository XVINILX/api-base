from fastapi import FastAPI, Request
from src.base_project_user.core.HttpException import HttpExceptionHandler
from src.base_project_user.routes import auth
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()


app.include_router(auth.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Catch request validation errors and return a custom JSON structure.
    """
    status_code = 422
    message = [
                {
                    "loc": err["loc"],
                    "msg": err["msg"],
                    "type": err["type"]
                }
                for err in exc.errors()
            ]
    return HttpExceptionHandler(status_code=status_code, message=message)