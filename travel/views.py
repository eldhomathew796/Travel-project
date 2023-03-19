from django.shortcuts import render
from .models import place,person
# Create your views here.
def homs(request):
    pla=place.objects.all()
    name=person.objects.all()
    return render(request,"homs.html",{'values':pla,'per':name})
  
   

