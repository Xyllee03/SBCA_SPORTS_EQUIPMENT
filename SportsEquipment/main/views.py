from django.shortcuts import render

# Create your views here.


def index(request):
    context= {}
    return render(request,"main/index.html", context)


def user_base(request):

    context ={}

    return render(request,"main/users/user_base.html", context)

def user_borrow(request):
    context ={}
    return render(request, "main/users/user_borrow.html", context)


def user_equipmentDetails(request):
    context ={}
    return render(request, "main/users/user_equipmentDetails.html", context)

def user_preRequestDetails(request):
    context ={}
    return render(request, 'main/users/user_preRequestDetails.html', context)