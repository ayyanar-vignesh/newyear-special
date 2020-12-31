from django.shortcuts import render


def index(request):
    return render(request,'sub_part/index.html')