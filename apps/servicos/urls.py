from django.urls import path
from servicos.views import index

urlpatterns = [
    path('', index)
]
