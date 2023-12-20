from rest_framework import serializers

class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="PublicId", read_only=True, format="hex")
    Created = serializers.DateTimeField(read_only=True)
    Updated = serializers.DateTimeField(read_only=True)
    