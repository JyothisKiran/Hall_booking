from django.shortcuts import render,redirect
from .forms import HallBookingForm
from django.views.generic import FormView
from .models import Meeting
from django.shortcuts import get_object_or_404,HttpResponse

# Create your views here.


def meeting_create_view(request):
    if request.method == 'POST':
        form = HallBookingForm(request.POST)
        if form.is_valid():
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            room = form.cleaned_data['room']
            team = form.cleaned_data['team_name']
            date = form.cleaned_data['date']

            if is_room_available(start_time, end_time, room,date) and (start_time <end_time):
                Meeting.objects.create(start_time=start_time, end_time=end_time, room=room,team_name=team,date = date)
                form = HallBookingForm()
                return render (request,'sucess.html',{'start_time':start_time,'end_time':end_time,'room':room, 'date':date ,'team':team })
            else:
                error_message = 'The room is not available for the selected time frame.'
                return render(request, 'hallbook.html', {'form': form, 'error_message': error_message})
    else:
        form = HallBookingForm()
    
    return render(request, 'hallbook.html', {'form': form})


def is_room_available(start_time, end_time, room, date):
    conflicting_bookings = Meeting.objects.filter(room=room, start_time__lte=end_time, end_time__gte=start_time, date=date)
    return not conflicting_bookings.exists()




def hall_booked_status_view(request):
    bookings = Meeting.objects.all()
    return render (request, 'booking_status.html',{'bookings':bookings})

def booking_cancel_view(request,pk):
    booking = Meeting.objects.get(pk =pk)
    if booking:
        booking.delete()
        #return redirect('sucess')
    return render (request,'booking_delete.html')


def booking_update_view(request,pk):
    booking = Meeting.objects.get(pk =pk)
    form = HallBookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        return redirect('sucess')
    return render (request,'hallbook.html',{'form':form} )


def success_page(request):
    return render (request,'sucess.html')


