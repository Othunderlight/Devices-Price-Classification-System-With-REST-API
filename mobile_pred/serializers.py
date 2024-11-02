from rest_framework import serializers
from .models import MobilePhone

class MobilePhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePhone
        fields = [
            'id',
            'battery_power',
            'blue',
            'clock_speed',
            'dual_sim',
            'fc',
            'four_g',
            'int_memory',
            'm_dep',
            'mobile_wt',
            'n_cores',
            'pc',
            'px_height',
            'px_width',
            'ram',
            'sc_h',
            'sc_w',
            'talk_time',
            'three_g',
            'touch_screen',
            'wifi',
            'price_range'
        ] 