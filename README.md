# Ubuntu Pyspark

Este container esta diseñado para ejecutarlo con Remote-Containers, extensión de vscode.

## Pasos de instalación

1. Crear imagen
   `docker build -t spark-ubuntu .`

2. Ejecutar container
   `docker run -it spark-ubuntu /bin/bash`

3. En vscode, ctrl-shift-p y escoger "Attach to Running Container"

## Guardar cambios

1. Obtener el id del container (docker ps) y ejecutar:
   `docker commit <container-id> <nueva-imagen>`

2. Ahora se debe ejecutar el container con la nueva imagen
   `docker run -it <nueva-imagen> /bin/bash`
