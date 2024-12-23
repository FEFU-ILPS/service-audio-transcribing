from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WAVFileSerializer
from .services import process_wav_file

class AudioUploadView(APIView):
    def post(self, request):
        serializer = WAVFileSerializer(data=request.data)
        if serializer.is_valid():
            audio_file = serializer.validated_data['audio_file']
            result = process_wav_file(audio_file)
            return Response({"phonetic_transcription": result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
