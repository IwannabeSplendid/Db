from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import DiseaseType, Country, Disease, Discover, Users, PublicServant, Doctor, Specialize, Record
from .forms import DiseaseTypeForm, CountryForm, DiseaseForm, DiscoverForm, UsersForm, PublicServantForm, DoctorForm, SpecializeForm, RecordForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import logout as log_out



tableList= ['Disease Type', 'Country','Disease', 'Discover','Users', "Public Servant", 'Doctor', 'Specialize', 'Record']
urls = ['dt', 'country','disease', 'discover','users', "ps", 'doctor', 'specialize', 'record']
sidenav = zip(tableList, urls)

def index(request):
    doctors = Doctor.objects.order_by('-email__salary').values('email__name', 'email__surname', 'email', 'degree')[:6]
    d_num = Doctor.objects.count()
    p_num = PublicServant.objects.count()
    t_num = Disease.objects.count()
    context = {'doctors' : doctors, 'd_num' : d_num, 'p_num': p_num , 't_num' : t_num}
    
    return render(request, 'index.html', context)

def tables(request):
    return render(request, 'tables.html' )

def dt(request):
    data = DiseaseType.objects.all()
    context ={'sidenav' : sidenav, 'name' : 'Disease Types', 'data' : data}
    return render(request, 'dt.html', context = context)

def dt_add(request):
    if request.method == 'POST':
        form = DiseaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dt')
    
    form = DiseaseTypeForm()
    context ={}
    context['form']= form
    return render(request, "add.html", context)

def dt_edit(request, id):
    elem = DiseaseType.objects.get(id=id)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = DiseaseTypeForm(request.POST, instance=elem)
            if form.is_valid():
                form.save()
        if 'delete' in request.POST:
            elem.delete()
        return redirect('dt')
        
    else:
        form = DiseaseTypeForm(instance=elem)

    return render(request, 'edit.html', {'form': form})
    
def country(request):
    data = Country.objects.all()
    context ={'name' : 'Country', 'data' : data}
    return render(request, 'country.html', context = context)

def country_add(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('country')
    
    form = CountryForm()
    context ={}
    context['form']= form
    return render(request, "add.html", context)

def country_edit(request, id):
    elem = Country.objects.get(id=id)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = CountryForm(request.POST, instance=elem)
            
            if form.is_valid():
                form.save()
        if 'delete' in request.POST:
            elem.delete()
        return redirect('country')
        
    else:
        form = CountryForm(instance=elem)

    return render(request, 'edit.html', {'form': form})

def disease(request):
    data = Disease.objects.values('id', 'diseaseCode', 'pathogen', 'description', 'id_dt_id__description' )
    context ={'name' : 'Disease', 'data' : data}
    return render(request, 'disease.html', context = context)

def disease_add(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('disease')
    
    form = DiseaseForm()
    context ={}
    context['form']= form
    return render(request, "add.html", context)

def disease_edit(request, id):
    elem = Disease.objects.get(id=id)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = DiseaseForm(request.POST, instance=elem)
            if form.is_valid():
                form.save()
        if 'delete' in request.POST:
            elem.delete()
        return redirect('disease')
        
    else:
        form = DiseaseForm(instance=elem)

    return render(request, 'edit.html', {'form': form})

def discover(request):
    data = Discover.objects.values('id','cname_id__cname', 'firstEncDate', 'diseaseCode_id__description')
    context ={'name' : 'Discover', 'data' : data}
    return render(request, 'discover.html', context = context)

def discover_add(request):
    if request.method == 'POST':
        form = DiscoverForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('discover')
    
    form = DiscoverForm()
    context ={}
    context['form']= form
    return render(request, "add.html", context)

def discover_edit(request, id):
    elem = Discover.objects.get(id=id)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = DiscoverForm(request.POST, instance=elem)
            if form.is_valid():
                form.save()
        if 'delete' in request.POST:
            elem.delete()
        return redirect('discover')
        
    else:
        form = DiscoverForm(instance=elem)

    return render(request, 'edit.html', {'form': form})

def users(request):
    data = Users.objects.values('id','email','name','surname','phone','salary','cname_id__cname')
    context ={'name' : 'Users', 'data' : data}
    return render(request, 'users.html', context = context)

def users_add(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('users')
    
    form = UsersForm()
    context ={}
    context['form']= form
    return render(request, "add.html", context)

def users_edit(request, id):
    elem = Users.objects.get(id=id)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = UsersForm(request.POST, instance=elem)
            if form.is_valid():
                form.save()
        if 'delete' in request.POST:
            elem.delete()
        return redirect('users')
        
    else:
        form = UsersForm(instance=elem)

    return render(request, 'edit.html', {'form': form})

def ps(request):
    data = PublicServant.objects.values('id','email_id__email', 'department')
    context ={'sidenav' : sidenav, 'name' : 'Public Servant', 'data' : data}
    return render(request, 'ps.html', context = context)

def ps_add(request):
    if request.method == 'POST':
        form = PublicServantForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ps')
    
    form = PublicServantForm()
    context ={}
    context['form']= form
    return render(request, "add.html", context)

def ps_edit(request, id):
    elem = PublicServant.objects.get(id=id)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = PublicServantForm(request.POST, instance=elem)
            if form.is_valid():
                form.save()
        if 'delete' in request.POST:
            elem.delete()
        return redirect('ps')
        
    else:
        form = PublicServantForm(instance=elem)

    return render(request, 'edit.html', {'form': form})
       
def doctor(request):
    data = Doctor.objects.values('id','email_id__email', 'degree')
    context ={'sidenav' : sidenav, 'name' : 'Doctor', 'data' : data}
    return render(request, 'doctor.html', context = context)

def doctor_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('doctor')
    
    form = DoctorForm()
    context ={}
    context['form']= form
    return render(request, "add.html", context)

def doctor_edit(request, id):
    elem = Doctor.objects.get(id=id)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = DoctorForm(request.POST, instance=elem)
            if form.is_valid():
                form.save()
        if 'delete' in request.POST:
            elem.delete()
        return redirect('doctor')
        
    else:
        form = DoctorForm(instance=elem)

    return render(request, 'edit.html', {'form': form})
  
  
def specialize(request):
    data = Specialize.objects.values('email_id__email_id__email', 'diseaseType_id__description', 'id')
    context ={'name' : 'Specialize', 'data' : data}
    return render(request, 'specialize.html', context = context)

def specialize_add(request):
    if request.method == 'POST':
        if 'diseaseType' and 'email' in request.POST:
            user = Users.objects.get(email = request.POST['email'])
            dt = DiseaseType.objects.get(id =request.POST['diseaseType'])
            doctor = Doctor.objects.get( email = user.id)
            form = Specialize(diseaseType=dt, email=doctor)
            form.save()
        return redirect('specialize')
    
    form = SpecializeForm()
    context ={}
    context['form']= form
    return render(request, "add.html", context)

def specialize_edit(request, id):
    elem = Specialize.objects.get(id=id)

    if request.method == 'POST':
        if 'update' in request.POST:
            if 'diseaseType' and 'email' in request.POST:
                user = Users.objects.get(email = request.POST['email'])
                dt = DiseaseType.objects.get(id =request.POST['diseaseType'])
                doctor = Doctor.objects.get( email = user.id)
                elem.diseaseType = dt
                elem.email = doctor
                elem.save()
        if 'delete' in request.POST:
            elem.delete()
        return redirect('specialize')
     
    else:
        form = SpecializeForm(initial ={'diseaseType' : elem.diseaseType, 'email' : elem.email.email.email})

    return render(request, 'edit.html', {'form': form})


def record(request):
    data = Record.objects.values('id','cname__cname','totalDeath','totalPatients','email_id__email_id__email','diseaseCode_id__description')
    context ={'sidenav' : sidenav, 'name' : 'Record', 'data' : data}
    return render(request, 'record.html', context = context)

def record_add(request):
    if request.method == 'POST':
        print(request.POST)
        if 'diseaseCode' and 'email' and 'cname' and 'totalDeath' and 'totalPatients' in request.POST:
            user = Users.objects.get(email = request.POST['email'])
            d = Disease.objects.get(id =request.POST['diseaseCode'])
            ps = PublicServant.objects.get( email = user.id)
            cname = Country.objects.get(id =request.POST['cname'])
            form = Record(diseaseCode=d, email=ps, totalDeath = request.POST['totalDeath'], totalPatients = request.POST['totalPatients'], cname = cname)
            form.save()
        return redirect('record')
    
    form = RecordForm()
    context ={}
    context['form']= form
    return render(request, "add.html", context)

def record_edit(request, id):
    elem = Record.objects.get(id=id)

    if request.method == 'POST':
        if 'update' in request.POST:
            if 'diseaseCode' and 'email' and 'cname' and 'totalDeath' and 'totalPatients' in request.POST:
                user = Users.objects.get(email = request.POST['email'])
                d = Disease.objects.get(id =request.POST['diseaseCode'])
                ps = PublicServant.objects.get( email = user.id)
                c = Country.objects.get(id =request.POST['cname'])
                elem.diseaseCode = d
                elem.email = ps
                elem.cname = c
                elem.totalDeath = request.POST['totalDeath']
                elem.totalPatients = request.POST['totalPatients']
                elem.save()
        if 'delete' in request.POST:
            elem.delete()
        return redirect('record')
     
    else:
        form = RecordForm(initial ={'diseaseCode' : elem.diseaseCode, 'totalDeath' :elem.totalDeath, 'totalPatients' : elem.totalPatients, 'cname' : elem.cname, 'email' : elem.email.email.email})

    return render(request, 'edit.html', {'form': form})



def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            print(username)
            return redirect( f'/user/{username}')
    form = AuthenticationForm()
    return render(request, 'log.html', {'form': form})

def logout(request):
    log_out(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(user.username)
            return redirect( userpage, name = user.username)
    form = UserCreationForm()
    return render (request, "register.html", context={"register_form":form})

def userpage(request, name):
    return render(request, "userpage.html", context = {'name' :name , 'is_staff' : request.user.is_staff})