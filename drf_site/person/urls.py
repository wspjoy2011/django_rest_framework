from django.urls import path, include
from rest_framework import routers

from .views import *

# router = routers.DefaultRouter()
# router.register(r'person', PersonViewSet)
# print(router.urls)

urlpatterns = [
    path('api/v1/person/', PersonAPIList.as_view()),
    path('api/v1/person/<int:pk>/', PersonAPIUpdate.as_view()),
    path('api/v1/person_delete/<int:pk>/', PersonAPIDestroy.as_view())
]
