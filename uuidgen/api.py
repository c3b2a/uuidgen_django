from django.http import HttpResponse

import uuid,string,random

def random_string(length):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits,length))
    return ran_str

def process(req):
	get = req.GET;
	if 'version' in get:
		if get['version'] == '1':
			return HttpResponse(uuid.uuid1())
		elif get['version'] == '3':
			return HttpResponse(uuid.uuid3(uuid.NAMESPACE_DNS,random_string(32)))
		elif get['version'] == '4':
			return HttpResponse(uuid.uuid4())
		elif get['version'] == '5':
			return HttpResponse(uuid.uuid5(uuid.NAMESPACE_DNS,random_string(32)))
		else:
			return HttpResponse('')
	else:
		return HttpResponse('')