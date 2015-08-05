from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.timer_view),
    url(r'^/?updatescramble/?$', views.give_new_scramble),
]
