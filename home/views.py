from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView





def home(request):
    """
    Return home page
    """
    return render(request, 'home/home.html')




def about(request):
    """
    Return About off documentation
    """
    return render(request, 'about/documentation.html')







def contact(request):
    """
    Return contact page
    """
    return render(request, 'support/contact.html')
