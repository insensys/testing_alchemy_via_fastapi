from starlette_admin.contrib.sqla import ModelView


class SubscriptionView(ModelView):
    form_include_pk = True