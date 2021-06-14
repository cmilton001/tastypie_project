from django.http import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.resources import ModelResource

import talk
from talk.models import Talk


class MyModelResource(ModelResource):
    class Meta:
        queryset = Talk.objects.all()


class GetTalks(ListView):  # generic view
    template_name = 'get_talks.html'
    model = Talk
    context_object_name = 'get_talks'


class Insert(CreateView):
    model = Talk
    fields = ['id', 'first_name', 'last_name', 'speaker', 'venue', 'duration']
    template_name = 'insert.html'
    success_url = reverse_lazy('get_talks')



class Update(UpdateView):
    model = Talk
    fields = ['id', 'first_name', 'last_name', 'speaker', 'venue', 'duration']
    template_name = 'update.html'
    success_url = reverse_lazy('get_talks')


class Delete(DeleteView):
        template_name = 'delete.html'
        model = Talk
        context_object_name = 'delete'
        success_url = reverse_lazy('get_talks')
