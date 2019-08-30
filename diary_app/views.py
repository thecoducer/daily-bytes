from django.shortcuts import render, redirect
from diary_app.models import Entry
from diary_app.forms import EntryForm

# Create your views here.

def index(request):
    # retrive the data from the database, pass it to the template and loop over that
    entries = Entry.objects.order_by('-date_posted') # to set a definite order
    count_entries = Entry.objects.all().count()
    context = {'entries': entries, 'count_entries': count_entries}
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


def delete(request, id):
        entry = Entry.objects.get(id=id)
        entry.delete()
        return redirect('home')

def edit(request,id):
        entry = Entry.objects.get(id=id)
        if request.method=="POST":
                form = EntryForm(request.POST, instance = entry)
                if form.is_valid():
                        form.save()
                        return redirect('home')
        else:
                form = EntryForm()
                return render(request,"diary_app/edit.html",{'eform':form,'entry':entry})


def about(request):
    return render(request, "diary_app/about.html")


def readmore(request, id):
    entry = Entry.objects.get(id=id)
    return render(request, "diary_app/readmore.html", {'entry': entry})
