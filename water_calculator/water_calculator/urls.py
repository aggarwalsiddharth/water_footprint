"""footprint_calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main.views import home_view,question_view,result_view,ChartData

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home_view ,name='home'),
    path('question/<int:id>',question_view, name='question'),
    path('result/',result_view, name='result'),
    path('api/data/',ChartData.as_view(),name ='api-data')


]
