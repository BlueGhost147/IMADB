from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1'
    ),
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('country/options', views.country_option_list),
    path('movie/list', views.movies_list),
    path('movie/create', views.movie_form_create),
    path('movie/<int:pk>/get', views.movie_form_get),
    path('movie/<int:pk>/update', views.movie_form_update),
    path('movie/<int:pk>/delete', views.movie_delete),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
