from django.shortcuts import render

# Create your views here.
from app.models import *

def EQUIJOINS(request):
    Equijoins=emp.objects.select_related('deptno').all()
    Equijoins=emp.objects.select_related('deptno').filter(deptno=20)
    Equijoins=emp.objects.select_related('deptno').filter(deptno__dloc='CHICAGO')
    Equijoins=emp.objects.select_related('deptno').filter(hiredate__year=2024)
    Equijoins=emp.objects.select_related('deptno').filter(sal__gte=2500)
    Equijoins=emp.objects.select_related('deptno').filter(hiredate__month=1)
    Equijoins=emp.objects.select_related('deptno').filter(mgr__isnull=True)
    Equijoins=emp.objects.select_related('deptno').filter(comm__isnull=False)
    Equijoins=emp.objects.select_related('deptno').filter(comm__isnull=True)
    d={'Equijoins':Equijoins}
    return render(request,'EQUIJOINS.html',d)