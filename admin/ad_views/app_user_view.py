from starlette_admin.contrib.sqla import ModelView
from starlette_admin import StringField, EmailField, PasswordField


class AppUserView(ModelView):
    form_include_pk=True
    name="AppUser"
    
    fields=[
        StringField("user_inn", label="Инн пользователя"),
        EmailField("email", label="Почто пользователя"),
        PasswordField("password", label="Пароль"),
        StringField("user_name", label="Имя пользователя")
    ]

    exclude_fields_from_list=[
        "created_at"
    ]


# class AppUserView(ModelView):
#     form_include_pk = True
#     name = "App User"
#     name_plural = "App Users"
#     icon = "fa fa-users"

#     fields = [
#         StringField("user_inn", label="ИНН пользователя"),
#         StringField("login_gns", label="Логин ГНС"),
#         StringField("password_app", label="Пароль приложения"),
#         StringField("user_name", label="Имя пользователя"),
#         StringField("theme", label="Тема"),
#         StringField("language", label="Язык"),
#         StringField("infocom_token", label="Токен Инфоком"),
#         DateTimeField("infocom_token_start_date", label="Дата начала токена Инфоком"),
#         DateTimeField("infocom_token_end_date", label="Дата окончания токена Инфоком"),
#         StringField("email", label="Email"),
#         StringField("tel_number", label="Номер телефона"),
#         DateTimeField("created_at", label="Дата создания"),
#         BooleanField("is_admin", label="Администратор"),
#         StringField("refresh_token", label="Токен обновления"),
#         BooleanField("is_active", label="Активен"),
#         DateTimeField("delete_at", label="Дата удаления"),
#     ]

#     searchable_fields = [
#         "user_tin",
#         "login_gns", 
#         "user_name",
#         "email",
#         "tel_number",
#     ]

#     sortable_fields = [
#         "user_tin",
#         "user_name",
#         "email",
#         "created_at",
#         "is_admin",
#         "is_active",
#     ]

#     exclude_fields_from_list = [
#         "password_app",
#         "infocom_token",
#         "refresh_token",
#     ]

#     exclude_fields_from_create = [
#         "created_at",
#         "delete_at",
#     ]

#     exclude_fields_from_edit = [
#         "created_at",
#     ]
