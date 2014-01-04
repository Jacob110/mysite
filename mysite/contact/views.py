from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.shortcuts import render_to_response,RequestContext
from forms import ContactForm


def contact(request):
    errors = []
    response=HttpResponse()
    data={
        'subject':'test',
        'email':'test@test.com',
        'message':'testmsg'
    }
    if request.method == 'POST':
        f=ContactForm(request.POST)

        print request.POST.dict()

        #f=ContactForm(data)
        #response.write(request.POST)
        #response.write(f.clean)
        response.write(f.is_valid())
    return response
 #        if not request.POST.get('subject', ''):
 #            errors.append('Enter a subject.')
 #        if not request.POST.get('message', ''):
 #            errors.append('Enter a message.')
 #        if request.POST.get('email') and '@' not in request.POST['email']:
 #            errors.append('Enter a valid e-mail address.')
 #        if not errors:
 #            send_mail(
 #                request.POST['subject'],
 #                request.POST['message'],
 #                request.POST.get('email', 'noreply@example.com'),
 #                ['siteowner@example.com'],
 #            )
 #            return HttpResponseRedirect('/contact/thanks/',context_instance=RequestContext(request))
 #    return render_to_response('contact_form.html',
 #        {'errors': errors,
	# 'subject': request.POST.get('subject', ''),
 #        'message': request.POST.get('message', ''),
 #        'email': request.POST.get('email', ''),
	# },context_instance=RequestContext(request))
