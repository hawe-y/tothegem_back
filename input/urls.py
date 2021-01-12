from django.urls import path, re_path
from input import views

app_name = 'input'

urlpatterns = [
    # Example: /input/found_new/
    path('found_new/', views.found_input.as_view(), name='found_new'),
    # Example: /input/found_new/found_success
    path('found_success/', views.found_success.as_view(), name='found_success'),
    # Example: /input/lost_new/
    path('lost_new/', views.lost_input.as_view(),name='lost_new'),
    # Example: /input/lost_new/lost_success
    path('lost_success/', views.lost_success.as_view(), name='lost_success')
]