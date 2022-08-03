# Xepelin Desafío Tecnico



# MVP Notifiaciones

## Decidí utilizar la herramienta "Google Scripts", la misma es agil para crear scripts y además de que para trabajar con google sheets es una herramienta accesible y compatible.

Para acceder al proyecto podrán desde el link: https://script.google.com/macros/s/AKfycbwKfK3UnaWhhTzHReNYKcFGNXn_3ANwD71S36YskIU_j_tvVE8z1LvS5LjAjZ6j4kxtyw/exec

Aclaración: La parte que no esta realizada del la aplicación web es pegarle al POST que envía la notificación del mail. De todas maneras el google sheet se puede editar desde la aplicación Web y los registros se guardan de igual manera.

## Funciones:

**La WebApplication que construí se compone de 3 archivos principales:**

<img width="227" alt="image" src="https://user-images.githubusercontent.com/96205624/182504916-1b4d45b4-26f8-4958-99cb-4b4804d8eb21.png">

Voy a resumir que es lo que hace cada uno:


### Código.gs:
- Se encuentra el serivicio que crea la pagina web:
<img width="1149" alt="image" src="https://user-images.githubusercontent.com/96205624/182505596-3c8c1d3f-ddf1-4919-99d6-2edb334ab6e2.png">



### DataServerSide.gs:
- Son las funciones que se utilizan para extraer la data del Gdoc, la conexión con el mismo. 
<img width="895" alt="image" src="https://user-images.githubusercontent.com/96205624/182505431-47d55c1e-a3e6-4286-95ed-0825e2e607d4.png">

- En la función **ediTasa**: la utilizamos para realizar el editado del gdoc desde la webApp.
<img width="856" alt="image" src="https://user-images.githubusercontent.com/96205624/182505748-af2b3f48-f6c9-4cdf-84bc-7e80bb637610.png">



### MAIN.HTML:
- En el mismo se encuentra todo lo relacionado con lo HTML de la pagina y pequeñas funciones de carga de información:

- En la función **loadData** la utilizamos para traer la información desde **DataServerSide.gs** y mostramos un mensaje de edición.
<img width="895" alt="image" src="https://user-images.githubusercontent.com/96205624/182505431-47d55c1e-a3e6-4286-95ed-0825e2e607d4.png">





# Recursos: 

Lenguaje: JavaScript, HTML, CSS

Gdoc: https://docs.google.com/spreadsheets/d/1zA3A85jCN7EceEUN6VAgMKceBmKQU6WeHdPaiU_PiQo/edit#gid=0

Tabulator: http://tabulator.info/docs/5.3/events

GoogleWebApp: https://script.google.com/macros/s/AKfycbwKfK3UnaWhhTzHReNYKcFGNXn_3ANwD71S36YskIU_j_tvVE8z1LvS5LjAjZ6j4kxtyw/exec
