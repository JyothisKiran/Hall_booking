from django.urls import path
from .views import success_page,hall_booked_status_view,booking_cancel_view,booking_update_view,meeting_create_view

urlpatterns = [
    path('booking/',meeting_create_view, name='hallbooking'),
    path('sucess/',success_page,name ='success'),
    path('bookinglist/',hall_booked_status_view,name ='bookinglist'),
    path('bookingupdate/<int:pk>/',booking_update_view, name='bookingupdate'),
    path('bookingdelete/<int:pk>/',booking_cancel_view,name ='bookingdelete'),
]