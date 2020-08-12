from django.http import HttpResponse

def get_connect_ip(req):
	ip = req.META.get('HTTP_X_FORWARDED_FOR')
	if not ip:
		return HttpResponse(req.META.get('REMOTE_ADDR'))
	return HttpResponse(ip.split(', ')[0])