from starlette_admin.contrib.sqla import ModelView

class OrganizationSubscriptionView(ModelView):
    form_include_pk = True