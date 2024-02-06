from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies
from .forms import MovieForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='user_login')
def index(request):
    obj = Movies.objects.all()
    context = {
        "obj":obj
    }
    return render(request,"index.html",context)

def ninestar(request):
    high_rated_movies = Movies.objects.filter(rating=9)
    context = {
        "rating":high_rated_movies
    }
    return render(request,"high_rated_movies.html",context)


@login_required(login_url='user_login')
def add_movie(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'add_movie.html', {'form': form})