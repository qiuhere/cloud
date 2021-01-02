from django.conf.urls import url
from user import views
urlpatterns = [
    url(r'^$',views.index_view),
    url(r'^upload/$',views.upload_view),
    url(r'^showall/$',views.showall_view)
]