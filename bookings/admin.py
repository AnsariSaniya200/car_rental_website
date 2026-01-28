# from django.contrib import admin
# from .models import Booking

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):

#     list_display = (
#         'user',
#         'car',
#         'booking_period',
#         'created_at',
#         'total_price',
#         'status'
#     )

#     list_filter = ('status', 'created_at')
#     search_fields = ('user__username', 'car__name')
#     list_per_page = 10
#     ordering = ('-created_at',)

#     def booking_period(self, obj):
#         return f"{obj.start_date} {obj.start_time} → {obj.end_date} {obj.end_time}"

#     booking_period.short_description = "Booking Date & Time"

from django.contrib import admin
from .models import Car, Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'car',
        'start_date',
        'end_date',
        'status',
        'total_price',
        'can_cancel_admin',
    )

    def can_cancel_admin(self, obj):
        if obj.can_cancel:
            return "Yes"
        return "No"
    can_cancel_admin.short_description = "Can Cancel"

