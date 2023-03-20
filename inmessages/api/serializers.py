from rest_framework import serializers
from inmessages.models import Estate_Messages


class Message_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Estate_Messages
        fields = ('sender', 'recipients', 'message_type','subject_heading', 'message_content')
