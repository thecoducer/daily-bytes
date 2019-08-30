from django.shortcuts import render, redirect
from diary_app.models import Entry
from diary_app.forms import EntryForm

# Create your views here.

def index(request):
    # retrive the data from the database, pass it to the template and loop over that
    entries = Entry.objects.order_by('-date_posted') # to set a definite order
    context = {'entries': entries}
    return render(request, 'diary_app/index.html', context)


def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EntryForm()
        
    context = {'form': form}
    return render(request, 'diary_app/add.html', context)