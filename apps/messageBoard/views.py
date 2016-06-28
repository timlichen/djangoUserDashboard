from django.shortcuts import render

# Create your views here.
def index(request):
    print "i am at the board's index route"
    return render(request, "board/index.html")
