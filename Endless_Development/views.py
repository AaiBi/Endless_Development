from django.shortcuts import render, redirect
from blog.models import Blog, Logo
from service.models import Service
from templates.forms import MessageForm


def home(request, template='home.html'):
    context = {
        'pictures': Logo.objects.all(),
        'posts': Blog.objects.all(),
        'services': Service.objects.all()
    }
    return render(request, template, context)


def send_message(request):
    if request.method == 'GET':
        return render(request, 'home.html', {'form': MessageForm()})
    else:
        try:
            form = MessageForm(request.POST)
            new_message = form.save(commit=False)
            new_message.save()
            return redirect('home')
        except ValueError:
            return render(request, 'todo/create_todos.html', {'form': MessageForm(), 'error': 'Bad data passed in'})