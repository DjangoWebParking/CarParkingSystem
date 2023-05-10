from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render

from .models import Customer, User
# from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.urls import path, include


from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .forms import CustomerForm, UserForm, CarForm, CarUpdateForm
from .forms import UpdateParkingRecordForm, ParkingRecordDetailForm

from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.conf import settings
import os
from .models import Customer, User, ParkingSlot, Car, ParkingRecord
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from datetime import datetime, date
from django.core.exceptions import ValidationError
from . import models
import operator
import itertools
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa  # Tao pdf hoa don
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CarSerializer

from .forms import CreateParkingRecordForm, MyRegistrationForm
from .forms import EmailVerificationForm
import smtplib
from django.views.generic import ListView, CreateView, UpdateView, FormView

from django.views import View
from django.core.mail import send_mail
# Create your views here.

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)


def show_signup(request):
    return render(request, 'home/register.html')


# class MyRegistrationView(RegistrationView):
#     form_class = MyRegistrationForm
#     template_name = 'myapp/register.html'
#     success_url = '/thanks/'


# def signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password1 = request.POST.get('password')
#         password2 = request.POST.get('confirm_password')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email đã được sử dụng!')
#             return redirect('view_signup')

#         if password1 == password2:
#             user = User.objects.create_user(
#                 email=email,
#                 username=username,
#                 password=password1,
#             )
#             user.save()
#             # group = Group.objects.get(name='Customer')
#             # user.groups.add(group)
#             # Chuyển hướng đến trang thông báo đăng ký thành công
#             return redirect('login')
#         else:
#             # Hiển thị thông báo lỗi nếu mật khẩu không trùng khớp
#             # return render(request, 'view_signup', {'error': 'Mật khẩu không trùng khớp!'})
#             messages.error(request,  'Mật khẩu không trùng khớp!')
#             return redirect('signup')
#     else:
#         # Hiển thị form đăng ký
#         return render(request, 'home/signup.html')


# def send_activation_email(user):
#     subject = 'Activate your account'
#     message = render_to_string('activation_email.html', {
#         'user': user,
#     })
#     plain_message = strip_tags(message)
#     from_email = 'your_email@gmail.com'
#     recipient_list = [user.email]
#     send_mail(subject, plain_message, from_email,
#               recipient_list, html_message=message)
# from django.http import HttpResponseBadRequest
class SignupView(FormView):
    model = get_user_model()
    template_name = 'home/register.html'
    form_class = MyRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # UserModel = get_user_model()
        # # user = UserModel.objects.create_user(**form.cleaned_data)
        # # user.is_active = False
        # # user.save()
        # # Gửi email xác nhận
        # send_email_verification(user)
        return self.form_valid(form)
        

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            email = request.POST.get('email')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            print(password1, password2)
            user = User.objects.create_user(
                email=email,
                username=username,
                password=password1,
            )
            user.is_active = False
            user.save()
            send_email_verification(user)
            # send_mail(
            #     'Activate Email Form',
            #     'Thời gian để kích hoạt là 5phuts',
            #     'settings.EMAIL_HOST_USER',
            #     [user.email,'letrongbach02@gmail.com','benphantom102@gmail.com'],
            #     fail_silently=False
            # )
            print("valid")
            return redirect('success_message')
        else:
            print("invalid")
            return self.form_invalid(form)

    # def post(self,request):
    #     email = request.POST.get('email')
    #     username = request.POST.get('username')
    #     password1 = request.POST.get('password')
    #     password2 = request.POST.get('confirm_password')

    #     if User.objects.filter(email=email).exists():
    #         messages.error(request, 'Email đã được sử dụng!')
    #         return redirect('signup')

    #     if password1 == password2:
    #         user = User.objects.create_user(
    #             email=email,
    #             username=username,
    #             password=password1,
    #         )
    #         user.is_active = False
    #         user.save()
    #         send_email_verification(user)
    #         # send_mail(
    #         #     'Activate Email Form',
    #         #     'Thời gian để kích hoạt là 5phuts',
    #         #     'settings.EMAIL_HOST_USER',
    #         #     [user.email,'letrongbach02@gmail.com','benphantom102@gmail.com'],
    #         #     fail_silently=False
    #         # )

    #         # Chuyển hướng đến trang thông báo đăng ký thành công
    #         return redirect('email_notification')
    #     else:
    #         # Hiển thị thông báo lỗi nếu mật khẩu không trùng khớp
    #         # return render(request, 'view_signup', {'error': 'Mật khẩu không trùng khớp!'})
    #         messages.error(request,  'Mật khẩu không trùng khớp!')
    #         return redirect('signup')


def send_email_verification(user):
    from_email = 'nhom9qlda2223@gmail.com'  # nhập email của bạn vào đây
    to_email = user.email
    token = user.token
    # Gửi email với token xác nhận
    message = 'Click link below to verify your email:\n\n' + \
        'http://localhost:8000/email_verification/' + str(token)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        # nhập mật khẩu email của bạn vào đây
        smtp.login(from_email, 'zpqxzpdcbzqgxefk')
        smtp.sendmail(from_email, to_email, message)


def email_verification(request):
    form = EmailVerificationForm(request.GET)
    if form.is_valid():
        token = form.cleaned_data['token']
        print(token)
        user = User.objects.get(token=token)
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'home/email_verification.html', {'form': form})


def email_notification(request):
    return render(request, 'home/email_notification.html')


def home(request):
    return render(request, 'home/home.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'home/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_admin or user.is_superuser:
                return redirect('dashboard')
            elif user.is_customer:
                return redirect('show_home')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Wrong Username or Password')
            return redirect('home')


def signup_view1(request):
    return render(request, "home/register.html")


def dashboard(request):
    return render(request, 'dashboard.html')


# def logout(request):
#     response = logout(request)
#     response.delete_cookie("my_cookie")
#     return response

def is_admin(user):
    return user.groups.filter(name='Admin').exists()


@user_passes_test(is_admin)
def admin_view(request):
    # Code xử lý cho trang quản trị ở đây
    return render(request, 'admin_dashboard.html')


def add_vehicle(request):
    choice = ['1', '0', 10000, 15000, 'Accomodation Fee', 'Verified All Spare']
    choice = {'choice': choice}
    return render(request, 'add_vehicle.html', choice)


def save_vehicle(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        card_number = request.POST['card_number']
        car_model = request.POST['car_model']
        car_color = request.POST['car_color']
        phone_number = request.POST['phone_number']
        comment = request.POST['comment']
        device = request.POST['device']
        cost_per_day = request.POST['cost_per_day']
        register_name = request.POST['register_name']
        current_time = datetime.now()
        date_time = current_time.strftime("%Y,%m,%d")

        a = Customer(first_name=first_name, last_name=last_name, card_number=card_number, car_model=car_model, car_color=car_color,
                     reg_date=date_time, register_name=register_name, comment=comment, cost_per_day=cost_per_day, device=device)
        a.save()
        messages.success(request, 'Vehicle Registered Successfully')
        return redirect('vehicle')


class ListVehicle(ListView):
    model = Customer
    template_name = 'vehicles.html'
    context_object_name = 'customers'
    paginate_by = 2

    def get_queryset(self):
        return Customer.objects.filter(is_payed="True")


# class UserView(ListView):
#     model = User
#     template_name = 'list_user.html'
#     context_object_name = 'users'
#     paginate_by = 5

#     def get_queryset(self):
#         return User.objects.order_by('-id')


class Vehicle(ListView):
    model = Customer
    template_name = 'list_vehicle.html'
    context_object_name = 'customers'
    paginate_by = 2

    def get_queryset(self):
        return Customer.objects.filter(is_payed="False")


# Template call in vehicles
class VehicleReadView(BSModalReadView):
    model = Customer
    template_name = 'view_vehicle.html'


class VehicleUpdateView(BSModalUpdateView):
    model = Customer
    template_name = 'update_vehicle.html'
    form_class = CustomerForm
    success_message = 'Vehicle update succesfully'
    success_url = reverse_lazy('vehicle')


class VehicleDeleteView(BSModalDeleteView):
    model = Customer
    template_name = 'delete_vehicle.html'
    form_class = CustomerForm
    success_message = 'Vehicle delete succesfully'
    success_url = reverse_lazy('vehicle')


# class MyParkingLot(BSModalReadView):
#     model = ParkingLot
#     template_name = 'my_parkinglot.html'


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # template = ''


def showCarList(request):
    cars = Car.objects.all()
    # print(cars)
    context = {'cars': cars}
    return render(request, 'cars/car_list.html', context)


def car_update(request, id_car):
    car = get_object_or_404(Car, pk=id_car)
    print('car_update', car)
    return render(request, 'cars/car_update.html', {'my_car': car})


def car_delete(request, id_car):
    car = get_object_or_404(Car, pk=id_car)
    return render(request, 'cars/car_delete.html', {'my_car': car})


def car_detail(request, id_car):
    # car = Car.objects.filter(id=id_car)
    car = get_object_or_404(Car, pk=id_car)
    return render(request, 'cars/car_view.html', {'my_car': car})


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CreateCarView(generics.CreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get(self, request):
        form = CarForm()
        return render(request, 'create_car.html', {'form': form})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Template call in vehicles


class CarCreateView(BSModalCreateView):
    template_name = 'cars/create_car.html'
    form_class = CarForm
    success_message = 'Success: Car was created.'
    success_url = reverse_lazy('car_list')


class CarDetailView(BSModalReadView):
    model = Car
    template_name = 'cars/car_view.html'
    form_class = CarForm


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'cars/car_update.html'
    form_class = CarForm
    success_message = 'Car update succesfully'
    success_url = reverse_lazy('car_list')

    def get(self, request, *args, **kwargs):
        car = self.get_object()
        context = {'form': CarUpdateForm(instance=car), 'car': car}
        return render(request, self.template_name, context)

    # def get_success_url(self):
    #     return reverse_lazy('car_list',kwargs={'pk': self.get_object().id})


class CarDeleteView(BSModalDeleteView):
    model = Car
    template_name = 'cars/car_delete.html'
    form_class = CarForm
    success_message = 'Car delete succesfully'
    success_url = reverse_lazy('car_list')


def showCustomerList(request):
    customers = Customer.objects.all()
    # print(customers)
    context = {'customers': customers}
    return render(request, 'customers/customer_list.html', context)


class CustomerCreateView(BSModalCreateView):
    template_name = 'customers/create_customer.html'
    form_class = CustomerForm
    success_message = 'Success: Customer was created.'
    success_url = reverse_lazy('customer_list')


class CustomerDetailView(BSModalReadView):
    model = Customer
    template_name = 'customers/customer_view.html'
    form_class = CustomerForm


class CustomerUpdateView(BSModalUpdateView):
    model = Customer
    template_name = 'customers/customer_update.html'
    form_class = CustomerForm
    success_message = 'Customer update succesfully'
    success_url = reverse_lazy('customer_list')
    # def get_success_url(self):
    #     return reverse_lazy('car_list',kwargs={'pk': self.get_object().id})


class CustomerDeleteView(BSModalDeleteView):
    model = Customer
    template_name = 'customers/customer_delete.html'
    form_class = CustomerForm
    success_message = 'Customer delete succesfully'
    success_url = reverse_lazy('customer_list')


def get_parking_record(request, pk):
    try:
        parking_slot = ParkingSlot.objects.get(pk=pk)
        if parking_slot.is_available:
            return JsonResponse({'error': 'This parking slot is empty.'})
        else:
            parking_record = parking_slot.parkingrecord_set.get(exit_time=None)
            data = {
                'parking_record_id': parking_record.id,
                'car_number': parking_record.car_number,
                'entry_time': parking_record.entry_time.strftime('%Y-%m-%d %H:%M:%S'),
                'cost_per_day': parking_slot.cost_per_day,
            }
            return JsonResponse(data)
    except ParkingSlot.DoesNotExist:
        return JsonResponse({'error': 'This parking slot does not exist.'})


def showParkingLot(request):
    parkingslots = ParkingSlot.objects.all()
    context = {'parking_slots': parkingslots}
    return render(request, 'parkingslots/parking_slot.html', context)

# def save_parking_record(request):
#     # if request =="POST":


class CreateParkingSlotView(CreateView):
    template_name = 'create_parking_slot_view.html'
    form_class = CreateParkingRecordForm
    success_message = 'Create Parking Slot succesfully'
    success_url = 'parking_slot.html'


# Create Parking Record View


class ParkingRecordView(ListView):
    model = ParkingRecord
    template_name = 'parkingrecord/parking_record_list.html'
    context_object_name = 'parkingrecords'
    paginate_by = 5


class CreateParkingRecordView(CreateView):
    cars = Car.objects.all()
    # parking_slots = ParkingSlot.objects.filter(is_available=True)
    template_name = 'parkingrecord/create_parking_record.html'
    form_class = CreateParkingRecordForm
    success_url = reverse_lazy('parking_record_list')

    def get(self, request):
        available_slots = ParkingSlot.objects.filter(is_available=True)
        context = {'cars': self.cars, 'parking_slots': available_slots}
        return render(request, self.template_name, context)
    # def get ----

    def post(self, request):
        # Lấy thông tin car và parking_slot theo id
        car_id = request.POST.get('car_id')
        parking_slot_id = request.POST.get('parking_slot_id')
        car = Car.objects.get(id=car_id)
        parking_slot = ParkingSlot.objects.get(id=parking_slot_id)

        # Set trạng thái của parking_slot là không còn trống
        parking_slot.is_available = False
        print("OK")
        parking_slot.save()

        # Tạo mới parking record cho car và parking_slot đã chọn
        parking_record = ParkingRecord.objects.create(
            parking_slot=parking_slot,
            car_number=car.license_plate,
            entry_time=timezone.now(),
            car=car,
            total_cost=0,
            is_paid=False
        )

        return redirect('parking_record_list')

    def form_valid(self, form):
        car = form.cleaned_data['car']
        parking_slot = form.cleaned_data['parking_slot']

        # Set trạng thái của parking_slot là không còn trống
        parking_slot.is_available = False
        parking_slot.save()

        # Tạo mới parking record cho car và parking_slot đã chọn
        parking_record = ParkingRecord.objects.create(
            parking_slot=parking_slot,
            car_number=car.license_plate,
            entry_time=timezone.now(),
            car=car,
            total_cost=0,
            is_paid=False
        )

        return super().form_valid(form)


class ParkingRecordDetailView(BSModalReadView):
    model = ParkingRecord
    template_name = 'parkingrecord/parking_record_detail.html'
    form_class = ParkingRecordDetailForm

    def get_object(self, queryset=None):
        return ParkingRecord.objects.get(id=self.kwargs['pk'])

    def render_to_response(self, context, **response_kwargs):
        html = render_to_string(self.template_name, context=context)
        return JsonResponse({'html': html})


class ParkingRecordUpdateView(BSModalUpdateView):
    model = ParkingRecord
    template_name = 'parkingrecord/update_parking_record.html'
    form_class = UpdateParkingRecordForm
    success_message = 'Parking record update succesfully'
    success_url = reverse_lazy('parking_record_list')

    # def get(self, request):
    #     print("Hello")
    #     return render(request, self.template_name)


class ParkingRecordDeleteView(BSModalDeleteView):
    model = ParkingRecord
    template_name = 'parkingrecord/delete_parking_record.html'
    # form_class = ParkingRecordDetailForm
    success_message = 'Parking record delete succesfully'
    success_url = reverse_lazy('parking_record_list')

    def delete(self, request, *args, **kwargs):
        # Lấy bản ghi ParkingRecord cần xóa
        parking_record = self.get_object()
        print(parking_record)
        # Set is_available của parking_slot của ParkingRecord thành true
        parking_record.parking_slot.is_available = True
        parking_record.parking_slot.save()
        # Xóa bản ghi ParkingRecord
        return super().delete(request, *args, **kwargs)


def show_home(request):
    slots = ParkingSlot.objects.all()
    return render(request, 'parking_overview.html', {'slots': slots})


def reserse_slot(request, pk):
    ps = ParkingSlot.objects.filter(id=pk)

    return redirect('show_home')


def exit(request):
    if request.method == 'POST':
        parking_slot_pk = request.POST.get('parking_slot_pk')
        # Do something with the parking_slot_pk, for example:
        parking_slot = ParkingSlot.objects.get(pk=parking_slot_pk)
        parking_slot.is_available = True
        parking_slot.exit_time = timezone.now()
        parking_slot.save()
        messages.success(request, 'Cập nhật trạng thái chỗ đậu xe thành công.')
    return redirect(reverse('show_parking_lot'))

    # class CarReadView(BSModalReadView):
    #     model = Customer
    #     template_name = 'view_vehicle2.html'

    # class UserReadView(BSModalReadView):
    #     model = User
    #     template_name = 'view_user.html'

    # class CarUpdateView(BSModalUpdateView):
    #     model = Customer
    #     template_name = 'update_vehicle2.html'
    #     form_class = CustomerForm
    #     success_url = reverse_lazy('listvehicle')

    # class CarDeleteView(BSModalDeleteView):
    #     model = Customer
    #     template_name = 'delete_vehicle2.html'
    #     form_class = CustomerForm
    #     success_url = reverse_lazy('listvehicle')

    # def Pay(request, pk):
    #     Customer.objects.filter(id = pk).update(exit_date = timezone.now())
    #     Customer.objects.filter(id = pk).update(is_payed = "True")
    #     reg_date = Customer.objects.values_list('reg_date').filter(id = pk)
    #     exit_date = Customer.objects.values_list('exit_date').filter(id = pk)

    #     a = str(reg_date)
    #     b = str(exit_date)

    #     x = a[30:59]
    #     y = b[30:59]

    #     date_time_str = x
    #     date_time_str2 = y

    #     myTime = datetime.strptime(date_time_str, "%Y, %m, %d, %H, %M, %S, %f")
    #     myTime2 = datetime.strptime(date_time_str2, "%Y, %m, %d, %H, %M, %S, %f")

    #     myFormat = ("%Y,%m,%d")
    #     new_reg_date = myTime.strftime(myFormat)
    #     new_exit_date = myTime2.strftime(myFormat)

    #     d2 = myTime2.date()
    #     d1 = myTime.date()

    #     delta = d2 -d1
    #     mo = delta.days

    #     if mo == 0:
    #         mo =1
    #     else:
    #         mo = mo

    #     Customer.objects.filter(id = pk).update(days_spent = mo)
    #     cost_per_day = Customer.objects.values_list('cost_per_day').filter(id = pk)
    #     days_spent = Customer.objects.values_list('days_spent').filter(id = pk)

    #     cpd = str(cost_per_day)
    #     cpd = cpd[12:-7]

    #     if cpd == str(15):
    #        cost_per_day = 15000
    #        total_cost = cost_per_day * mo
    #        Customer.objects.filter(id = pk).update(total_cost = total_cost)
    #        messages.success(request, 'Payment Was Finished Successfully')
    #        return redirect('listvehicle')
    #     else:
    #         cost_per_day = 10000
    #         total_cost = cost_per_day * mo
    #         Customer.objects.filter(id = pk).update(total_cost = total_cost)
    #         messages.success(request, 'Payment Was Finished Successfully')
    #         return redirect('listvehicle')

    # def render_to_pdf(template_src, context_dict={}):
    #     template = get_template(template_src)
    #     html  = template.render(context_dict)
    #     result = BytesIO()
    #     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    #     if not pdf.err:
    #         return HttpResponse(result.getvalue(), content_type='application/pdf')
    #     return None

    # class GeneratePdf(ListView):
    #     def get(self, request, pk, *args, **kwargs):
    #         #info = Customer.objects.filter(id=pk)
    #         infos = Customer.objects.filter(id=pk).values('id','first_name','last_name','total_cost','days_spent', 'reg_date', 'exit_date', 'card_number')
    #         print(infos)
    #         context = {
    #         "data": {
    #             'today': 'Today',
    #              'amount': 39.99,
    #             'customer_name': 'Cooper Mann',
    #             'order_id': 1233434,
    #             'location': 'MoTech Tower, Ilala',
    #             'address': 'P.Box 122 Dar Es Salaam',
    #             'email': 'info@motechapp.com',
    #         },
    #         "infos": infos,
    #         }

    #         pdf = render_to_pdf('invoice.html', context)
    #         return HttpResponse(pdf, content_type='application/pdf')

    # class GeneratePDF(LoginRequiredMixin,ListView):
    #     def get(self, request, *args, **kwargs):
    #         template = get_template('invoice.html')
    #         context = {
    #             "invoice_id": 123,
    #             "customer_name": "John Cooper",
    #             "amount": 1399.99,
    #             "today": "Today",
    #         }
    #         html = template.render(context)
    #         pdf = render_to_pdf('invoice.html', context)
    #         if pdf:
    #             response = HttpResponse(pdf, content_type='application/pdf')
    #             filename = "Invoice_%s.pdf" %("12341231")
    #             content = "inline; filename='%s'" %(filename)
    #             download = request.GET.get("download")
    #             if download:
    #                 content = "attachment; filename='%s'" %(filename)
    #             response['Content-Disposition'] = content
    #             return response
    #         return HttpResponse("Not found")

    # class DeleteUser(BSModalDeleteView):
    #     model = User
    #     template_name = 'dashboard/delete_user.html'
    #     success_message = 'Success: Data was deleted.'
    #     success_url = reverse_lazy('users')

    # def create(request):
    #     choice = ['1', '0', 5000, 10000, 15000, 'Register', 'Admin', 'Cashier']
    #     choice = {'choice': choice}
    #     if request.method == 'POST':
    #             first_name=request.POST['first_name']
    #             last_name=request.POST['last_name']
    #             username=request.POST['username']
    #             userType=request.POST['userType']
    #             email=request.POST['email']
    #             password=request.POST['password']
    #             password = make_password(password)
    #             print("User Type")
    #             print(userType)
    #             if userType == "Register":
    #                 a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_register=True)
    #                 a.save()
    #                 messages.success(request, 'Member was created successfully!')
    #                 return redirect('users')
    #             elif userType == "Cashier":
    #                 a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_cashier=True)
    #                 a.save()
    #                 messages.success(request, 'Member was created successfully!')
    #                 return redirect('users')
    #             elif userType == "Admin":
    #                 a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_admin=True)
    #                 a.save()
    #                 messages.success(request, 'Member was created successfully!')
    #                 return redirect('users')
    #             else:
    #                 messages.success(request, 'Member was not created')
    #                 return redirect('users')
    #     else:
    #         choice = ['1', '0', 5000, 10000, 15000, 'Register', 'Admin', 'Cashier']
    #         choice = {'choice': choice}
    #         return render(request, 'add.html', choice)
