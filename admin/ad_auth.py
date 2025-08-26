from starlette_admin.auth import AuthProvider, AdminUser


class SimpleAuthProvider(AuthProvider):
    async def login(self, username:str, password:str) -> AdminUser:
        if username =="admin" and password == "admin123": #TODO: пока оставлю так. Потом как заработает сделать через БД
            return AdminUser(username=username)
        return None
