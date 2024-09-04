from django import forms
from django.forms import ModelForm
from .models import Doctor, Patient, Operation, Nurse, Nurse_List


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"

        labels = {

            'Name':'',
            'mobile':'',
            'special':''}
       
        widgets = {

            'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Doctor Name'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Phone Number'}),
            'special':forms.Select(attrs={'class':'form-control','placeholder':'Enter Doctor Specialization'})}
        


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

        labels = {
            'name':'',
            'gender':'',
            'mobile':'',
            'address':''}
       
        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Patient Name'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Enter Patient Gender'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Phone Number'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Patient Address'})}            


class NurseForm(ModelForm):
    class Meta:
        model = Nurse
        fields = "__all__"

        labels = {

            'Name':'',
            'mobile':'',
            'experience':''}
       
        widgets = {

            'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Nurse Name'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Phone Number'}),
            'experience':forms.Select(attrs={'class':'form-control','placeholder':'Enter Nurse Experience'})}

class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = "__all__"

        labels = {
            'doctor':'Doctor Name',
            'patient':'Patient Name',
            'department':'Department',
            'date':'Date',
            'time':'Time'}
       
        widgets = {

            'doctor':forms.Select(attrs={'class':'form-control','placeholder':'Enter Doctor Name'}),
            'patient':forms.Select(attrs={'class':'form-control','placeholder':'Enter Patient Name'}),
            'department':forms.Select(attrs={'class':'form-control','placeholder':'Select The department'}),
            'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Operation Date'}),
            'time':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter Operation Time'})}


class Nurse_ListForm(ModelForm):
    class Meta:
        model = Nurse_List
        fields = "__all__"

        labels = {
            'nurse':'Nurse Name',
            'operation':'Operation Name'}
       
        widgets = {

            'nurse':forms.Select(attrs={'class':'form-control','placeholder':'Select Nurse Name'}),
            'operation':forms.Select(attrs={'class':'form-control','placeholder':'Select Operation Name'})}
        