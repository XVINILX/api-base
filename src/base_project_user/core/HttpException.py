from fastapi.responses import JSONResponse


def HttpExceptionHandler(status_code, message):
    """
    Catch request validation errors and return a custom JSON structure.
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "message":  message
        }
    ) 
    