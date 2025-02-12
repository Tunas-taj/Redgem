from django.shortcuts import render, redirect
from Survey.models import register
# Create your views here
def index(request):
    return render(request, 'index.html')

def congratulations(request):
    return render(request, 'congratulations.html')

def data_saved(request):
    registers =  register.objects.all()
    if request.method == 'POST':
        rating = request.POST.get('rating')
        print(rating)
        if rating is None:
            return redirect('/')
        try:
            rating = int(rating)
        except ValueError:
            return redirect('/')

        if 1 <= rating <= 10:
            Register = register.objects.create(note=rating)
            print(Register.date)

        return redirect('congratulations') 
    return render(request, 'data_saved.html', {
        'registers':registers
    })