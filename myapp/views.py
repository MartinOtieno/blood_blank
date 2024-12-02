from django.shortcuts import render

# Create your views here.


#my landing page
def index_page(request):
    """ Display the home page """
    return render(request, "index.html")
#about us
def about_page(request):
    """ Display the about us page """
    return render(request, "about.html")
#Blood
def blood_page(request):
    """ Diplay the bllod page """
    return render(request, 'blood.html')