from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib import messages

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
            messages.success(request, "cool", fail_silently=True)
            return HttpResponseRedirect(reverse("message_lecturer"))
    else:
        form = messageLecturerForm()

    ordered_lecturers = Lecturer.objects.order_by("name", "surname")
    return render_to_response(
        "message_lecturer.html",
        {"ordered_lecturers": ordered_lecturers},
        context_instance=RequestContext(request)
    )
