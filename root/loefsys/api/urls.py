from django.conf import settings
from django.urls import path, include

from rest_framework.schemas import get_schema_view

app_name = "loefsys"

urlpatterns = [
    path("admin/", include("loefsys.api.admin.urls", namespace="admin")),
    path("", include("events.api.urls")),
    # path(
    #     "schema",
    #     get_schema_view(
    #         title="LoefAPI",
    #         version=1,
    #         url="/api/",
    #         urlconf="thaliawebsite.api.urls",
    #         generator_class=OAuthSchemaGenerator,
    #         public=True,
    #     ),
    #     name="schema",
    # ),
]
