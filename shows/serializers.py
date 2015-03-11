from rest_framework import serializers

from shows.models import Venue, ShowListing, Artist


class ShowListingSerializer(serializers.ModelSerializer):
    artists = serializers.RelatedField
    venue = serializers.RelatedField
    class Meta:
        model = ShowListing


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist