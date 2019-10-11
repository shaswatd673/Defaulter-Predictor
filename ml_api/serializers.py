from . models import Applicant
from rest_framework import serializers

class ApplicantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Applicant
		fields = "__all__"


class PredictionSerializer(serializers.Serializer):
	result = serializers.CharField(max_length=100)