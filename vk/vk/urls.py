from django.contrib import admin
from django.urls import path
from student.views import home,studentlist,courselist,register,enrolledStudents,projectReg
urlpatterns = [
path('secretadmin/', admin.site.urls),
path('',home),
path('home/',home),
path('studentlist/',studentlist),
path('courselist/',courselist),
path('register/',register),
path('enrolledlist/',enrolledStudents),
path('projectReg/',projectReg),
]
 