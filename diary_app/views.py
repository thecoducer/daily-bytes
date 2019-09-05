from django.shortcuts import render, redirect
from diary_app.models import Entry
from diary_app.forms import EntryForm, UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
# importing generic views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

@login_required
def home(request):
    entries = Entry.objects.filter(author=request.user, trash=False)
    count_entries = entries.count()
    entries = entries.order_by('-date_posted')
    paginator = Paginator(entries, 5)   
    page = request.GET.get('page') 
    entries = paginator.get_page(page)
    context = {'entries': entries, 'count_entries': count_entries}
    return render(request, 'diary_app/home.html', context)


""" class PostListView(ListView):
        model = Entry
        template_name = 'diary_app/home.html'
        context_object_name = 'entries'
        ordering = ['-date_posted']
        paginate_by = 5

        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
                return super().dispatch(*args, **kwargs)

        # Override get_context_data and add any additional querysets to the context.
        def get_context_data(self, **kwargs):
                context = super(PostListView, self).get_context_data(**kwargs)
                context['count_entries'] = Entry.objects.all().count()
                # Add any other variables to the context here
                ...
                return context """


@login_required
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        title = request.POST.get('title')
        text = request.POST.get('text')
        drafts = request.POST.get('drafts')
        save = request.POST.get('save')

        """ if drafts is not None:
                drafts_flag = True 
                post_save = Entry(title=title, text=text, drafts=drafts_flag, author=request.user)
                post_save.save()
                current = Entry.objects.latest('date_posted')
                return redirect('readmore', id=current.id) """

        if save is not None and form.is_valid():
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
        entry = get_object_or_404(Entry, id=id, author=request.user)
        entry.delete()
        return redirect('home')


@login_required
def edit(request,id):
        #entry = Entry.objects.get(id=id)
        entry = get_object_or_404(Entry, id=id, author=request.user)
        if request.method == 'POST':
                form = EntryForm(request.POST, instance = entry)
                if form.is_valid():
                        form.save()
                        return redirect('readmore', id=id)
        else:
                form = EntryForm()
                #return render(request,"diary_app/edit.html",{'eform':form,'entry':entry})
        return render(request,"diary_app/edit.html", {'entry': entry}) # indentation ?


@login_required
def readmore(request, id):
    #entry = Entry.objects.get(id=id)
    entry = get_object_or_404(Entry, id=id, author=request.user)
    return render(request, "diary_app/readmore.html", {'entry': entry})


def about(request):
    return render(request, "diary_app/about.html")


@login_required
def contact(request):
        return render(request, "diary_app/contact.html")


def SignUp(request):
        if request.method == 'POST':
                form = UserForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect("/signin/")
        else:
                form = UserForm()
        return render(request, "users/signup.html", {'form': form}) # indentation?


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


@login_required
def Trash(request):
        entries = Entry.objects.filter(author=request.user, trash=True)
        entries = entries.order_by('-date_posted')
        count_entries = entries.count()
        context = {'entries': entries, 'count_entries': count_entries}
        return render(request, 'diary_app/trash.html', context)