from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from django.conf.urls import url

from reservation_manager import views

urlpatterns = [
    path('', views.ReservationManagerView.as_view(), name ="instr_reservation"),
    path('<instr_id>', views.ReservationManagerView.as_view(), name ="instr_reservation"),
    path('<instr_id>/settings', views.GetSettings),
    path('<instr_id>/dates/', views.GetReservations),
    path('<instr_id>/info', views.InstrInfoModal, name="instr_info_modal"),
    path('<instr_id>/delete-reservation/', views.DeleteReservation),
] 