from django.shortcuts import render

# Create your views here.


def products(request, pk_id):
    # product = Prod
    return render(request, 'bootstrap_file.html')
    pass
