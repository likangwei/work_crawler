#coding=utf8
from django.shortcuts import render
from django.shortcuts import render_to_response
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


@login_required
def index(request):
    company_ids = set()
    for job in Job.objects.all():
        company_ids.add(job.companyId)

    companys = Company.objects.filter(cid__in=company_ids)
    data = []
    for company in companys:
        data.append({
            "id": company.id,
            "cid": company.cid,
            "name": company.name,
            "address": company.address,
            "companyShortName": company.companyShortName,
            "companyName": company.companyName,
            "financeStage": company.financeStage,
            "companySize": company.companySize,
            "briefPosition": company.briefPosition,
            "detailPosition": company.detailPosition,
            "lat": company.lat,
            "lng": company.lng,
            "score": company.score,
            "status": company.status,
            "jobCount": Job.objects.filter(companyId=company.cid).count()
        })
    print len(data)
    json_data = json.dumps(list(data), ensure_ascii=False)
    print json_data
    # render_to_response('add.html', {'form': form}, context_instance=RequestContext(request))
    return render(request, 'map.html', context={
        'company_list': json_data
    })