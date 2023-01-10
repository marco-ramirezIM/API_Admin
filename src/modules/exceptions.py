from fastapi import HTTPException

module_not_found_exception = HTTPException(404, detail="Módulo no encontrado")
category_not_found_exception = HTTPException(404, detail="Categoría no encontrada")
clusters_associated_to_modules_exception = HTTPException(400, detail="El módulo tiene clústeres asociados")
module_name_repeated_exception = HTTPException(403, "El nombre del módulo que está intentando crear ya existe")