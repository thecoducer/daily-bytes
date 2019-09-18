from django.shortcuts import render

from search.documents import EntryDoc

# Create your views here.


def search(request):
    q = request.GET.get('q')

    if q:
        results = EntryDoc.search().query("match", title=q)
    else:
        results = ''
    
    return render(request, 'search.html', {'results': results})