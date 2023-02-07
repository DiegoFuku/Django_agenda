from django.urls import path 
from .views import index,create,view,edit,delete


urlpatterns = [
    path('',index, name='todo'),
    path('create/',create, name='todo_create'),
    path('view/<int:id>',view, name='todo_view'),
    path('edit/<int:id>',edit, name='todo_edit'),
    path('delete/<int:id>',delete, name='todo_delete'),
    



]