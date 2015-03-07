from django.contrib import admin
from shows.models import ShowListing, Venue, Artist

admin.site.register(ShowListing)
admin.site.register(Venue)
admin.site.register(Artist)
