from rest_framework import serializers

from voting.models import Poll, Option


class PollSerializer(serializers.ModelSerializer):
    options = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='option-detail'
    )

    class Meta:
        model = Poll
        fields = ('title', 'description', 'active', 'expiretion_date', 'assigned_users', 'options')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('title', 'count', 'is_correct', 'poll')
