from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view,name='index-page'),
    path('contact/', contact_view, name='contact-page'),
    path('service/',services_view,name='service-page'),
    path('about/',about_view,name='about-page'),
    path('price/',testimonial_view,name='test-page'),
    path('price/',works_view,name='work-page'),

]
    