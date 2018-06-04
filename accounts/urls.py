from django.conf.urls import url
#from . import views
from . import views as accounts_views


urlpatterns = [

    url(r'^signup/$', accounts_views.signup, name='signup'),

]
