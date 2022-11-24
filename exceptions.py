from fastapi import HTTPException, status
from urllib.request import Request
from fastapi.responses import JSONResponse

server_error_exception = HTTPException(
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="The request could not be completed."
    )

def entity_error_exception(type,id):
    return HTTPException(
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail=f"The {type} with the id {id} is not in the database."
    )
