from covid.forms import CovidUserDetailForm, CovidUserForm
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

    def get(self, request, *args, **kwargs):
        covid_user_form = CovidUserForm(initial={})
        covid_user__details_form = CovidUserDetailForm(initial={})

        return Response({
            'covid_user_form': covid_user_form,
            'covid_user_details_form': covid_user__details_form,
        }, status=status.HTTP_200_OK)
