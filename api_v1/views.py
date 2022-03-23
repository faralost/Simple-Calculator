import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse

from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('only GET requests are allowed!')


def add_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if isinstance(data['A'], int) and isinstance(data['B'], int):
            response = {'answer': data['A'] + data['B']}
            return JsonResponse(response)
        else:
            response = {'error': 'Please enter integer numbers!'}
            return JsonResponse(response)
    return HttpResponseNotAllowed('only POST requests are allowed!')


def subtract_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if isinstance(data['A'], int) and isinstance(data['B'], int):
            response = {'answer': data['A'] - data['B']}
            return JsonResponse(response)
        else:
            response = {'error': 'Please enter integer numbers!'}
            return JsonResponse(response)
    return HttpResponseNotAllowed('only POST requests are allowed!')


def multiply_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if isinstance(data['A'], int) and isinstance(data['B'], int):
            response = {'answer': data['A'] * data['B']}
            return JsonResponse(response)
        else:
            response = {'error': 'Please enter integer numbers!'}
            return JsonResponse(response)
    return HttpResponseNotAllowed('only POST requests are allowed!')


def divide_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if isinstance(data['A'], int) and isinstance(data['B'], int):
            try:
                response = {'answer': data['A'] / data['B']}
            except ZeroDivisionError:
                response = {'error': 'Division by zero!'}
            return JsonResponse(response)
        else:
            response = {'error': 'Please enter integer numbers!'}
            return JsonResponse(response)
    return HttpResponseNotAllowed('only POST requests are allowed!')
