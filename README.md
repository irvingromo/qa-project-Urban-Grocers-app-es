Proyecto de Pruebas de API - Creación de Kits de Usuario

## Descripción
Este proyecto contiene pruebas automatizadas para la API de Urban Grocers. El objetivo específico es verificar la funcionalidad de creación de un kit de productos ("kit personal") para un usuario recién creado. Las pruebas validan distintos escenarios (positivos y negativos) para el campo `name` del kit, comprobando los límites de caracteres, tipos de datos y manejo de campos vacíos.

## Requisitos previos
- Python 3 instalado.
- Paquetes necesarios: `pytest` y `requests`.

## Cómo ejecutar las pruebas
1. Asegúrate de actualizar la variable `URL_SERVICE` en el archivo `configuration.py` con la URL actual de tu servidor.
2. Abre tu terminal.
3. Navega al directorio donde se encuentran los archivos del proyecto.
4. Ejecuta el siguiente comando:
   ```bash
   pytest create_kit_name_kit_test.py
