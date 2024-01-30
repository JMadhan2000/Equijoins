from django.db import models

# Create your models here.
  
class dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)


    def __str__(self):
        return self.dname
    

class emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField()
    sal=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE)



class salgrade(models.Model):
    garade=models.IntegerField(primary_key=True)
    lowgrade=models.DecimalField(max_digits=10,decimal_places=2)
    higrade=models.DecimalField(max_digits=10,decimal_places=2)

