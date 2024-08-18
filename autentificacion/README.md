# Microservicio de Autentificación

Este microservicio permite gestionar usuarios, permite controlar Login, Logout, Register y Autentification utilizando una arquitectura basada en microservicios. 

# Estructura de Autentificación

```
├──autentificacion/
│    ├── .dockerignore
│    ├── Dockerfile
│    ├── config/
│    |   ├── conf_firebase.json
│    |   ├── conf.json
│    ├── README.md
│    ├── main.py
│    └── requirements.txt
```
# Importante

- El directorio config debe ser creado con los archivos especificados en la estructura.
- Tener una cuenta de Firebase.
- Crear un proyecto en firebase y configurar el servicio de autentificación.
## conf_firebase.json
```
{
  "type": 
  "project_id": 
  "private_key_id": 
  "private_key": 
  "client_email": 
  "client_id": 
  "auth_uri":
  "token_uri": 
  "auth_provider_x509_cert_url":
  "client_x509_cert_url":
  "universe_domain": 
  }
```

## conf.json
```
{
    "firebase_api_key": 
}
```
