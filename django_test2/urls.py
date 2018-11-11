"""djang_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from API_own import views
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.post_json, name='index'),
    # path('test_api/1/<node_name1>/', views.post_Select, name='api1'),
    # path('test_api/2/<node_name>/<node_time>/', views.post_Nodeson, name='api2'),
    # path('test_api/3/', views.get_json, name='api3'),
    path('test_api/2/<str_name>/', views.get_json, name='json1'),
    path('test_api/1/', views.total_getJson, name='json2'),
]

