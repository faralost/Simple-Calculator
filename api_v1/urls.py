from django.urls import path, include

from api_v1.views import get_csrf_token_view, add_view, subtract_view, multiply_view, divide_view

app_name = "api_v1"

calculation_urlpatterns = [
    path('add/', add_view),
    path('subtract/', subtract_view),
    path('multiply/', multiply_view),
    path('divide/', divide_view),
]

urlpatterns = [
    path('get-csrf-token/', get_csrf_token_view),
    path('', include(calculation_urlpatterns))
]
