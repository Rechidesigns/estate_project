from rest_framework import serializers
from comments.models import Comments



class Comment_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ["properties", "comment", "date_time"]