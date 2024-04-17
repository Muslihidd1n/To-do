from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class Tasks(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'tasks': Task.objects.filter(user=request.user)
            }
            return render(request, "index.html", context)
        else:
            return redirect('login')

    def post(self, request):
        Task.objects.create(
            user = request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            status=request.POST['status'],
            deadline=request.POST['deadline']
        )
        return redirect('task')


class Edit(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            context = {
                "task": Task.objects.get(id=pk)
            }
            return render(request, "edit.html", context)
        else:
            return redirect('login')


    def post(self, request, pk):
        if Task.objects.get(id=pk).user==request.user:
            Task.objects.filter(id=pk).update(
                tilte=request.POST.get("task-name"),
                description=request.POST.get("task-details"),
                status=request.POST.get("status"),
            )
            return redirect('task')
        else:
            return redirect('logout')


def task_ochir(request, pk):
    if request.user.is_authenticated:
        if Task.objects.get(id=pk).user==request.user:
            Task.objects.get(id=pk).delete()
            return redirect('task')
        else:
            return redirect('login')
    else:
        return redirect('logout')


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request,user)
            return redirect('task')
        return redirect('/')


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
