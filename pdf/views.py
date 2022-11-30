from django.shortcuts import render
from .models import Profile

from django.http import HttpResponse
from django.template import loader
import pdfkit                              #pip install pdfkit
import io                                  #it is needed if you want to send the information from form to the database and database to the form
# Create your views here.

def accept(request):
    if request.method=="POST":  #if it is a post then take all the information from the user and post it to the database.
        name=request.POST.get("name","")# 1>whatever the request you get, you post it to the database after getting it from the user(....)
                                        #2>you get information (....) from the user and post to database -->
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        school=request.POST.get("school","")
        degree=request.POST.get("degree","")
        university=request.POST.get("university","")
        skill=request.POST.get("skill","")
        about_you=request.POST.get("about_you","")
        previous_work=request.POST.get("previous_work","")
        
                                                                        
        profile = Profile(name=name,phone=phone,        #inorder to pass all above variable ,we create the obj of the class       
                          email=email,degree=degree,
                          university=university,skill=skill,
                          about_you=about_you,
                          previous_work=previous_work,school=school) 
        profile.save()
        
    return render(request,'accept.html')


def resume(request, id):
    user_profile=Profile.objects.get(pk=id) #accesing table
    template = loader.get_template('resume.html')
    html = template.render({'user_profile':user_profile})
    option={
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf = pdfkit.from_string(html,False,option)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    
    return response

def list(request):
    profile=Profile.objects.all()
    return render(request,'list.html',{'profile':profile})
    
