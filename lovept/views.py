
# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .import models
from django.utils import timezone
import random


##生成随机邀请码
def generate_verification_code(len=6):
    # 注意： 这里我们生成的是0-9A-Za-z的列表，当然你也可以指定这个list，这里很灵活
    # 比如： code_list = ['P','y','t','h','o','n','T','a','b'] # PythonTab的字母
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # 对应从“A”到“Z”的ASCII码
        code_list.append(chr(i))
    for i in range(97, 123): #对应从“a”到“z”的ASCII码
        code_list.append(chr(i))
    myslice = random.sample(code_list, len)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    return verification_code


#主界面
def home(request):
    return render(request, 'home.html')


#活动界面
def activity(request):
    activities = models.ActVolum.objects.all()
    context = {'lists': activities}
    return render(request, 'activity.html', context)


#忘记密码
def forget(request):
    return render(request, 'forget.html')


#个人信息
def person(request):
    return render(request, 'person.html')


def personLeft(request):
    return render(request, 'personLeft.html')


def personNavi(request):
    return render(request, 'personNavi.html')


def personRight(request):
    uid = request.session['user_id']
    activities = models.ActJoin.objects.filter(user_id=uid)
    context = {'lists': activities}

    '''
    i = 0
    uid=request.session['user_id']
    join_list = models.ActJoin.objects.filter(user_id=uid)
    context = {'activity_list': [], 'v_btime': [], 'v_etime': []}
    for join_i in range(len(join_list)):
        activitys = join_list.join_i.act_numb
        context['activity_list'].append(activitys.act_name)
        context['v_btime'].append(join_list[join_i].v_btime)
        context['v_etime'].append(join_list[join_i].v_etime)
        i = i + 1
    context={'join_i': i}
    '''
    return render(request, 'personRight.html',context)


#登录
def signin(request):
    if request.session.get('is_login', None):
        return redirect('/person.html')

    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.Userinfo.objects.get(user_name=username)
                if user.user_passwd == password:
                    request.session['is_login'] = True
                    request.session['user_name'] = user.user_name
                    request.session['user_id'] = user.user_id
                    request.session['user_telenumb'] = user.user_telenumb
                    request.session['user_tname'] = user.user_tname
                    return render(request, 'home.html')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
            return render(request, 'signin.html', {"message": message})
    return render(request, 'signin.html')


#注册
def signup(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/home.html/")
    if request.method == "POST":
        id = request.POST.get('id', None)
        usertname = request.POST.get('usertname', None)
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        telenumb = request.POST.get('telenumb', None)

        if username and password1:
            username = username.strip()
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'signup.html', {"message": message})
            else:
                same_name_user = models.Userinfo.objects.filter(user_name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'signup.html', {"message": message})

                # 当一切都OK的情况下，创建新用户

                new_user = models.Userinfo.objects.create(user_name=username, user_passwd=password1, user_id=id,
                                                          user_telenumb=telenumb, user_tname=usertname)
                new_user.save()
                return redirect('../signin/')  # 自动跳转到登录页面
    return render(request, 'signup.html')


#活动详情
def vol(request, act_numb):
    ##创建活动列表
    activity = models.ActVolum.objects.get(pk=act_numb)
    request.session['act_num'] = act_numb
    context = {'ActVolum': activity}
    #个人报名处理步骤
    if request.method == "POST":
        ##获取登录状态
        if request.session.get('is_login', None):
           ##获取用户id
            uid = request.session['user_id']
            try:
                idss = str(uid) + str(act_numb)
                new = models.ActJoin.objects.create(id=idss, user_id=uid, v_numb=act_numb, j_btime=timezone.now())
                new.save()
            except:
                return render(request, 'vol.html', context)
           ##没登录时，转到登录页面
        else:
            return render(request, "signin.html")
    return render(request, 'vol.html', context)


#团体报名
def worksignin(request):
   if request.method == 'POST':
      if request.session.get('is_login', None):
          code1 = generate_verification_code(len=6)
          context = {'code': code1}
          cname_r = request.POST.get('cname_r')
          act_numb = request.session['act_num']
          pname = request.POST.get('pname')
          phone = request.POST.get('phone')
          time_now = timezone.now()
          info=models.ComJoin.objects.create(code=code1,cname=cname_r,rea_name=pname,res_telenumb=phone,c_btime=time_now,v_numb=act_numb, counts =1)
          info.save()

          return render( request,'yqmsc.html', context)
      else:
          return render(request, 'signin.html')
   return render(request,'worksignin.html')

  #  else:
   #     message = "请返回主页先登录，再报名！"
    #    return render(request, 'vol.html' , message)
    #return render(request, 'vol.html')

#团体报名成功
def yqmsc(request):
    return render(request, 'yqmsc.html')


#输入邀请码报名
def yqmtx(request):
    if request.method == 'POST':
        if request.session.get('is_login', None):
            coder = request.POST.get('coder')
            context = {'code': coder}

            if models.ComJoin.objects.filter(pk=coder):
                    ainfo = models.ComJoin.objects.get(pk=coder)
                    ainfo.counts += 1
                    act_numb = ainfo.v_numb
                    uid = request.session['user_id']
                    idss = str(uid) + str(act_numb)
                    new = models.ActJoin.objects.create(id=idss, user_id=uid, v_numb=act_numb, j_btime=timezone.now()
                                                        , code=coder)
                    new.save()
                    return render(request, 'yqmsc.html', context)
            else:
                return render(request, 'yqmtx.html')
        else:
            return render(request, 'signin.html')
    return render(request, 'yqmtx.html')






#公益账单
def thing(request):
    return render(request, 'thing.html')


#注销
def signout(request):
    if not request.session.get('is_login', None):
        return redirect('')
    request.session.flush()
    return redirect('../')


