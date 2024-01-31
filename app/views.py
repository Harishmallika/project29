from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from app.forms import *

def create_school(request):
    ESFO=schoolForm()
    d={'ESFO':ESFO}
    
    if request.method=='POST':
        SFDO=schoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['sname']
            sl=SFDO.cleaned_data['sloction']
            sp=SFDO.cleaned_data['sprincipal']
            e=SFDO.cleaned_data['email']
            re=SFDO.cleaned_data['renteremail']
            SO=school.objects.get_or_create(sname=sn,slocation=sl,sprincipal=sp,email=e,renteremail=re)[0]
            SO.save()
            return HttpResponse('school Date is inserted')
        else:
            return HttpResponse('inavlid data')
    return render(request,'create_school.html',d) 




















    #def htmlforms(request):
    #if request.method=='POST':
     #   username=request.POST['un']
      #  return HttpResponse(username)
   # return render(request,'htmlforms.html')   
