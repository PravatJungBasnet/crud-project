from django.shortcuts import render,HttpResponseRedirect
from .forms import student
from .models import user

def register(request):
    if request.method=='POST':
        fm=student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            db=user(name=nm,email=em,password=pw)
            db.save()
            fm=student()
            


    else:
        fm=student()
    stud=user.objects.all()  
    return render(request,'enroll/save.html',{'form':fm,'stu':stud})

# delet
def delet(request,id):
    if request.method=="POST":
        pi=user.objects.get(pk=id)
        pi.delete()
        fm=student()
    return HttpResponseRedirect('/')   
# update or edit
def update(request,id):
    if request.method=="POST":
        pi=user.objects.get(pk=id)
        fm=student(request.POST,instance='pi')
        if fm.is_valid():
           fm.save()

    else:
       pi=user.objects.get(pk=id)
       fm=student(pi=id)  
    return render(request,'enroll/update.html',{'form':fm}) 
        
