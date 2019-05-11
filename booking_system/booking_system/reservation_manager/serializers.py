from rest_framework  import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('instrument_id','date','time_start','time_end')
        read_only_fields = ('user_id',)

