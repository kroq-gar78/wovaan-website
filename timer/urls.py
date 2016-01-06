from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.timer_view),
    url(r'^(puzzle/(?P<puzzle>[-\w0-9]+))?/?$', views.timer_view),
    url(r'^updatescramble/?$', views.give_new_scramble),
    url(r'^addsolve/?$', views.add_solve),
    url(r'^gettimes/?$', views.give_time_list),
]
