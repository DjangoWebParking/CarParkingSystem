"""CarParkingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.contrib.auth import views as auth_views  # khong su dung

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_dashboard/', views.admin_view, name='admin_dashboard'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # name to call at views
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('email_verification/', views.email_verification,
         name='success_message'),
    #    path('signup/', views.signup, name='signup'),
     #    path('signup/', views.signup_view1, name='signup'),
    #     path('signup/', views.signup, name='signup'),
    # path('pay/<int:pk>', views.Pay, name='pay'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('save_vehicle/', views.save_vehicle, name='save_vehicle'),
    path('vehicle/', views.Vehicle.as_view(), name='vehicle'),  # Hien thi 1 xe
    # path('users/', views.UserView.as_view(), name='users'),
    path('listvehicle/', views.ListVehicle.as_view(), name='listvehicle'),
    path('view_vehicle/<int:pk>',
         views.VehicleReadView.as_view(), name='view_vehicle'),
    # path('view_car/<int:pk>', views.CarReadView.as_view(), name='view_car'),
    # path('view_user/<int:pk>', views.UserReadView.as_view(), name='view_user'),
    path('update_vehicle/<int:pk>',
         views.VehicleUpdateView.as_view(), name='update_vehicle'),
    # path('update_car/<int:pk>', views.CarUpdateView.as_view(), name='update_car'),
    path('delete_vehicle/<int:pk>',
         views.VehicleDeleteView.as_view(), name='delete_vehicle'),

    path('cars/', views.CarList.as_view(), name='api_car_list'),
    path('cars/<int:pk>', views.CarDetailView.as_view(), name='api_car_detail'),
    path('car_list/', views.showCarList, name='car_list'),
    # path('car_list/<int:id_car>', views.car_detail,name='car_view'), #id_car
    # path('update_car/<int:id_car>', views.car_update,name='car_update'),
    # path('delete_car/<int:id_car>', views.car_delete,name='car_delete'),
    path('car_list/<int:pk>', views.CarDetailView.as_view(),
         name='car_view'),  # id_car
    path('create_car/', views.CarCreateView.as_view(), name='create_car'),
    path('update_car/<int:pk>', views.CarUpdateView.as_view(), name='car_update'),
    path('delete_car/<int:pk>', views.CarDeleteView.as_view(), name='car_delete'),

    path('customer_list/', views.showCustomerList, name='customer_list'),
    path('customer_list/<int:pk>', views.CustomerDetailView.as_view(),
         name='customer_view'),  # id_car
    path('create_car/', views.CustomerCreateView.as_view(), name='create_customer'),
    path('update_customer/<int:pk>',
         views.CustomerUpdateView.as_view(), name='customer_update'),
    path('delete_customer/<int:pk>',
         views.CustomerDeleteView.as_view(), name='customer_delete'),
    path('parking_slot/',
         views.showParkingLot, name='show_parking_lot'),
    path('create_parking_slot/',
         views.CreateParkingSlotView.as_view(), name='create_parking_lot'),

    # Parking Record
    path('parking_record/parking_record_list',
         views.ParkingRecordView.as_view(), name='parking_record_list'),
    path('parking_record/create_parking_record',
         views.CreateParkingRecordView.as_view(), name='create_parking_record'),
    path('parking_record/update_parking_record/<int:pk>',
         views.ParkingRecordUpdateView.as_view(), name='update_parking_record'),
    path('parking_record/delete_parking_record/<int:pk>',
         views.ParkingRecordDeleteView.as_view(), name='delete_parking_record'),
    path('parking_record_detail/<int:pk>/',
         views.ParkingRecordDetailView.as_view(), name='parking_record_detail'),
    path('parking-record/<int:pk>/',
         views.get_parking_record, name='get_parking_record'),
    path('show_home/', views.show_home, name='show_home'),
    path('exit/', views.exit, name='exit'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('email_verification/<str:token>',
         views.email_verification, name='email_verification'),
    path('success_message/', views.show_success_signup, name='success_message'),
    path('user_car_list', views.UserCarList.as_view(),name='user_car_list')

]
