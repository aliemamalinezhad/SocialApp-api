"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from graphene_django.views import GraphQLView
# from post.schema import schema

schema_view = get_schema_view(
    openapi.Info(
        title="Social App API",
        default_version='v1',
        description="Welcome",
        terms_of_service="https://www.socailappapi.org",
        contact=openapi.Contact(email="aliemamalinezhad@gmail.com"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

v1_urlpatterns =[
    path('post/', include('post.api.urls', namespace='post')),
]


urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'), 
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'), 

    path('admin/', admin.site.urls),
    # path('api/v1/post/', include('post.urls', namespace="post")),
    path('api/v1/', include(v1_urlpatterns)),



    # path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),



]
