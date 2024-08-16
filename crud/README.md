# Microservicio CRUD de Productos

Este microservicio permite gestionar productos en una tienda utilizando una arquitectura basada en microservicios. El servicio incluye operaciones para crear, leer, actualizar y eliminar (CRUD) productos, junto con la gestión de categorías y usuarios. El microservicio está desarrollado en FastAPI y utiliza PostgreSQL como base de datos, todo gestionado a través de contenedores Docker.
## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
├── app/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ └── database.py
├── alembic.ini
└── migrations/
```


## Archivos Principales

1. **main.py**: Contiene la configuración de la aplicación FastAPI y las rutas para el CRUD de productos.

2. **models.py**: Define los modelos de datos para productos, categorías y usuarios, utilizando SQLAlchemy.

3. **schemas.py**: Define los esquemas Pydantic que se utilizan para validar y serializar los datos de entrada y salida.

4. **crud.py**: Implementa las operaciones CRUD para interactuar con la base de datos.

5. **database.py**: Configura la conexión a la base de datos PostgreSQL.

6. **alembic.ini**: Archivo de configuración para Alembic, que gestiona las migraciones de la base de datos.

7. **Dockerfile**: Define la imagen de Docker para el microservicio.





## Configuración del Entorno


### Configuración de Docker

Asegúrate de tener Docker y Docker Compose instalados. El archivo docker-compose.yml define dos servicios principales:

app: El servicio que ejecuta la aplicación FastAPI.
db: El servicio que ejecuta la base de datos PostgreSQL.

```
version: '3.8'

services:
  app:
    build: .
    volumes:
      - .:/app
    ports:
      - "8001:8000"
    depends_on:
      - db
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: mysecretpassword123
      POSTGRES_DB: cms_db
    ports:
      - "5432:5432"
```

## Migraciones de Base de Datos con Alembic
Alembic se utiliza para gestionar las migraciones de la base de datos. Las migraciones permiten que los cambios en los modelos de datos se reflejen en la estructura de la base de datos.

### Crear una Migración
Dentro del contenedor de la aplicación, ejecuta el siguiente comando para generar una migración automática basada en los modelos actuales:

```
docker-compose exec app alembic revision --autogenerate -m "Initial migration for products, categories, and users"
```

### Aplicar la Migración
Aplica la migración para crear las tablas en la base de datos:

```
docker-compose exec app alembic upgrade head
```

### Tomar en consideracion 
Se debe ejectuar lo siguiente antes de ejecutar


```
export PYTHONPATH=/app
```


