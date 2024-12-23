from django.urls import path
from audio_pocessing.views import AudioUploadView

urlpatterns = [
    path('api/v1/phoneme/', AudioUploadView.as_view(), name='audio_upload'),
]