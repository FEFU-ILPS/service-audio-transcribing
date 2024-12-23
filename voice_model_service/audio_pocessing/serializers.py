from rest_framework import serializers

class WAVFileSerializer(serializers.Serializer):
    audio_file = serializers.FileField()

    def validate_audio_file(self, value):
        if not value.name.endswith('.wav'):
            raise serializers.ValidationError("The file must be in .wav format")
        return value
