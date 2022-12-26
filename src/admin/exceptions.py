from fastapi import HTTPException, status
from urllib.request import Request
from fastapi.responses import JSONResponse


duplicated_value_exception = HTTPException(403, "Estas intentando guardar un dato que ya se encuentra registrado en la base de datos, por favor revisa los datos del formulario nuevamente")