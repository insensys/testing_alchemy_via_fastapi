from fastapi import Request
from starlette_admin.auth import AuthProvider, AdminUser
from starlette_admin.exceptions import FormValidationError, LoginFailed


class SimpleAuthProvider(AuthProvider):
    async def is_authenticated(self, request: Request):
        return request.session.get("username") is not None
    
    async def login(self, username, password, remember_me, request, response):
        errors = ()
        if not username:
            errors["username"] = "Bведите имя пользователя"
        if not password:
            errors["password"] = "Введите пароль"
        if errors:
            raise FormValidationError(errors)
        
        if username =="admin" and password == "admin":
            request.session.update({"username": username})
            return response
        
        raise LoginFailed("Неверный логин пароль")
    
    async def logout(self, request, response):
        request.session.clear()
        return response
    
    def get_admin_user(self, request: Request):
        username = request.session.get("username")
        if username:
            return AdminUser(username=username)
        return None