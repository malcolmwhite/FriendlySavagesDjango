from django.forms import widgets
from rest_framework import serializers
from shows.models import Venue, ShowListing, Artist


class ShowListingSerializer(serializers.Serializer):
    artists = serializers.RelatedField(many=True, read_only=True)
    venue = serializers.RelatedField(many=True, read_only=True)
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=400)
    datetime = serializers.DateTimeField('date and time of show')
    formatted_datetime = serializers.CharField(max_length=200)
    formatted_location = serializers.CharField(max_length=40)
    ticket_url= serializers.URLField()
    ticket_type = serializers.CharField(max_length=40)
    ticket_status = serializers.CharField(max_length=40)
    on_sale_datetime = serializers.DateTimeField()
    facebook_rsvp_url= serializers.URLField()
    description = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return ShowListing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)


class VenueSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    city = serializers.CharField(max_length=20)
    region = serializers.CharField(max_length=20)
    country = serializers.CharField(max_length=20)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    def create(self, validated_data):
        return Venue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)


class ArtistSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    image_url= serializers.URLField()
    thumb_url= serializers.URLField()
    facebook_tour_dates_url= serializers.URLField()
    mbid = serializers.CharField(max_length=40)
    upcoming_events_count = serializers.IntegerField()

    def create(self, validated_data):
        return Artist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)