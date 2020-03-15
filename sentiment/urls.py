from . import views
from django.conf.urls import url

app_name = 'sentiment'

urlpatterns = [
    url(r'^result',views.result,name='result'),
]