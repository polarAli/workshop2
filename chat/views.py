from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ConversationsListSerializer, CreateMessageSerializers, MessageSerializer, \
    UpdateMessageSerializer
from .models import Message, Conversation


class ConversationsView(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        convs = Conversation.objects.all()
        return Response(ConversationsListSerializer(convs, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ConversationsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Conversation created!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Validation failed!',
                             'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ConversationView(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request, pk):
        messages = Message.objects.filter(conversation_id=pk).all()
        return Response(MessageSerializer(messages, many=True).data)

    def post(self, request, pk):
        conversation = Conversation.objects.get(pk=pk)
        serializer = CreateMessageSerializers(data=request.data, context={'sender': request.user,
                                                                          'conversation': conversation})
        if serializer.is_valid():
            serializer.save(sender=request.user, conversation=conversation)
            return Response({'message': 'Message created!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Validation failed!',
                             'errors': serializer.errors})

    def put(self, request, pk):
        message = Message.objects.get(id=request.data['id'])
        serializer = UpdateMessageSerializer(message, data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Message updated!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Validation failed!',
                             'errors': serializer.errors})
