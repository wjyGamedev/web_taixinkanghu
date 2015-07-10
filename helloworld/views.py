from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from __future__ import unicode_literals

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
        'head_title': u'Django Bookmarks',
        'page_title': u'Welcome to Django Bookmarks',
        'page_body': u'Where you can store and share bookmarks!'
    })
    output = template.render(variables)
    return HttpResponse(output)


def hospital_list(request):
    import json

    response_data = {}
    response_data['1'] = u'��������ҽԺ'
    response_data['2'] = u'����ţ��ҽԺ'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


