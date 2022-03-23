from django.urls import path, include

from api_v1.views import get_csrf_token_view, add_view, subtract_view, multiply_view, divide_view

app_name = "api_v1"

calculation_urlpatterns = [
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide'),
]

urlpatterns = [
    path('get-csrf-token/', get_csrf_token_view),
    path('', include(calculation_urlpatterns))

]
