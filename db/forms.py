from django import forms
from .models import DiseaseType, Country, Disease, Discover, Users, PublicServant, Doctor, Specialize, Record
 
 
class DateInput(forms.DateInput):
    input_type = 'date'
    
    
class DiseaseTypeForm(forms.ModelForm):
    class Meta:
        model = DiseaseType
        fields = ('description',)
    
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('cname', 'population')
        
        labels = {
            'cname': ('Country'),
        }

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = "__all__"
        
        labels = {
            'diseaseCode': ('Disease Code'),
            'id_dt': ('Disease Type'),
        }

class DiscoverForm(forms.ModelForm):
    class Meta:
        model = Discover
        fields = "__all__"
        
        labels = {
            'cname': ('Country'),
            'diseaseCode': ('Disease Code'),
            'firstEncDate': ('First Encountered Date'),
        }
        widgets = {
            'made_on': DateInput(),
        }

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        
        labels = {
            'cname': ('Country'),
        }
        
class PublicServantForm(forms.ModelForm):
    class Meta:
        model = PublicServant
        fields = "__all__"
        
class SpecializeForm(forms.ModelForm):
    class Meta:
        model = Specialize
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(SpecializeForm, self).__init__(*args, **kwargs)
        self.fields['email']=forms.ModelChoiceField(queryset=Doctor.objects.values_list('email_id__email', flat=True))
        
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        
class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
        
        labels = {
            'cname': ('Country'),
            'diseaseCode': ('Disease Code'),
            'totalDeath': ('Total Death'),
            'totalPatients': ('Total Patients'),
        }
    
    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['email']=forms.ModelChoiceField(queryset=PublicServant.objects.values_list('email_id__email', flat=True))
        
        
