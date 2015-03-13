from django.contrib import admin

from shows.models import ShowListing, Venue, Artist


@admin.register(ShowListing)
class ShowListingAdmin(admin.ModelAdmin):
    pass


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    pass


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

