from fastapi import Request
from starlette_admin.auth import AuthProvider, AdminUser
from starlette_admin.exceptions import FormValidationError, LoginFailed
from starlette.requests import Request
from sqlalchemy import select, or_
from models_folder.app_user import AppUser
from config.sync_db_config import SessionLocal
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError


hasher = PasswordHasher()

class SimpleAuthProvider(AuthProvider):
    async def is_authenticated(self, request: Request):
        return request.session.get("username") is not None
    
    async def login(self, username, password, remember_me, request:Request, response):
        errors = {}
        if not username:
            errors["username"] = "Bведите имя пользователя"
        if not password:
            errors["password"] = "Введите пароль"
        if errors:
            raise FormValidationError(errors)
        
        query = (
            select(AppUser)
            .where(
                or_(
                    AppUser.user_inn == username,
                    AppUser.user_name == username,
                    AppUser.email == username,
                )
            )
        )

        with SessionLocal() as db:
            user = db.execute(query).scalars().one_or_none()

        if user is None:
            raise LoginFailed("Пользователь не найден")

        try:
            hasher.verify((user.password or ""), (password or ""))
        except VerifyMismatchError:
            raise LoginFailed("Неверный пароль")        

        request.session["username"] = user.user_name or user.email
        return response
    
    async def logout(self, request: Request, response):
        request.session.clear()
        return response
    
    def get_admin_user(self, request: Request):
        username = request.session.get("username")
        if username:
            return AdminUser(username=username)
        return None