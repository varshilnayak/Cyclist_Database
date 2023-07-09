"""cyclist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('', views.showemp, name="showemp"),
    path('insert_form', views.insert_form, name="insert_form"),
    path('insertemp', views.insertemp, name="insertemp"),
    path('editemp/<int:cyclist_id>', views.editemp, name="editemp"),
    path('update/<int:cyclist_id>', views.updateemp, name="updateemp"),
    path('delemp/<int:cyclist_id>', views.delemp, name="delemp"),
    path('showcyclist', views.showcyclist, name="showcyclist"),
    path('showorganizer', views.showorganizer, name="showorganizer"),
    path('insert_organizer', views.insert_organizer, name="insert_organizer"),
    path('organizer_temp', views.organizer_temp, name="organizer_temp"),
    path('organizer_editemp/<int:organizer_id>',
         views.organizer_editemp, name="organizer_editemp"),
    path('organizer_updateemp/<int:organizer_id>',
         views.organizer_updateemp, name="organizer_updateemp"),
    path('organizer_delemp/<int:organizer_id>',
         views.organizer_delemp, name="organizer_delemp"),
    path('showevent', views.showevent, name="showevent"),
    path('event_temp', views.event_temp, name="event_temp"),
    path('insert_event', views.insert_event, name="insert_event"),
    path('showsponsor', views.showsponsor, name="showsponsor"),
    path('event_editemp/<int:event_id>',
         views.event_editemp, name="event_editemp"),
    path('event_updateemp/<int:event_id>',
         views.event_updateemp, name="event_updateemp"),
    path('event_delemp/<int:event_id>', views.event_delemp, name="event_delemp"),
    path('sortCyclist', views.sortCyclist, name="sortCyclist"),
    path('sortOrganizer', views.sortOrganizer, name="sortOgranizer"),
    path('sortevent', views.sortevent, name="sortevent"),
    path('custom_query', views.custom_query, name="custom_query"),
    path('run_query', views.run_query, name="run_query"),



]
