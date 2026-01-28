from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from .models import Booking
from .forms import BookingForm
from cars.models import Car
from datetime import datetime, date, time


from math import ceil

from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from math import ceil
from .forms import BookingForm
from .models import Booking
from cars.models import Car
from datetime import datetime
from decimal import Decimal
from math import ceil
from datetime import datetime
from django.utils import timezone
from datetime import timedelta


def book_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    total_price = None  # Default to None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = car
            booking.user = request.user

            # Combine dates and times
            start_dt = datetime.combine(form.cleaned_data['start_date'], form.cleaned_data['start_time'])
            end_dt = datetime.combine(form.cleaned_data['end_date'], form.cleaned_data['end_time'])

            total_km = form.cleaned_data['total_km']  # HiddenInput or entered in form

            # Calculate days (400 km per day rule)
            max_km_per_day = Decimal('400')
            total_days = ceil(Decimal(total_km) / max_km_per_day)

            # Calculate price
            total_price = total_days * car.price_per_day + Decimal(total_km) * car.fare_per_km

            # 🔹 Round to 2 decimal places
            total_price = round(total_price, 2)

            if "check_price" in request.POST:
                # Show total price without saving
                return render(request, 'bookings/book_car.html', {
                    'form': form,
                    'car': car,
                    'total_price': total_price
                })

            # If "book_now" clicked, save booking
            booking.total_km = total_km
            booking.total_days = total_days
            booking.total_price = total_price
            booking.start_time = start_dt
            booking.end_time = end_dt
            booking.save()
            return redirect('bookings:booking_confirm', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'bookings/book_car.html', {
        'form': form,
        'car': car,
        'total_price': total_price
    })




def booking_confirm(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    max_km_per_day = Decimal('400')
    total_km = Decimal(str(booking.total_km))

    # days derived from KM rule
    total_days = ceil(total_km / max_km_per_day)

    booking.total_price = (
        Decimal(total_days) * booking.car.price_per_day +
        total_km * booking.car.fare_per_km
    )

    booking.save()

    return render(request, 'bookings/booking_confirm.html', {

        'booking': booking,
        'total_days': total_days,
        'car': booking.car
    })
  

    


@login_required
def bookings_index(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/bookings_index.html', {'bookings': bookings})


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # User / Admin permission
    if request.user != booking.user and not request.user.is_staff:
        messages.error(request, "You are not allowed to cancel this booking.")
        return redirect('bookings:bookings_index')

    # 24 hours rule
    if timezone.now() - booking.created_at > timedelta(hours=24):
        messages.error(request, "Cancellation allowed only within 24 hours.")
        return redirect('bookings:bookings_index')

    booking.is_cancelled = True
    booking.save()

    messages.success(request, "Booking cancelled successfully.")
    return redirect('bookings:bookings_index')

@login_required
def booking_success(request):
    return render(request, 'bookings/booking_success.html')

