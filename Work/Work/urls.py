"""
URL configuration for Work project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from App import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('edit/', views.edit, name='films_edit'),
    path('delete/', views.delete, name='films_delete'),
    path('delete/<int:id>/', views.delete_choose, name='films_delete_choose'),
    path('edit/<int:id>/', views.edit_choose, name='films_edit_choose'),
    #path('')
    # path('delete/', views.delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
