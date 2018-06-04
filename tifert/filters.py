from django.contrib.auth.models import User
from tifert.models import Rj,Defaut_tabia,Photo

import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]

#####################################################""
class DefFilter(django_filters.FilterSet):
    joure = django_filters.NumberFilter(name='jour')
    class Meta:
        model = Defaut_tabia
        fields = ['defaut', 'jour',]
#####################################################""
class RjFilter(django_filters.FilterSet):
    date_year = django_filters.NumberFilter(name='date', lookup_expr='year')
    date_month = django_filters.NumberFilter(name='date', lookup_expr='month')
    date_day = django_filters.NumberFilter(name='date', lookup_expr='day')



    class Meta:
        model = Rj
        fields = ['date', 'starter','date_year','date_month','date_day',]
