from django.shortcuts import render, redirect
from diary_app.models import Entry, UserData
from django.contrib.auth.models import User
from diary_app.forms import EntryForm, UserForm, ProfileUpdateForm, ContactForm, UserUpdateForm, UserUpdateForm, NewUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.utils.translation import ugettext as _
# importing generic views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

""" @login_required
def home(request):
    entries = Entry.objects.filter(author=request.user, trash=False)
    count_entries = entries.count()
    entries = entries.order_by('-date_posted')
    paginator = Paginator(entries, 5)   
    page = request.GET.get('page') 
    entries = paginator.get_page(page)
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
                entries = Entry.objects.filter(author=self.request.user, trash=False)
                context['count_entries'] = entries.count()
                return context

        def get_queryset(self):
                entries = Entry.objects.filter(author=self.request.user, trash=False)
                entries = entries.order_by('-date_posted')
                return entries


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
        if entry.trash == False:
                entry.trash = True
                entry.save()
                return redirect('home')
        else:
                entry.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def confirmdelete(request, id):
        entry = get_object_or_404(Entry, id=id, author=request.user)
        return render(request, "diary_app/confirmdelete.html", {'entry': entry})


@login_required
def restore(request, id):
        entry = get_object_or_404(Entry, id=id, author=request.user)
        if entry.trash == True:
                entry.trash = False 
                entry.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

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

@login_required
def about(request):
    return render(request, "diary_app/about.html")


@login_required
def contact(request):
        user = get_object_or_404(User, username = request.user.username)
        if request.method == 'POST':
                form = ContactForm(request.POST)
                message = request.POST.get('message')
                sender = request.POST.get('sender')
                message = message + "\n\n Sender's Email: " + sender
                send_mail('Daily Bytes contact form', message, sender, [settings.EMAIL_HOST_USER], fail_silently=False)
        else:
                form = ContactForm()
        return render(request, "diary_app/contact.html", {'user': user, 'form': form})


def SignUp(request):
        if request.user.is_authenticated == True:
                return redirect('home')

        if request.method == 'POST':
                form = UserForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect("/signin/")
        else:
                form = UserForm()
        return render(request, "users/signup.html", {'form': form})


@login_required
def SocialSignUp(request):
        if request.user.has_usable_password() == False:
                new_user = User.objects.get(username=request.user.username)

                if request.method == 'POST':
                        form = NewUserForm(request.POST, instance=new_user)
                        if form.is_valid():
                                form.save()
                                return redirect('home')
                else:
                        form = NewUserForm()
                return render(request, 'users/social-signup.html', {'form': form, 'new_user': new_user})
        else:
                return redirect('home')

@login_required
def SignOut(request):
        logout(request)
        return redirect('signin')


@login_required
def Trash(request):
        entries = Entry.objects.filter(author=request.user, trash=True)
        context = {'entries': entries}
        return render(request, 'diary_app/trash.html', context)


@login_required
def Profile(request):

        current_user = request.user
        new_user = User.objects.get(username=request.user.username)
        
        try:
                get_bio = UserData.objects.get(user=current_user)
        except:
                # creating an object of UserData
                new = UserData(user=request.user, bio=" ")
                new.save()
                get_bio = UserData.objects.get(user=current_user)

        if request.method == 'POST':
                uform = UserUpdateForm(request.POST, instance=current_user)
                puform = ProfileUpdateForm(request.POST, instance=get_bio)
                pcform = PasswordChangeForm(request.user, request.POST)
                nuform = NewUserForm(request.POST, instance=new_user)

                if uform.is_valid() and puform.is_valid() and pcform.is_valid():
                        puform.save()
                        uform.save()
                        pwd = pcform.save()
                        update_session_auth_hash(request, pwd)
                        nuform.save()
                        return redirect('home')
        else:
                uform = UserUpdateForm()
                puform = ProfileUpdateForm()
                pcform = PasswordChangeForm(request.user)
                nuform = NewUserForm()

        return render(request, "users/profile.html", {'uform': uform, 'puform': puform, 'pcform': pcform, 'nuform': nuform, 'current_user': current_user, 'get_bio': get_bio})
