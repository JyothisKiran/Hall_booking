from django import forms
from .models import Meeting

class HallBookingForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(format='%d/%m/%Y'),
    )

    class Meta:
        model = Meeting
        fields = "__all__"
        



# class RoomBookingForm(forms.ModelForm):
#     date = forms.DateField(
#         input_formats=['%d/%m/%Y', '%Y-%m-%d'],
#         widget=forms.DateInput(format='%d/%m/%Y'),
#     )

#     class Meta:
#         model = RoomBooking
#         fields = '__all__'