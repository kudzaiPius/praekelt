from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from campus import models as m

# Create your views here.
def adminTable(request):
    template = loader.get_template('adminTable.html')

    ordered_lecturers = m.Lecturer.objects.order_by("name", "surname")

    context = Context({
        'ord_lect': ordered_lecturers,
    })
 
    return HttpResponse(template.render(context))