from django.shortcuts import render, redirect
from diary_app.models import Entry
from diary_app.forms import EntryForm
from django.http import HttpResponse, HttpResponseRedirect
# importing generic views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

""" def index(request):
    # retrive the data from the database, pass it to the template and loop over that
    entries = Entry.objects.order_by('-date_posted') # to set a definite order
    count_entries = Entry.objects.all().count()
    context = {'entries': entries, 'count_entries': count_entries}
    return render(request, 'diary_app/home.html', context) """

class EntryListView(ListView):
        model = Entry 
        template_name = 'diary_app/home.html'
        context_object_name = 'entries'
        ordering = ['-date_posted']
        paginate_by = 10

        # Override get_context_data and add any additional querysets to the context.
        def get_context_data(self, **kwargs):
                context = super(EntryListView, self).get_context_data(**kwargs)
                context['count_entries'] = Entry.objects.all().count()
                # Add any other variables to the context here
                ...
                return context


def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            current = Entry.objects.latest('date_posted') # fetching latest entry
            return redirect('readmore', id=current.id)

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
                        return redirect('readmore', id=id)
        else:
                form = EntryForm()
                return render(request,"diary_app/edit.html",{'eform':form,'entry':entry})


def readmore(request, id):
    entry = Entry.objects.get(id=id)
    return render(request, "diary_app/readmore.html", {'entry': entry})


def about(request):
    return render(request, "diary_app/about.html")


def contact(request):
        return render(request, "diary_app/contact.html")


def SignIn(request):
        return render(request, "diary_app/signin.html")

def SignUp(request):
        return render(request, "diary_app/signup.html")