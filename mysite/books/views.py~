from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book
# Create your views here.

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	# errors info
	errors=[]
	if 'q' in request.GET :
		q=request.GET['q']
		
		if not q:
			#error=True
			errors.append('Enter a search term.')
		elif len(q) > 20:
			#error=True
			errors.append('Plz enter at most 20 charactors.')
		else:			
			books=Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html',{'books':books,'query':q})
			#message='You searched for: %r' % request.GET['q']
	#else:
		#return HttpResponse('Please submit a search term.')
		#return HttpResponse(message)
	return render_to_response('search_form.html',{'errors':errors})


