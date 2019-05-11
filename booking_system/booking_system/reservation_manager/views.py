from collections import OrderedDict
import json

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import JsonResponse

from utils import helperfuncs
from .models import CalenderSetting,Reservation,InstrumentCategory,Instrument
from django.contrib.auth.models import User
from datetime import datetime,date,time, timedelta


class ReservationManagerView(LoginRequiredMixin, View):

    template_name = "reservation_manager.html"
    pk_url_kwarg = "instr_id"

    def get(self, request, instr_id=''):
        instr_category_dict = OrderedDict()
        settings = CalenderSetting.objects.all().filter(active=True).values('number_of_days','number_of_sessions','time_interval','first_session_time')
        times = []
        month_colspan = settings[0]['number_of_days']

        for session in range(settings[0]['number_of_sessions']):
            times.append('{0:%H:%M}'.format((datetime.combine(date.today(), settings[0]['first_session_time']) + timedelta(minutes=(session*settings[0]['time_interval']))).time()))

        for instr_category in InstrumentCategory.objects.all().order_by('category'):
            instr_category_dict[instr_category.category] = Instrument.objects.filter(category=instr_category).values('instrument_id','instrument_name','under_maintenance')

        try:
            helperfuncs.ValidateUUID(instr_id)
            instr_ = Instrument.objects.filter(instrument_id=instr_id).values('category','instrument_name')[0]
            instr_cat = InstrumentCategory.objects.filter(id=instr_['category']).values('category')[0]
            instr_name = instr_cat['category'] + ': ' + instr_['instrument_name']
        except:
            instr_name = 'Please select an instrument'
            pass

        return render(request,'reservation_manager.html',context={'instr_cat_dict':instr_category_dict,
                                                            'instr_id':instr_id,
                                                            'instr_name':instr_name,
                                                            'month_colspan':month_colspan,
                                                            'number_of_days':range(settings[0]['number_of_days']), 
                                                            'times':times,
                                                            'settings':settings[0]})

    def post(self, request, instr_id=''):
        user = request.user.get_username()
        instrument = Instrument.objects.filter(instrument_id=instr_id)[0]
        date = request.POST.get('date')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        available = CheckReservationAvailability(request,instr_id,date,time_start,time_end)
        if available == True:
            Reservation.objects.create(user_id=request.user,instrument_id=instrument,date=date,time_start=time_start,time_end=time_end)
            json_serializer = helperfuncs.FieldsJSONSerializer()
            queryset = Reservation.objects.filter(user_id=request.user,instrument_id=instrument,date=date,time_start=time_start,time_end=time_end)
            serialized_q = json_serializer.serialize(queryset, fields=['user_id','date','time_start','time_end'])
            return JsonResponse(serialized_q, safe=False)
        else:
            return JsonResponse('False', safe=False)


def InstrInfoModal(request, instr_id=''):
    instrument = get_object_or_404(Instrument, instrument_id=instr_id)
    return render(request, "instr_info_modal.html", context={"instrument": instrument})

def GetSettings(request,instr_id=''):
    settings = CalenderSetting.objects.filter(active=True)
    print(settings)
    json_serializer = helperfuncs.FieldsJSONSerializer()
    serialized_settings = json_serializer.serialize(settings,fields=['number_of_days','first_session_time','time_interval','number_of_sessions'])
    return JsonResponse(serialized_settings,safe=False)

def GetReservations(request,instr_id=''):
    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')
    helperfuncs.ValidateUUID(instr_id)
    queryset = Reservation.objects.filter(instrument_id=instr_id,date__range=[startdate,enddate])
    json_serializer = helperfuncs.FieldsJSONSerializer()
    serialized_q = json_serializer.serialize(queryset, fields=['user_id','date','time_start','time_end'])
    return JsonResponse(serialized_q, safe=False)

def CheckUser(request, reservation_id):
    reservation_user = Reservation.objects.filter(reservation_id=reservation_id).values('user_id')
    if reservation_user[0]['user_id'] == request.user.get_username():
        authenticated = True
    else:
        authenticated = False
    return authenticated

def DeleteReservation(request, instr_id=''):

    reservation_id = request.POST.get('reservation_id')
    reservation_user = Reservation.objects.filter(reservation_id=reservation_id).values('user_id')
    user_authenticated = CheckUser(request, reservation_id)
    
    if user_authenticated:
        Reservation.objects.filter(reservation_id=reservation_id).delete()
        response = reservation_id
    else:
        response = 'You do not have permission to delete this reservation'
    
    return JsonResponse(response , safe=False)
    
def CheckReservationAvailability(request,instr_id,date, time_start, time_end):
    reservations = Reservation.objects.filter(instrument_id=instr_id,date=date).values('time_start','time_end')
    for reservation in reservations:
        if reservation['time_start'] <= datetime.time(datetime.strptime(time_start, '%H:%M')) <= (reservation['time_end']):
            return False
        elif reservation['time_start'] <= datetime.time(datetime.strptime(time_end, '%H:%M')) <= (reservation['time_end']):
            return False
        elif datetime.time(datetime.strptime(time_start, '%H:%M')) < reservation['time_start'] < datetime.time(datetime.strptime(time_end, '%H:%M')):
            return False
        else:
            return True
    return True