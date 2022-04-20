"""event_handling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from events.viewsets.viewsets import EventUpdateGenericView
from events.viewsets.viewsets import EventsListGenericView
from events.viewsets.viewsets import EventsCreateGenericView
from events.viewsets.viewsets import EventDeleteGenericView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',include(router.urls)),

    # API For JWT Token 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API For Events
    path('event/list', EventsListGenericView.as_view()),
    path('event/create', EventsCreateGenericView.as_view()),
    path('event/update/<event_id>', EventUpdateGenericView.as_view()),
    path('event/delete/<event_id>', EventDeleteGenericView.as_view())

]