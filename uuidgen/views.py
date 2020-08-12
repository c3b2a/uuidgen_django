from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators import csrf

import uuid, random, string

def random_str(length):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, length))
    return ran_str

def display(req):
    if req.method == "GET":
        return render(req, "index.html", {'uuid': uuid.uuid3(uuid.NAMESPACE_DNS, random_str(32)), 'List': [False, False, True, False, False]})
    elif req.method == "POST":
        if 'mode_select' in req.POST:
            if req.POST['mode_select'] == 'uuid1':
                return render(req, "index.html", {'uuid': uuid.uuid1(), 'List': [True, False, False, False, False]})
            elif req.POST['mode_select'] == 'uuid3':
                return render(req, 'index.html', {'uuid': uuid.uuid3(uuid.NAMESPACE_DNS, random_str(32)), 'List': [False, False, True, False, False]})
            elif req.POST['mode_select'] == 'uuid4':
                return render(req, 'index.html', {'uuid': uuid.uuid4(), 'List': [False, False, False, True, False]})
            elif req.POST['mode_select'] == 'uuid5':
                return render(req, 'index.html', {'uuid': uuid.uuid5(uuid.NAMESPACE_DNS, random_str(32)), 'List': [False, False, False, False, True]})
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
