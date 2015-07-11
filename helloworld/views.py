# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

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

    request.get_full_path()
    response_data = [{"id":1,"name":"北京朝阳医院"},{"id":2,"name":"北京牛街医院"}]
    return HttpResponse(json.dumps(response_data), content_type="application/json")


