"""applicationRouting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from application.views import home, loginUser, createApplication, mainpage, allApplication
from application.views import signup, logoutUser, members, applicationDetail, googleSignup
from application.views import editProfile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage),
    url(r'^signup', signup),
    url(r'^login', loginUser),
    url(r'^dashboard', home),
    url(r'^createApplication', createApplication),
    url(r'^allapplication', allApplication),
    url(r'^logout', logoutUser),
    url(r'^members', members),
    url(r'^applicationDetail/(?P<appId>\w+)$', applicationDetail),
    url(r'^googlesignup', googleSignup),
    url(r'^editProfile', editProfile),

]
