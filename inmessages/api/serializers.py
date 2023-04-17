from rest_framework import serializers
from inmessages.models import Estate_Messages
from estate_project.users.models import User

class User_Info ( serializers.ModelSerializer ):

    class Meta:
        model = User
        fields = ('name', 'email',)



class Message_Serializer(serializers.ModelSerializer):
    recipient_email = serializers.EmailField( required = True )
    class Meta:
        model = Estate_Messages
        fields = ('recipient_email','message_type','subject_heading', 'message_content')