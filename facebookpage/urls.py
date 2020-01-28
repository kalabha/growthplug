from django.urls import path

from facebookpage import views

app_space = 'facebook_page'

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.get_page, name='get_page'),
    path('update/', views.update_page, name='update_page')
]
