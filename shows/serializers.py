from django.forms import widgets
from rest_framework import serializers
from shows.models import Venue, ShowListing, Artist


class ShowListingSerializer(serializers.ModelSerializer):
	class Meta:
        model = ShowListing
        fields = ('id', 'title', 'datetime', 'formatted_datetime', 'formatted_location', 'ticket_url',
        	'ticket_type','ticket_status','on_sale_datetime','facebook_rsvp_url','description','artists','venue')


class VenueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Venue
        fields = ('name', 'city', 'region', 'country', 'latitude', 'longitude')


class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist		
        fields = ('name', 'image_url', 'thumb_url', 'facebook_tour_dates_url', 'mbid', 'upcoming_events_count')
