# Para que python interprete una carpeta de modulos como un paquete completo, debe existir el archivo "__init__.py" dentro de la carpeta que se quiere que sea un paquete.
# Por buenas practicas, se importan los modulos en este mismo archivo __init__.py
from .paquete1 import funcion_primera
from .paquete2 import funcion_segunda