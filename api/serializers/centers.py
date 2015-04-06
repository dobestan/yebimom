from __future__ import absolute_import

from rest_framework import serializers

from centers.models import Center


class CenterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Center
        fields = (
            'id',
            'name',
            'address',
            'phone',
            'url',
            'price',
            'hash_id',
        )
