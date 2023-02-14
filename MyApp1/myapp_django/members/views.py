from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member, User
from .forms import MemberForm,UpdateMember,UpdateUser, CreateMember,CreateUser
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView



# Importamos modelo Member y la función generate_slug_hash
from .models import Member
# from .models import generate_slug_hash


###### Otras vistas iniciales

def start(request):
    template= loader.get_template('start.html')
    return HttpResponse(template.render())

def main(request):
    template= loader.get_template('main.html')
    return HttpResponse(template.render())
    

def members2(request):
    return HttpResponse("Hello world!")

def Er_404(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())



# #### my primer form
# def form_1(request):
#     try:
#         context={}
#         context['form']= New_member()
#         return render (request, 'form_1.html' , context)
#     except NameError as error:
#        return render(request, 'form_1.html', {'error': error})


#############CRUD Members ################################
#Vista member listamos todos los miembros de members

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('members/all_members.html')
    context ={
        'mymembers':mymembers
    }
    return HttpResponse(template.render(context,request))

#Vista de mebers que nos muestra el detalle de membre 

def details(request,slug):
    mymembers = Member.objects.get(slug=slug)
    template = loader.get_template("members/details_members.html")
    context ={
            'mymembers':mymembers
        }
    return HttpResponse(template.render(context,request))

# Update members
def update_member( request, slug):
    member = Member.objects.get(slug=slug)
    form = UpdateMember(instance= member)
    return render(request,'members/update_member.html',{'form':form, 'slug':slug } )

def form_update_member(request,slug):
    member = Member.objects.get(slug=slug)
    form = UpdateMember(request.POST,instance=member)
    try:
        if form.is_valid():
            form.save()
            form=UpdateMember()
            msg = f'El Membre con slug {slug} ha sido actualizado'
        mymembers =Member.objects.all()
        return render(request,'members/all_members.html',{'msg':msg ,'mymembers': mymembers})
    except :
        msg = f'El Membre con slug {slug} NO ha sido actualizado'
        member = Member.objects.get(slug=slug)
        form = UpdateMember(instance= member)
        return render(request,'members/update_member.html', {'msg': msg, 'form': form, 'member': member })
    

# Vista delete ejemplo con form
def delete_member (request, slug):
    member = Member.objects.get(slug=slug)
    member.delete()
    msg = f'El miembro {member.slug} ha sido borrado'
    mymembers =Member.objects.all().values()
    return render(request, 'members/all_members.html',  {'msg':msg ,'mymembers': mymembers} )


def create_member(request):
    if request.method == 'POST':
        form = CreateMember(request.POST)
        if form.is_valid():
            form.save()
            msg= f'The member has been created successfully'
            mymembers = Member.objects.all().values()
            return render(request,'members/all_members.html', {'msg': msg,'mymembers': mymembers})
        else: 
          error = "El formulario no es válido."
          return render(request, 'members/create_member.html', {'error': error})
    elif request.method == 'GET':
        form= CreateMember()
        return render(request, 'members/create_member.html', {'form': form})






#########USERS#############################################################################

class Userviews(ListView):
    model = User
    template_name = 'Users/all_users.html'
    context_object_name = 'all_users'

class Userviews2(ListView):
    model = User
    template_name = 'Users/all_users_Generic.html'
    context_object_name = 'all_users'

class DetailUser(DetailView):
    model = User
    template_name =  'Users/detail_user.html'
    context_object_name = 'detail_user' 

#Vista PARA USER que levanta y borrar formulario (problema lo borrar pero no vewmos resultado)
def delete_user(request,id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        msg = f'Se ha eliminado el Member {user.username}'
        all_users = User.objects.all().values()
        return render (request ,'Users/all_users.html', {'msg' : msg, 'all_users':all_users})
    except User.DoesNotExist as error:
        Error = f"El member {id} no existe."
        all_users = User.objects.all().values()
        return render(request, 'Users/all_users.html', {'Error': Error, 'all_users':all_users})


#vista que levanta formulario para crear miembro y funciona

def create_user(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            msg= f'The user has been created successfully'
            all_users = User.objects.all().values()
            return render(request,'Users/all_users.html', {'msg': msg, 'all_users': all_users})
        else: 
          error = "El formulario no es válido."
          return render(request, 'Users/create_user.html', {'error': error})
    elif request.method == 'GET':
        form = CreateUser()
        return render(request, 'Users/create_user.html', {'form': form})


#vista que levanta  formulario para actualizar
def edit_user(request, id):
    user = User.objects.filter(pk=id).first() #Para listar varios registros
    form = UpdateUser(instance=user)
    return render(request,'Users/edit_user.html',{'form' : form})


# funcion para actulizar boton de actualizar del button del form de update
def update_user(request):
    try:
        form = UpdateUser(request.POST)
        if form.is_valid():
            form.save()
            all_users = User.objects.all().values()
            msg = "User Actualizado"
        return render(request, 'Users/all_users.html', {'msg': "User Actualizado", 'all_users': User.objects.all().values()})
    except TypeError as Error:
        msg = f'En Usuairio no se ha actualizado. Error:{Error}'
        all_users = User.objects.all().values()
        return render(request,'Users/all_users.html',{'msg': msg , 'all_users': all_users})






###### EJEMPLOS CON VISTA GENERICAS FUNCIONAN
class Userviews(ListView):
    model = User
    template_name = 'Users/all_users.html'
    context_object_name = 'all_users'

class Userviews2(ListView):
    model = User
    template_name = 'Users/all_users_Generic.html'
    context_object_name = 'all_users'

class DetailUser(DetailView):
    model = User
    template_name =  'Users/detail_user.html'
    context_object_name = 'detail_user' 

