from rest_framework import response
from user.models import City, State
from covid.forms import CovidUserDetailForm, CovidUserForm, LocalityForm
from rest_framework import status
# from rest_framework.authentication import BasicAuthentication
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from core.api.base import BaseAPIView


class CovidHomeAPIView(BaseAPIView):
    '''
    Dashboard to enroll mentor (using mobile/email) to selected course
    '''
    http_method_names = ['post', 'get']
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'covid/home.html'
    # queryset = Mentor.objects.all()
    # authentication_classes = (BasicAuthentication,
    #                           JSONWebTokenAuthentication)
    # permission_classes = [IsAuthenticated]

    @staticmethod
    def get_locality_data():
        data = {}
        state_objs = State.objects.prefetch_related('city_state').all()
        for state_obj in state_objs:
            data[state_obj.id] = {}
            city_objs = state_obj.city_state.order_by('name')
            city_id_list = list(city_objs.values_list('id', flat=True))
            city_name_list = list(city_objs.values_list('name', flat=True))

            data[state_obj.id] = {
                "names": city_name_list,
                "ids": city_id_list
            }

        print(data)
        return data

    def get(self, request, *args, **kwargs):
        covid_user_form = CovidUserForm(initial={})
        covid_user__details_form = CovidUserDetailForm(initial={})
        locality_form = LocalityForm(initial={})

        return Response({
            'covid_user_form': covid_user_form,
            'covid_user_details_form': covid_user__details_form,
            'locality_form': locality_form,
            'locality_data': self.get_locality_data(),
        }, status=status.HTTP_200_OK)
