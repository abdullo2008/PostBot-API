from django.http import JsonResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import TGUserModel
from .serializers import TGUserSerializer


class CreateTGUser(ListCreateAPIView):
    queryset = TGUserModel.objects.all()
    serializer_class = TGUserSerializer


class DeleteTGUser(RetrieveDestroyAPIView):
    queryset = TGUserModel.objects.all()
    serializer_class = TGUserSerializer
    lookup_field = 'tg_id'



def ListTGUser(request):
    model = TGUserModel.objects.all()
    context = {
        'tgusers': model
    }
    return render(request, 'index.html', context)
