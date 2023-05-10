from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
import requests
# Create your views here.
url_connect = "localhost"
url_connect = "vmclient.brazilsouth.cloudapp.azure.com"
def make_request_get(url, params={}):
    if params:
        response = requests.get("{}/{}" .format(url, "/".join(params)))
    else:
        response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return False
    
def make_request_post(url, params={}):
    if params:
        response = requests.post(url, json=params, headers = {'Content-Type': "application/json", 'Accept': "application/json"})
    else:
        return False
    if response.status_code == 200:
        return response.json()
    else:
        return False
    
def make_request_delete(url):
    response = requests.delete(url)
    # print(response)
    if response.status_code == 200:
        return True
    else:
        return False
    
def make_request_put(url, params={}):
    if params:
        response = requests.put(url, json=params, headers = {'Content-Type': "application/json", 'Accept': "application/json"})
    else:
        return False
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
        request_to_api = make_request_get(f"http://{url_connect}:3000/productos")
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
        if 'edit_product_' in request.POST['id'] and len(request.POST['id'].split('edit_product_')) > 0:
            id_to_send = (request.POST['id'].split('edit_product_'))[1]
            request_to_api = make_request_get(f"http://{url_connect}:3000/productos/{id_to_send}")
            if request_to_api:
                product_info = request_to_api
        # if request_to_api:
        #     product_info = request_to_api
    content_return = {'product':product_info}
    html = render_to_string("base/formProduct.html", content_return)
    return HttpResponse(html)
    
def goToProduct(request):
    """
        ----------
        Description
            Esta función trae los campos para llenar y crear el registro.
    """
    content_return = {}
    html = render_to_string("base/formProduct.html", content_return)
    return HttpResponse(html)

def createProduct(request):
    """
        ----------
        Description
            Esta función actualiza un producto determinado.
    """
    content_return = {'error':[]}
    if 'login' in request.session:
        if request.POST.get('name_product', False) and request.POST.get('descrip_product', False) and request.POST.get('price_product', False) and request.POST.get('inventory_product', False):
            json_to_send = {
                'nombre': request.POST.get('name_product'),
                'descripcion': request.POST.get('descrip_product'),
                'precio': request.POST.get('price_product'),
                'inventario': request.POST.get('inventory_product')
            }
            print('to_send',json_to_send)
            request_to_api = make_request_post(f"http://{url_connect}:3000/productos", json_to_send)
            if not request_to_api:
                content_return['error'].append('Durante el proceso surgió un error.')
        else:
            content_return['error'].append('No se recibió el ID adecuado.')
    return JsonResponse(content_return, safe=False)
    
def putProduct(request):
    """
        ----------
        Description
            Esta función actualiza un producto determinado.
    """
    content_return = {'error':[]}
    if 'login' in request.session:
        if request.POST.get('id', False):
            json_to_send = {
                'id': request.POST.get('id'),
                'nombre': request.POST.get('name_product'),
                'descripcion': request.POST.get('descrip_product'),
                'precio': request.POST.get('price_product'),
                'inventario': request.POST.get('inventory_product')
            }
            request_to_api = make_request_put("http://{}:3000/productos/{}" .format(url_connect, request.POST.get('id')), json_to_send)
            if not request_to_api:
                content_return['error'].append('Durante el proceso surgió un error.')
        else:
            content_return['error'].append('No se recibió el ID adecuado.')
    return JsonResponse(content_return, safe=False)
    
def deleteProduct(request):
    """
        ----------
        Description
            Esta función elimina el producto enviado.
    """
    content_return = {'error':[]}
    if 'login' in request.session:
        if 'delete_product_' in request.POST['id'] and len(request.POST['id'].split('delete_product_')) > 0:
            id_to_send = (request.POST['id'].split('delete_product_'))[1]
            request_to_api = make_request_delete(f"http://{url_connect}:3000/productos/{id_to_send}")
            if not request_to_api:
                content_return['error'].append('Durante el proceso surgió un error.')
        else:
            content_return['error'].append('No se recibió el ID adecuado.')
        # request_to_api = make_request_delete(f"http://{url_connect}:3000/productos")
        # productos_list = []
        # if request_to_api:
        #     productos_list = request_to_api
        pass
    return JsonResponse(content_return, safe=False)
        
