from django.contrib import admin
from django.urls import path, include
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/', views.index1),
    path('index2/', views.index2),
    path('firstapp/', include('firstapp.urls')),
]