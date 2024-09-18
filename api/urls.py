from django.urls import path
from .views import getUsers, getUser, createUser, updateUser, deleteUser


urlpatterns = [
    path('users/', getUsers, name="getUsers"),
    path('users/create', createUser, name="createUser"),
    path('users/<int:pk>/', getUser, name="getUser"),
    path('users/<int:pk>/update', updateUser, name="updateUser"),
    path('users/<int:pk>/delete', deleteUser, name="deleteUser"),
]