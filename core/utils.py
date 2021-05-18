from user.dj_city import CITIES
from user.models import City, State


def create_location_date():
    '''Method to generate location data for DB first time'''

    state_count = State.objects.all().count()
    if(state_count < 30):
        for data in CITIES:
            state_name = data[0]
            cities = data[1]

            state_obj, _ = State.objects.get_or_create(name=state_name)

            for (_, city_name) in cities:
                City.objects.get_or_create(name=city_name, state=state_obj)
