from __future__ import absolute_import

from rest_framework import serializers

from centers.models import Center


class CenterSerializer(serializers.ModelSerializer):
    api_url = serializers.HyperlinkedIdentityField(view_name='api:centers-detail', lookup_field="hash_id")

    class Meta:
        model = Center
        fields = (
            'id',
            'hash_id',
            'name',
            'address',
            'phone',
            'url',
            'price',
            'api_url',
        )
