from . import views
from django.urls import path


urlpatterns = [
    path('',views.demo,name='demo'),
    #path('expression',views.expression,name='expression value')
    #path('contact/',views.contact,name='contact')
]
