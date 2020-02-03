from django.template import RequestContext
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from .models import OurFocus, Partners, WhatWeDo, Manifesto, JoinUs, WorkShop


class DvgBaseIndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['focus_models'] = OurFocus.objects.all()
        context['partners_models'] = Partners.objects.all()

        return context


class DvgBaseWhatWeDoView(generic.TemplateView):
    template_name = 'whatwedo.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['whatwedo_models'] = WhatWeDo.objects.all()

        return context


class DvgBaseManifestoView(generic.TemplateView):
    template_name = 'manifesto.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manifesto_models'] = Manifesto.objects.all()

        return context


class DvgBaseJoinUsView(generic.TemplateView):
    template_name = 'joinus.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['joinus_models'] = JoinUs.objects.all()

        return context


class DvgBaseWorkShopView(generic.TemplateView):
    template_name = 'worskshop.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workshop_models'] = WorkShop.objects.all()

        return context


# def error_404(request):
#     data = {}
#     return render(request, '404a.html', data)

def error_404(request, exception):
    context = RequestContext(request)
    err_code = 404
    response = render_to_response('404a.html', {"code": err_code}, context)
    response.status_code = 404
    return response


