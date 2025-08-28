from starlette_admin.contrib.sqla import ModelView


class OrganizationView(ModelView):
    form_include_pk = True