from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', Tasks.as_view(),name ='task'),
    path('', LoginView.as_view(),name ='login'),
    path('logout/', LogoutView.as_view(),name ='logout'),


    path('edit/<int:pk>/', Edit.as_view(),name ='edit'),



    path('task_ochir/<int:pk>/', task_ochir),

]
