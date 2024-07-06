from django.urls import path
from .import views
urlpatterns = [
     path('', views.home,name='home'),
     # path("form/",views.form_view,name='Form_view'),
     path("edit/<pk>", views.edit, name="edit"),
     path("delete/<pk>", views.delete, name="delete")]