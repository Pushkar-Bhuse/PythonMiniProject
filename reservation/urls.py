from django.conf.urls import url
from django.conf import settings
from django.urls import path, include
from reservation.views import choose_and_book,choose_location

urlpatterns = [
    url(r'(?P<place>\d+)/$', choose_and_book, name='book'),
    path('choose/', choose_location, name='choose'),
    # url(r'confirmation/$', reservations, name='reservation'),
]
