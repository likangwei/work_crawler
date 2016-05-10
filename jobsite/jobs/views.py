#coding=utf8
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.response import Response
from serializers import JobSerializer
from serializers import CompanySerializer
from models import Job
from models import Company
from rest_framework import permissions
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json

@login_required(login_url="/admin")
def index(request):
    return render(request, 'index.html')


class JobViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = self.queryset
        filter = self.request.GET.get('filter', '{}')
        filter = json.loads(filter)
        queryset = queryset.filter(**filter)
        return queryset


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = self.queryset
        filter = self.request.GET.get('filter', '{}')
        filter = json.loads(filter)
        queryset = queryset.filter(**filter)
        return queryset


def index(request):
    return HttpResponse(str(request.user))