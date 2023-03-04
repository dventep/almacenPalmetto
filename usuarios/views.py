from django.shortcuts import render, redirect
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

def login(request):
    """
        ----------
        Description
            Esta función nos permite obtener los datos para permitir que la persona prosiga.
    """
    try:
        content_return = {}
        if not request.session.get('login'):
            return redirect('/')
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
