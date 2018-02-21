import todo.views as views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo/p', views.PViewSet)
router.register(r'todo/a', views.AViewSet)
router.register(r'todo/c', views.CViewSet)
router.register(r'todo/chu', views.ChuViewSet)
router.register(r'todo/t', views.TViewSet)
router.register(r'todo/co', views.CoViewSet)
router.register(r'todo/tf', views.TfViewSet)
urlpatterns = [
]

urlpatterns += router.urls
