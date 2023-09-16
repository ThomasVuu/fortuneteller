from django.shortcuts import render
import random

# Create your views here.
def fortune(request):
    fortuneList = ["You will be rich", "You will be poor", "You will be happy", "You will be sad", "You will be healthy", "You will be sick", "You will be lucky", "You will be unlucky", "You will be famous", "You will be infamous"] 
    fortune = random.choice(fortuneList)
    return render(request, 'randomfortune/fortune.html', {'fortune': fortune})