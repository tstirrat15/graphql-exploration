from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lists import views

router = DefaultRouter()
router.register('clients', views.ClientViewset)
router.register('items', views.ItemViewset)
router.register('sources', views.SourceViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
