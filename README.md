# Proyecto de Servidor y Cliente TCP

Este proyecto implementa un servidor y un cliente TCP en Python. El servidor acepta múltiples conexiones simultáneas de clientes y responde con los mensajes recibidos en mayúsculas. Además, permite a los clientes desconectarse enviando el mensaje `"DESCONEXION"`.


## Instrucciones para ejecutar el proyecto

### Requisitos Previos
- Asegúrate de tener Python instalado en tu sistema (versión 3.6 o superior).
- Descarga o clona este repositorio en tu máquina.

### Ejecutar el Servidor

1. Navega al directorio donde está el archivo del servidor (`server.py`).
2. Ejecuta el siguiente comando en la terminal:   `python server.py`

### Ejecutar Cliente 

1. En la misma ubicacion del proyecto abre una nueva terminal
2. Ejecuta el siguiente comando:   `python client.py`

Este proyecto incluye dos pruebas manuales para verificar su funcionamiento:

1. **Prueba de Mensaje Normal**
   - Enviar un mensaje de texto normal desde el cliente (por ejemplo, `"hola"`).
   - Verificar que el servidor responda con el mensaje en mayúsculas (por ejemplo, `"HOLA"`).

2. **Prueba de Desconexión**
   - Enviar el mensaje `"DESCONEXION"` desde el cliente.
   - Verificar que la conexión se cierre correctamente en ambos lados (tanto el cliente como el servidor deberían indicar que la conexión se ha cerrado).
