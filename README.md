# Proyecto de Pruebas de API - Creación de Kits de Usuario

## Descripción
Este proyecto contiene pruebas automatizadas para la API de la aplicación. El objetivo es verificar la funcionalidad de creación de un kit de productos ("kit personal") para un usuario recién creado, validando distintos escenarios para el campo `name` según los límites y restricciones establecidas.

## Documentación
- **Fuente de documentación utilizada:** apiDoc (Documentación oficial de la API del proyecto).

## Tecnologías y técnicas utilizadas
- **Lenguaje:** Python 3.
- **Librerías:** 
  - `requests` para el envío de peticiones HTTP.
  - `pytest` para la ejecución y estructuración de las pruebas automatizadas.
- **Técnicas:**
  - Pruebas de API REST (validación de códigos de estado y cuerpos de respuesta JSON).
  - Parametrización y modificación dinámica del cuerpo de las peticiones.
  - Uso de aserciones (`assert`) para validaciones positivas (código 201) y negativas (código 400).
  - Manejo de Tokens de Autorización (Auth Token) en los encabezados (`headers`).

## Cómo ejecutar las pruebas
1. Asegúrate de actualizar la variable `URL_SERVICE` en el archivo `configuration.py` con la URL actual de tu servidor.
2. Abre la terminal de comandos.
3. Ejecuta el siguiente comando:
   ```bash
   pytest create_kit_name_kit_test.py
