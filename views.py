from django.db.models import Q
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
from datetime import datetime, timedelta, time
import random
# Create your views here.

def Index(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'index.html', d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('index')
    today = datetime.now().date()
    yesterday = today - timedelta(1)
    lasts = today - timedelta(7)

    tv = Visitor.objects.filter(vdate=today).count()
    yv = Visitor.objects.filter(vdate=yesterday).count()
    ls = Visitor.objects.filter(vdate__gte=lasts,vdate__lte=today).count()
    totalv = Visitor.objects.all().count()

    d = {'tv':tv,'yv':yv,'ls':ls,'totalv':totalv}
    return render(request,'admin_home.html',d)


def Logout(request):
    logout(request)
    return redirect('index')


def manage_newvisitors(request):
    if not request.user.is_authenticated:
        return redirect('index')
    visitor = Visitor.objects.all()
    d = {'visitor':visitor}
    return render(request, 'manage_newvisitors.html', d)


def visitor_form(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    if request.method=="POST":
        vn = request.POST['visname']
        mn = request.POST['mobilenumber']
        addr = request.POST['address']
        apt = request.POST['apartment']
        flr = request.POST['floor']
        wtm = request.POST['whomtomeet']
        rtm = request.POST['reasontomeet']
        intime = request.POST['intime']
        try:
            Visitor.objects.create(visitorname=vn,mobileno=mn,address=addr,apartment=apt,floor=flr,whomtomeet=wtm,reasontomeet=rtm,intime=intime,vdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'visitor_form.html', d)


def visitor_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    visitor = Visitor.objects.get(id=pid)
    if request.method == 'POST':
        rm = request.POST['remark']
        ot = request.POST['outtime']
        try:
            visitor.remark = rm
            visitor.outtime = ot
            visitor.save()
            error = "no"
        except:
            error = "yes"
    d = {'visitor': visitor,'error':error}
    return render(request,'visitor_detail.html', d)


def betweendate_reportdetails(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'betweendate_reportdetails.html')



def betweendate_report(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        fd = request.POST['fromdate']
        td = request.POST['todate']
        visitor = Visitor.objects.filter(Q(vdate__gte=fd) & Q(vdate__lte=td))
        visitorcount = Visitor.objects.filter(Q(vdate__gte=fd) & Q(vdate__lte=td)).count()
        d = {'visitor': visitor,'fd':fd,'td':td,'visitorcount':visitorcount}
        return render(request, 'betweendate_reportdetails.html', d)
    return render(request, 'betweendate_report.html')


def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    if request.method == "POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'changepassword.html',d)


def search(request):
    q = request.GET.get('searchdata')

    try:
        visitor = Visitor.objects.filter(Q(visitorname=q) | Q(mobileno=q))
        visitorcount = Visitor.objects.filter(Q(visitorname=q) | Q(mobileno=q)).count()

    except:
        visitor = ""
    d = {'visitor': visitor,'q':q,'visitorcount':visitorcount}
    return render(request, 'search.html',d)
