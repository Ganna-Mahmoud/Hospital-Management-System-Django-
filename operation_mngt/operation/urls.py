
from django.urls import path
from .views import About,Home,Logout_Home, Contact,Login, Logout_admin,LoginPage, SignupPage, LogoutPage, Index, View_Doctor, Delete_Doctor, Add_Doctor, Add_Doc,Add_Pat,  Add_Oper,Add_Nurse, View_Nurse, Delete_Nurse,Add_Nurse_List, View_Nurse_List, Delete_Nurse_List,  Add_Patient, View_Patient, Delete_Patient, View_Operation, Add_Operation, Delete_Operation

urlpatterns = [
    path('', Home, name='home'),
     path('logout_home', Logout_Home, name='logout_home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),


    path('Signup_Page/', SignupPage, name='Signup_Page'),
    path('Login_Page/', LoginPage, name='Login_Page'),
    path('Logout_Page/', LogoutPage, name='Logout_Page'),


    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('view_operation/', View_Operation, name='view_operation'),
    path('view_nurse/', View_Nurse, name='view_nurse'),
    path('view_nurse_list/', View_Nurse_List, name='view_nurse_list'),


    path('add_doc/', Add_Doc, name='add_doc'),
    path('add_oper/', Add_Oper, name='add_oper'),
    path('add_pat/', Add_Pat, name='add_pat'),
    path('add_nurse/', Add_Nurse, name='add_nurse'),
    path('add_nurse_list/', Add_Nurse_List, name='add_nurse_list'),

    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('add_operation/', Add_Operation, name='add_operation'),


    path('delete_doctor(?P<int:pid>)', Delete_Doctor, name='delete_doctor'),
    path('delete_patient(?P<int:pid>)', Delete_Patient, name='delete_patient'),
    path('delete_operation(?P<int:pid>)', Delete_Operation, name='delete_operation'),
    path('delete_nurse(?P<int:pid>)', Delete_Nurse, name='delete_nurse'),
    path('delete_nurse_list(?P<int:pid>)', Delete_Nurse_List, name='delete_nurse_list'),
]