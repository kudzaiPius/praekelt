from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from campus.models import Lecturer
from campus.forms import messageLecturerForm

# Create your views here.
def admin_table(request):
     template = loader.get_template("admin_table.html")

     ordered_lecturers = Lecturer.objects.order_by("name", "surname")

     context = Context({
          "ordered_lecturers": ordered_lecturers,
     })
 
     return HttpResponse(template.render(context))

def message_lecturer(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = messageLecturerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect(reverse("message_lecturer"))
    else:
        form = messageLecturerForm()

    ordered_lecturers = Lecturer.objects.order_by("name", "surname")
    context = Context({
		"ordered_lecturers": ordered_lecturers,
	})
    return HttpResponse(loader.get_template("message_lecturer.html").render(
        context), {"form":form})