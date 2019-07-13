from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def activity(request):
    return render(request, 'activity.html')

def forget(request):
    return render(request, 'forget.html')

def person(request):
    return render(request, 'person.html')

def personLeft(request):
    return render(request, 'personLeft.html')

def personNavi(request):
    return render(request, 'personNavi.html')

def personRight(request):
    return render(request, 'personRight.html')


def signin(request):
    if request.session.get('is_login', None):
        return redirect('/home.html')

    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password :
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(user_name=username)
                if user.user_passwd == password:
                    '''
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.user_name
                    '''
                    return redirect('/home.html/')

                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
            return render(request, 'signin.html', {"message": message})
    return render(request, 'signin.html')

def signup(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)

        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.user_name = username
                new_user.user_passwd = password1
                new_user.user_id = id
                new_user.user_telenumb = telenumb
                new_user.save()
                return redirect('/signin.html/')  # 自动跳转到登录页面
    return render(request, 'signup.html', {"message": message})

def vol(request):

    return render(request, 'vol.html')

def worksignin(request):
    return render(request, 'worksignin.html')

def signout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/home.html/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")





