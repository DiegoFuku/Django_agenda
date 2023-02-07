from django.urls import path 
from .views import index,edit,view,create,delete

urlpatterns = [
    path("",index,name="contact"),    
    path("edit/<int:id>",edit,name="contact_edit"),
    path("view/<int:id>",view,name="contact_detail"),
    path("create/",create,name="contact_create"),
    path("delete/<int:id>",delete,name="contact_delete"),


    
]