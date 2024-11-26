from django.shortcuts import render

# Create your views here.


#my landing page
def index_page(request):
    """ Display the home page """
    return render(request, "index.html")