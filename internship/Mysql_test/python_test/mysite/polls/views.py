
from django.shortcuts import render


# views.py
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            string = form.cleaned_data['search']
            terms = re.compile(r'[^\s",;.:]+').findall(string)
            fields = ['field1', 'field1', '...'] # your field names
            query = None
            for term in terms:
                for field in fields:
                    qry = Q(**{'%s__icontains' % field: term})
                    if query is None:
                        query = qry
                    else:
                        query = query | qry
            found_entries = Patient.objects.filter(query).order_by('-something') # your model
            return render(request, 'results.html', {'found_entries':found_entries})
    else:
        form = SearchForm()
        return render(request, 'search.html', {'form':form})

