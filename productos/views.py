from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
# Create your views here.
def make_request_get(url, params={}):
    if params:
        response = requests.get("{}/{}" .format(url, "/".join(params)))
        print(response)
    else:
        response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return False
def make_request_post(url, params={}):
    response = requests.post(url, data=params)
    if response.status_code == 200:
        return response.json()
    else:
        return False
def make_request_delete(url):
    response = requests.delete(url)
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        return False
    
def home(request):
    """
        ----------
        Description
            Esta función trae todos los productos.
    """
    if 'login' in request.session:
        request_to_api = make_request_get("http://localhost:3000/productos")
        productos_list = []
        if request_to_api:
            productos_list = request_to_api
        return render(request, 'productos.html', {"products":productos_list})
    else:
        return redirect('/usuarios/')
    
def getProduct(request):
    """
        ----------
        Description
            Esta función trae todos los productos.
    """
    product_info = {}
    if 'login' in request.session:
        print(request.POST)
        if 'edit_product_' in request.POST['id'] and len(request.POST['id'].split('edit_product_')) > 0:
            id_to_send = (request.POST['id'].split('edit_product_'))[1]
            request_to_api = make_request_get(f"http://localhost:3000/productos/{id_to_send}")
            if request_to_api:
                product_info = request_to_api
        # if request_to_api:
        #     product_info = request_to_api
    return JsonResponse(product_info, safe=False)
    
def deleteProduct(request):
    """
        ----------
        Description
            Esta función trae todos los productos.
    """
    if 'login' in request.session:
        request_to_api = make_request_delete("http://localhost:3000/productos")
        productos_list = []
        if request_to_api:
            productos_list = request_to_api
        return render(request, 'productos.html', {"products":productos_list})
    else:
        return redirect('/usuarios/')
        