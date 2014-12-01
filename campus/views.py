from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from campus.forms import messageLecturerForm

from campus import models as m

# Create your views here.
def adminTable(request):
     template = loader.get_template('adminTable.html')

     ordered_lecturers = m.Lecturer.objects.order_by("name", "surname")

     context = Context({
          'ord_lect': ordered_lecturers,
     })
 
     return HttpResponse(template.render(context))

def messageLecturer(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = messageLecturerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/campus/')
    else:
        form = messageLecturerForm()
    lect = m.Lecturer.objects.order_by("name", "surname")
    context = Context({
		'lect': lect,
	})
    return HttpResponse(loader.get_template('messageLecturer.html').render(context), {'form':form})