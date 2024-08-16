# Grupo 03
### Karla Ansatuña
### Leonardo Obando
### Alex Trejo

# Microservices

Este proyecto es un microservicio para gestionar un crud de productos de coffes y atentificacion de usarios utilizando FastAPI, PostgreSQL, Firebase y Kong. A continuación se detalla la configuración, el proceso de instalación y el uso de este microservicio.

## Estructura del Proyecto
```
Microservicios
│
├──autentificacion/
│    ├── .dockerignore
│    ├── Dockerfile
│    ├── README.md
│    ├── main.py
│    ├── requirements.txt
│    │
├── crud/
│   │
│   ├── app/
│   │   ├── _init_.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │
│   ├── migrations/
│   │   ├── versions/
│   │   │   ├── d07e15dd385d_initial_migration.py
│   │   ├── README.md
│   │   ├── env.py
│   │   ├── script.py.mako
│   │
│   ├── .gitignore
│   ├── Dockerfile
│   ├── README.md
│   ├── alembic.ini
│   ├── requirements.txt
│
├── .gitignore
├──README.md
├── docker-compose.yml
├── kong.yml
```
## Requistos

- Docker

## Comandos de Ejecucion

Usa el siguiente comando para lanzar la aplicacion de microservicios:

### Para usar el microservicio 
```
docker-compose up --build -d
```
# Nota 

Para una correcta ejecucion y configuracion visitar los archivos *README.md* de cada Microservicio