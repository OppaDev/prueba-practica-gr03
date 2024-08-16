from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
import firebase_admin
from firebase_admin import credentials, auth
from typing import Optional
import logging
import requests

app = FastAPI()

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Credenciales de Firebase
cred = credentials.Certificate('config/conf_firebase.json')
firebase_admin.initialize_app(cred)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

class User(BaseModel):
    email: EmailStr
    password: str
    display_name: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        logger.error(f"Error verifying token: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciales inválidas',
            headers={'WWW-Authenticate': 'Bearer'},
        )

@app.post('/register', status_code=status.HTTP_201_CREATED)
async def register(user: User):
    try:
        user_record = auth.create_user(
            email=user.email,
            email_verified=False,
            password=user.password,
            display_name=user.display_name,
        )
        return {"mensaje": "Usuario creado", "uid": user_record.uid}
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='El correo ya está registrado',
        )
    except auth.WeakPasswordError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='La contraseña es muy débil',
        )
    except auth.InvalidEmailError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='El correo no es válido',
        )
    except Exception as e:
        logger.error(f"Error in register: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.post('/login', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user = auth.get_user_by_email(form_data.username)
        # Nota: Aquí deberías verificar la contraseña, pero Firebase Admin SDK no lo permite directamente
        # En un entorno de producción, considera usar Firebase Authentication REST API para la verificación de contraseñas
        
        # Crear un token personalizado
        custom_token = auth.create_custom_token(user.uid)
        
        # Intercambiar el token personalizado por un token de ID
        firebase_api_key = "AIzaSyAoEW1lSkpnOO2DE2K8nlAohIXIG5-jtdg"  # Necesitas obtener esto de tu configuración de Firebase
        response = requests.post(
            f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={firebase_api_key}",
            json={"token": custom_token.decode(), "returnSecureToken": True}
        )
        
        id_token = response.json()['idToken']
        
        return {"access_token": id_token, "token_type": "bearer"}
    except auth.UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='El usuario no existe',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except Exception as e:
        logger.error(f"Error in login: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.post('/logout')
async def logout(current_user: dict = Depends(get_current_user)):
    try:
        auth.revoke_refresh_tokens(current_user['uid'])
        return {"mensaje": "Sesión cerrada"}
    except Exception as e:
        logger.error(f"Error in logout: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Error al cerrar sesión',
        )

@app.get('/me', response_model=dict)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

@app.on_event("startup")
async def startup_event():
    logger.info("Rutas registradas:")
    for route in app.routes:
        logger.info(f"  {route.methods} {route.path}")

@app.get("/test")
async def test_route():
    return {"message": "Test route works!"}