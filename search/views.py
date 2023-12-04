from django.http import HttpResponse
from django.shortcuts import redirect, render
from search.forms import SearchForm, WichaForm
from search.models import wicha

# Create your views here.
def home(req):
    obj = wicha.objects.all()
    return render(req,"home.html" ,{'obj': obj})

def search(req):
    if req.method == 'GET':
        form = SearchForm(req.GET)
        if form.is_valid():
            query = form.cleaned_data.get('search_query')
            results = wicha.objects.filter(name=query)
            results2 = wicha.objects.filter(subject_id=query)
        else:
            results = wicha.objects.all()
            results2 = wicha.objects.all()
    else:
        form = SearchForm()
        results = wicha.objects.all()
        results2 = wicha.objects.all()
    return render(req, 'search.html', {'form': form, 'results': results, 'results2': results2})

def update(req,id):
    ob = wicha.objects.get(pk=id)
    form = WichaForm(req.POST,instance=ob)
    if form.is_valid():
        form.instance.owner = req.user
        form.save()
        return redirect(home)
    return render(req,'update.html',{'wicha':ob})

def delete_item(req, id):
    item = wicha.objects.get(pk=id)
    item.delete()
    return redirect(search)
