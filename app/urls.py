"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
import todo.views as views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)
router.register(r'todosanother', views.TodoAnotherViewSet)
router.register(r'todosyetanother', views.TodoYetAnotherViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Api Description",
    ),
    public=True,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
]
urlpatterns += router.urls
