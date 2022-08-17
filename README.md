# Redes_Proyecto1

## Librerias utilizadas
slixmpp
xmpppy

## Funcionalidades
1. Creacion de cuenta
  Input:
  - Usuario
  - Clave

2. Login
  - Usuario
  - Clave

3. Logout

4. Eliminacion de cuenta

5. Mostrar usuarios
  Output:
  - JID
  - Mensaje presencia
  - Status

6. Agregar contacto
  Input:
  - Usuario

7. Detalles de contacto
  Input:
  - Usuario
  Output:
  - JID
  - Mensaje presencia
  - Status

8. Mensaje directo
  Input:
  - Usuario
  Loop:
  - Reply a los mensajes

9. Group chat
  ---

10. Presencia
  Input:
  - Mensaje presencia
  Output:
  - Enviado al servidor

11. Notificaciones
  ---

12. Archivos
  ---

## Presentacion
### Caracteristicas
Las caracteristicas implementadas estan descritas anteriormente.
Mensaje grupal, notificaciones y archivos no se puedieron implementar.
Otras de las caracteristicas, como lo es el mensaje de presencia, realizan su trabajo, pero no siempre se ve reflejado.

### Dificultades
Fue un proyecto complicado, porque las librerias no tenian documentacion suficiente.
Lo empeze a trabajar en JS, pero resulto con varios problemas, por lo que decidi pasarme a Python.
Por un momento, tambien pense en realizarlo sin libreria en C++, pero por falta de conocimiento al inicio del proyecto, decidi mejor irme a algo mas seguro.

### Lecciones
Una vez comprendi bien el proceso de coneccion, hubiera querido realizar todo de mejor manera. Creo que la libreria me limito hasta cierto punto, porque habian funcionalidades para las que conocia como debia ser armada la stanza, pero por no tener suficiente documentacion, costo mas de lo esperado.
A parte, aprendi mucho sobre autentificacion SASL, porque una de las librerias utilizaba este tipo, y no lograba realizar la autenticacion por este metodo.
A pesar de esto, me parecio muy interesante el protocolo, por su uso en diferentes aplicaciones.