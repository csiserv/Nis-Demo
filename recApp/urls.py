from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task-list'),            # root URL
    path('recApp/', views.task_list, name='task-list-alt'), # this will also work at /recApp
]
