from django.contrib import admin
from django.urls import path

from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sinashga/', sinashga),
    path('bs/', bosh_sahifa),
    path('mashq/', mashq),
    path('students/', hamma_studentlar),
    path('bitiruvchi/', bitiruvchi),
    path('talaba/<int:son>/', talaba),
    path('muallif/<int:num>/', muallif),
    path('mualliflar/', mualliflar),
    path('kitoblar/', kitoblar),
    path('kitob/<int:num>/', kitob),
    path('recordlar/', recordlar),
    path('tirik/', tirik_mualliflar),
    path('sahifak/', sahifa_max),
    path('mk3/', muallif_kitob3),
    path('recordsana/', record_sana),
    path('tmk/', tirik_muallif_kitoblar),
    path('badiiy/', badiiy),
    path('student_ochir/<int:num>/', student_ochir),
    path('kitob_ochir/<int:num>/', kitob_ochir),
    path('isma/', ism_a),
    path('yosh3/', yosh3),
    path('kitob10/',kitob10),
    path('erkak/', student_erkak),
    path('record/<int:num>/', record),
    path('muallif_ochir/<int:num>/', muallif_ochir),
    path('record_ochir/<int:num>/', record_ochir),
    path('student_edit/<int:num>/', student_edit),
    path('muallif_edit/<int:num>/', muallif_edit),
    path('record_edit/<int:num>/', record_edit),
    path('student_tasdiqlash/<int:num>/', student_tasdiqlash),
    path('muallif_tasdiqlash/<int:num>/', muallif_tasdiqlash),
    path('kitob_tasdiqlash/<int:num>/', kitob_tasdiqlash),
    path('record_tasdiqlash/<int:num>/', record_tasdiqlash),
    path('', loginView),
    path('logout/', logOutView),
    path('register/', register),



]









































