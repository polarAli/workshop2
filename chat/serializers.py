from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Message, Conversation


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class CreateMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text']

    def validate(self, attrs):
        if self.context['sender'] not in self.context['conversation'].members.all():
            raise ValidationError("You are not a member of this conversation")
        return attrs


class UpdateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text']


class ConversationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'name', 'members']
