from django.shortcuts import render, redirect
from diary_app.models import Entry
from diary_app.forms import EntryForm, UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
    entries = Entry.objects.filter(author=request.user)
    context = {'entries': entries, 'count_entries': count_entries}
    return render(request, 'diary_app/home.html', context) """


class EntryListView(ListView):
        model = Entry 
        template_name = 'diary_app/home.html'
        context_object_name = 'entries'
        ordering = ['-date_posted']
        paginate_by = 10

        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
                return super().dispatch(*args, **kwargs)

        # Override get_context_data and add any additional querysets to the context.
        def get_context_data(self, **kwargs):
                context = super(EntryListView, self).get_context_data(**kwargs)
                context['count_entries'] = Entry.objects.all().count()
                # Add any other variables to the context here
                ...
                return context

        """ def get_queryset(request):
                queryset = Entry.objects.filter(author=request.user)
                return queryset """


@login_required
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.save()
            current = Entry.objects.latest('date_posted') # fetching latest entry
            return redirect('readmore', id=current.id)

    else:
        form = EntryForm()
        
    context = {'form': form}
    return render(request, 'diary_app/add.html', context)


@login_required
def delete(request, id):
        #entry = Entry.objects.get(id=id)
        entry = get_object_or_404(Entry, id=id)
        entry.delete()
        return redirect('home')


@login_required
def edit(request,id):
        #entry = Entry.objects.get(id=id)
        entry = get_object_or_404(Entry, id=id)
        if request.method == "POST":
                form = EntryForm(request.POST, instance = entry)
                if form.is_valid():
                        form.save()
                        return redirect('readmore', id=id)
        else:
                form = EntryForm()
                return render(request,"diary_app/edit.html",{'eform':form,'entry':entry})


@login_required
def readmore(request, id):
    #entry = Entry.objects.get(id=id)
    entry = get_object_or_404(Entry, id=id)
    return render(request, "diary_app/readmore.html", {'entry': entry})


def about(request):
    return render(request, "diary_app/about.html")


@login_required
def contact(request):
        return render(request, "diary_app/contact.html")


def SignUp(request):
        if request.method == "POST":
                form = UserForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect("/signin/")
        else:
                form = UserForm()
        return render(request, "users/signup.html", {'form': form})


""" def SignIn(request):
        return render(request, "diary_app/signin.html") """


""" def SignIn_validate(request):
        next_page = request.GET['next']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user) #logs in the user
                return HttpResponseRedirect(next_page)
        else:
                return redirect('signin') """


@login_required
def SignOut(request):
        logout(request)
        return redirect('signin')


def ForgetPassword(request):
        return render(request, "diary_app/forgetpassword.html")