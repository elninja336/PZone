from Parkzoneapp import views
from django.urls import path

urlpatterns = [
    # path('customer/',views.get_and_post),
    path('customers/',views.manage_customer),
    # path('customer/<int:id>',views.cusustomer_view)
]
