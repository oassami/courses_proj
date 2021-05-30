from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

def index(request):
    context={
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    errors = Course.objects.addCourseValidation(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        request.session['name']= request.POST['c_name']
        request.session['description']= request.POST['c_desc']
        return redirect('/')
    Course.objects.create(name=request.POST['c_name'], description=request.POST['c_desc'])
    request.session.clear()
    return redirect('/')

def confirm(request, course_id):
    context={
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'confirm.html', context)

def destroy(request, course_id):
    del_course=Course.objects.get(id=course_id)
    del_course.delete()
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')