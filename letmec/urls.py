"""letmec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# coding:utf-8
from django.contrib import admin
from django.urls import path
from lovept import views as lovept_views


urlpatterns = [

    path('activity.html/', lovept_views.activity, name='activity'),
    path('forget.html/', lovept_views.forget, name='forget'),
    path('person.html/', lovept_views.person, name='person'),
    path('person.html/personLeft.html/', lovept_views.personLeft, name='personLeft'),
    path('person.html/personNavi.html/', lovept_views.personNavi, name='personNavi'),
    path('person.html/personRight.html/', lovept_views.personRight, name='personRight'),
    path('signup.html/', lovept_views.signup, name='signup'),#注册
    path('signin.html/', lovept_views.signin, name='signin'),#登陆
    path('vol.html/', lovept_views.vol, name='vol'),
    path('home.html', lovept_views.home, name='home'),#主页
    path('', lovept_views.home, name='home'),
    #网页url
    path('activity.html/vol.html', lovept_views.vol, name='vol'),
    path('vol.html/worksignin.html', lovept_views.worksignin, name='vworksignin'),
    path('admin/', admin.site.urls),
]
