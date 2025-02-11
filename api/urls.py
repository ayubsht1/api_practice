from django.urls import path, include
from .views import ToDoListCreateView, ToDoDetailView 

urlpatterns = [
    path('todos/', ToDoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', ToDoDetailView.as_view(), name='todo-detail'),
]
