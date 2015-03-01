from django.contrib import admin
from shows.models import ShowListing, Venue


class VenueInline(admin.StackedInline):
    model = Venue
    extra = 1


class ShowListingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['date_and_time','opener','ticket_url','other_info','sold_out']}),
        ('Venue', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(ShowListing)
admin.site.register(Venue)