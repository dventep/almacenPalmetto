from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
import traceback
import requests

def make_request_get(url, params=False):
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

def login(request):
    """
        ----------
        Description
            Esta función nos permite obtener los datos para permitir que la persona prosiga.
    """
    try:
        content_return = {}
        # if not request.session.get('login'):
        #     return redirect('/')
        if request.POST:
            data_to_send = [request.POST.get('usuario', ''), request.POST.get('password', '')]
            login_to_api = make_request_get("http://localhost:3000/user", params=data_to_send)
            if login_to_api:
                request.session['login'] = {
                    'usuario': login_to_api.get('usuario'),
                    'nombre': login_to_api.get('nombre'),
                    'apellido': login_to_api.get('apellido')
                }
                request.session['no_found'] = False
                return redirect("/")
            else:
                request.session['login'] = False
                request.session['no_found'] = True
    except:
        print(traceback.format_exc())
        
    return render(request, 'ingreso.html', content_return)
    
def list_users(request):
    """
        ----------
        Description
            Esta función nos trae la lista de usuarios.
    """
    if 'login' in request.session:
        request_to_api = make_request_get("http://localhost:3000/user")
        users_list = []
        if request_to_api:
            users_list = request_to_api
        return render(request, 'list_users.html', {"users":users_list})
    else:
        return redirect('/usuarios/')
    
def logout_function(request):
    """
        ----------
        Description
            Esta función es para eliminar las variables de sesión y que se vuelva a logear
    """
    if 'login' in request.session:
        request.session['login'] = False
        request.session['no_found'] = False
    return redirect('/usuarios/')
    
def getUser(request):
    """
        ----------
        Description
            Esta función trae todos los campos del user.
    """
    user_info = {}
    if 'login' in request.session:
        if 'edit_user_' in request.POST['id'] and len(request.POST['id'].split('edit_user_')) > 0:
            id_to_send = (request.POST['id'].split('edit_user_'))[1]
            request_to_api = make_request_get(f"http://localhost:3000/user/{id_to_send}")
            if request_to_api:
                user_info = request_to_api
        # if request_to_api:
        #     user_info = request_to_api
    content_return = {'user':user_info}
    html = render_to_string("base/formUser.html", content_return)
    return HttpResponse(html)
    
def goToUser(request):
    """
        ----------
        Description
            Esta función trae los campos para llenar y crear el registro.
    """
    content_return = {}
    html = render_to_string("base/formUser.html", content_return)
    return HttpResponse(html)

def createUser(request):
    """
        ----------
        Description
            Esta función actualiza un usero determinado.
    """
    content_return = {'error':[]}
    if 'login' in request.session:
        if request.POST.get('name_user', False) and request.POST.get('lastname_user', False) and request.POST.get('user_user', False) and request.POST.get('password_user', False) and request.POST.get('telephone_user', False) and request.POST.get('email_user', False):
            json_to_send = {
                'nombre': request.POST.get('name_user'),
                'apellido': request.POST.get('lastname_user'),
                'usuario': request.POST.get('user_user'),
                'password': request.POST.get('password_user'),
                'telefono': request.POST.get('telephone_user'),
                'email': request.POST.get('email_user')
            }
            print('to_send',json_to_send)
            request_to_api = make_request_post("http://localhost:3000/user", json_to_send)
            if not request_to_api:
                content_return['error'].append('Durante el proceso surgió un error.')
        else:
            content_return['error'].append('No se recibió el ID adecuado.')
    return JsonResponse(content_return, safe=False)
    
def putUser(request):
    """
        ----------
        Description
            Esta función actualiza un usero determinado.
    """
    content_return = {'error':[]}
    if 'login' in request.session:
        if request.POST.get('id', False):
            json_to_send = {
                'id': request.POST.get('id'),
                'nombre': request.POST.get('name_user'),
                'apellido': request.POST.get('lastname_user'),
                'usuario': request.POST.get('user_user'),
                'password': request.POST.get('password_user'),
                'telefono': request.POST.get('telephone_user'),
                'email': request.POST.get('email_user')
            }
            request_to_api = make_request_put("http://localhost:3000/user/{}" .format(request.POST.get('id')), json_to_send)
            if not request_to_api:
                content_return['error'].append('Durante el proceso surgió un error.')
        else:
            content_return['error'].append('No se recibió el ID adecuado.')
    return JsonResponse(content_return, safe=False)
    
def deleteUser(request):
    """
        ----------
        Description
            Esta función elimina el usero enviado.
    """
    content_return = {'error':[]}
    if 'login' in request.session:
        if 'delete_user_' in request.POST['id'] and len(request.POST['id'].split('delete_user_')) > 0:
            id_to_send = (request.POST['id'].split('delete_user_'))[1]
            request_to_api = make_request_delete(f"http://localhost:3000/user/{id_to_send}")
            if not request_to_api:
                content_return['error'].append('Durante el proceso surgió un error.')
        else:
            content_return['error'].append('No se recibió el ID adecuado.')
        # request_to_api = make_request_delete("http://localhost:3000/user")
        # useros_list = []
        # if request_to_api:
        #     useros_list = request_to_api
        pass
    return JsonResponse(content_return, safe=False)
        
