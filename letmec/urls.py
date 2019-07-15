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
    # 主路径
    path('admin/', admin.site.urls),  # 管理
    path('', lovept_views.home, name='home'),  # lovept 主界面

    # 活动
    path('activity/', lovept_views.activity, name='activity'),
    path('vol/<int:act_numb>', lovept_views.vol,name='vol'),
    ###

    # 个人信息
    path('person/', lovept_views.person, name='person'),
    path('personLeft/', lovept_views.personLeft, name='personLeft'),
    path('personNavi/', lovept_views.personNavi, name='personNavi'),
    path('personRight/', lovept_views.personRight, name='personRight'),

    #登录注册注销
    path('signup/', lovept_views.signup, name='signup'),#注册
    path('signin/', lovept_views.signin, name='signin'),#登陆
    path('signout/', lovept_views.signout, name='signout'),#注销
    path('forget/', lovept_views.forget, name='forget'),  # 忘记密码

    #报名
    path('worksignin/', lovept_views.worksignin, name='worksignin'),    #公司报名
    path('yqmsc/', lovept_views.yqmsc, name='yqmsc'),        #公司报名成功
    path('yqmtx/', lovept_views.yqmtx, name='yqmtx'),        #公司报名

    # 公益账单
    path('thing/', lovept_views.thing, name='thing'),


]
