from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import StudentForm, KitobForm, MuallifForm, RecordForm
from .models import *


# Create your views here.

def sinashga(request):
    return HttpResponse('Hello World')

def bosh_sahifa(request):
    if request.user.is_authenticated:
        return render(request, 'asosiy.html')
    else:
        return redirect('/')

def mashq(request):
    data = {
        'ism':'Xusniddin',
        'names':['Ali', 'Vali']
    }
    return render(request, 'mashq.html')

def hamma_studentlar(request):
    if request.method == 'POST':
        f = StudentForm(request.POST)
        if f.is_valid():
            Student.objects.create(
               ism = f.cleaned_data.get('ism'),
               jins = f.cleaned_data.get('jins'),
               kitob_soni = f.cleaned_data.get('kitob_soni'),
               bitiruvchi = f.cleaned_data.get('bitiruvchi')
            )
        redirect('/students/')
    soz = request.GET.get('q_sozi')
    if soz is None:
        s = Student.objects.all()
    else:
        s = Student.objects.filter(ism__contains = soz)
    data = {
        'list': s,
        'form': StudentForm
    }
    return render(request, 'students.html', data)

def bitiruvchi(request):
    data = {
        'student':Student.objects.filter(bitiruvchi = True)
    }
    return render(request, 'mashq/Bitiruvchi.html', data)

# def kitob(request):
#     data = {
#         'student':Student.objects.filter(kitob_soni__gt = 0)
#     }
#     return render(request, 'mashq/kitob.html', data)

def talaba(request, son):
    data = {
        'student':Student.objects.get(id = son)
    }
    return render(request, 'mashq/student.html', data)

def muallif(request, num):
    data = {
        'muallif':Muallif.objects.get(id = num)
    }
    return render(request, 'mashq/muallif.html', data)

def mualliflar(request):
    if request.method == 'POST':
        form = MuallifForm(request.POST)
        if form.is_valid():
            Muallif.objects.create(
                ism = form.cleaned_data.get('ism'),
                tirik = form.cleaned_data.get('tirik'),
                kitob_soni = form.cleaned_data.get('kitob_soni'),
                tugilgan_yil = form.cleaned_data.get('tugilgan_yil')
            )
        redirect('/mualliflar/')
    soz = request.GET.get('qidirish')
    if soz is None:
        object = Muallif.objects.all()
    else:
        object = Muallif.objects.filter(ism__contains=soz)
    data = {
        'mualliflar': object,
        'form':MuallifForm
    }
    return render(request, 'mashq/mualliflar.html', data)



def kitob(request, num):
    data = {
        'kitob':Kitob.objects.get(id = num)
    }
    return render(request, 'mashq/kitob1.html', data)

def recordlar(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/recordlar/')
    soz = request.GET.get('qidirish')
    if soz is None:
        object = Record.objects.all()
    else:
        object = Record.objects.filter(student__ism__contains=soz)
    data = {
        'kitoblar':Kitob.objects.all(),
        'students':Student.objects.all(),
        'recordlar':object,
        'form':RecordForm
    }
    return render(request, 'mashq/recordlar.html', data)

def tirik_mualliflar(request):
    data = {
        "tirik":Muallif.objects.filter(tirik = True)
    }
    return render(request, 'mashq/tirik.html', data)

def sahifa_max(request):
    data = {
        'kitob':Kitob.objects.order_by('-sahifa')[:3]
    }
    return render(request, 'mashq/sahifak.html', data)

def muallif_kitob3(request):
    data = {
        'muallif':Muallif.objects.order_by('-kitob_soni')
    }
    return render(request, 'mashq/mk3.html', data)

def record_sana(request):
    data = {
        'record':Record.objects.order_by('-olingan_sana')[:3]
    }
    return render(request, 'mashq/recordsana.html', data)

def tirik_muallif_kitoblar(request):
    data = {
        'kitob':Kitob.objects.filter(muallif__tirik = True)
    }
    return render(request, 'mashq/tmk.html', data)

def badiiy(request):
    data = {
        'kitob': Kitob.objects.filter(janr = 'fiction')
    }
    return render(request, 'mashq/badiiy.html', data)

def ism_a(request):
    data = {
        'student':Student.objects.filter(ism__contains = 'a')
    }
    return render(request, 'mashq/ism_a.html', data)

def student_ochir(request, num):
    Student.objects.filter(id = num).delete()
    return redirect('/students/')

def student_tasdiqlash(request, num):
    data = {
        'student':Student.objects.get(id = num)
    }
    return render(request, 'talaba_ochir.html', data)

def kitoblar(request):
    if request.method == 'POST':
        form = KitobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/kitoblar/')
    data = {
        'kitoblar':Kitob.objects.all(),
        'mualliflar':Muallif.objects.all(),
        'form':KitobForm
    }
    return render(request, 'mashq/kitoblar.html', data)

def kitob_ochir(request, num):
    Kitob.objects.filter(id = num).delete()
    return redirect('/kitoblar/')

def yosh3(request):
    data = {
        'muallif':Muallif.objects.order_by('-tugilgan_yil')[:3]
    }
    return render(request, 'mashq/yosh3.html', data)

def kitob10(request):
    data = {
        'kitoblar':Kitob.objects.filter(muallif__kitob_soni__lt = 10)
    }
    return render(request, 'mashq/kitob10.html', data)

def student_erkak(request):
    data = {
        'students':Student.objects.filter(jins = 'Erkak')
    }
    return render(request, 'mashq/erkak.html', data)

def record(request, num):
    data = {
        'record':Record.objects.get(id = num)
    }
    return render(request, 'mashq/record.html', data)

def muallif_ochir(request, num):
    Muallif.objects.filter(id = num).delete()
    return redirect('/mualliflar/')

def record_ochir(request, num):
    Record.objects.filter(id = num).delete()
    return redirect('/recordlar/')

def student_edit(request, num):
    if request.method == 'POST':
        if request.POST.get('bitiruvchi') == 'on':
            natija = True
        else:
            natija = False
        Student.objects.filter(id = num).update(
            ism=request.POST.get('ismi'),
            bitiruvchi=natija,
            kitob_soni=request.POST.get('kitob_soni')
        )
        return redirect('/students/')
    data = {
        'student':Student.objects.get(id = num)
    }
    return render(request, 'student_edit.html', data)

def muallif_edit(request, num):
    if request.method == 'POST':
        if request.POST.get('tirik') == 'on':
            natija = True
        else:
            natija = False
        Muallif.objects.filter(id = num).update(
            ism=request.POST.get('ism'),
            tirik=natija,
            kitob_soni=request.POST.get('kitob_soni')
        )
        return redirect('/mualliflar/')
    data = {
    'muallif':Muallif.objects.get(id = num)
    }
    return render(request, 'muallif_edit.html', data)

def record_edit(request, num):
    if request.method == 'POST':
        if request.POST.get('qaytardi') == 'on':
            natija = True
        else:
            natija = False
        Record.objects.filter(id = num).update(
            qaytardi = natija,
            qaytargan_sana = request.POST.get('qaytargan_sana')
        )
        return redirect('/recordlar/')
    data = {
        'record':Record.objects.get(id = num)
    }
    return render(request, 'record_edit.html', data)

def muallif_tasdiqlash(request, num):
    data = {
        'muallif':Muallif.objects.get(id = num)
    }
    return render(request, 'muallif_ochir.html', data)

def kitob_tasdiqlash(request, num):
    data = {
        'kitob':Kitob.objects.get(id = num)
    }
    return render(request, 'kitob_ochir.html', data)

def record_tasdiqlash(request, num):
    data = {
        'record':Record.objects.get(id = num)
    }
    return render(request, 'record_ochir.html', data)


def loginView(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('login'),
                            password=request.POST.get('parol'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/bs/')
    return render(request, 'login.html')

def logOutView(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username =request.POST.get('login'),
            password =request.POST.get('parol')
        )
        return redirect('/')
    return render(request, 'register.html')









