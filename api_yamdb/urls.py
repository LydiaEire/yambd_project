from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(
   openapi.Info(
      title="Yamdb API",
      default_version='v1',
      description="Документация для приложения проекта Yamdb",
      contact=openapi.Contact(email="admin@yamdb.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('redoc/', TemplateView.as_view(template_name='redoc.html'),
         name='redoc'),
    path('api/', include('title_api.urls')),
    path('api/', include('users_api.urls')),
]

urlpatterns += [
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]
