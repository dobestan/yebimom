from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Form
from centers.forms import CenterForm


def center_registration(request):
    if request.method == 'GET':
        center_form = CenterForm()
    else:
        center_form = CenterForm(request.POST)

        if center_form.is_valid():
            return HttpResponseRedirect('/center/register_ok')

    return render(
        request,
        'centers/center_registration.html',
        {'center_form': center_form}
    )


def center(request):
    return HttpResponse("Center")
