"""GCT_V01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from tifert import views
################################################
from django.conf import settings
from django.conf.urls.static import static
###########################################
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
################################################

urlpatterns = [

##############################################################
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),



###############################################################
    path('', views.home, name='home'),
    ###################################
    # ex: /tifert/
    path('tabia/', views.index_tabia, name='index_tabia'),
    # ex: /tifert/5/
    re_path(r'^new_tabia/$', views.NewPostView.as_view(), name='new_tabia'),
    # ex: /tifert/5/
    re_path(r'^tabia/table/(?P<pk>\d+)/$', views.table_tabia, name='table_tabia'),
    re_path(r'^tabia/table/(?P<pk>\d+)/edit/$',views.DefUpdateView.as_view(), name='edit_tabia'),

    # ex: /tifert/5/results/
    ###################################
    # ex: /rapport/
    path('rj/', views.index_rj, name='index_rj'),
    re_path(r'^new_rj/$', views.NewRjView.as_view(), name='new_rj'),
    # ex: /tifert/5/
    re_path(r'^rj/table/(?P<pk>\d+)/$', views.table_rj, name='table_rj'),
    re_path(r'^rj/table/(?P<pk>\d+)/edit/$',views.RjUpdateView.as_view(), name='edit_rj'),


    ##########################################################

    path('upload/', views.image_upload, name='upload'),
    path('photo_list/', views.photo_list, name='photo_list'),
    #############################################################

    path('calcule/', views.calcule, name='calcule'),
########################################################
    re_path(r'^search/$', views.search, name='search'),
    re_path(r'^def_search/$', views.def_search, name='def_search'),
    re_path(r'^Rj_search/$', views.Rj_search, name='Rj_search'),
    ############################################################
    #                    PDF CREATION
    ############################################################
    path('pdf/', views.some_view, name='pdf'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
