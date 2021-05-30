from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses/new', views.new),
    path('courses/<int:course_id>/confirm', views.confirm),
    path('courses/<int:course_id>/destroy', views.destroy),
    path('reset', views.reset),
]
