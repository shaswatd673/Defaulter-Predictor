#from django.shortcuts import render
from ml_api.models import Applicant
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ml_api.serializers import ApplicantSerializer, PredictionSerializer
from ml_api.SVMModel import svm_predictor

# Create your views here.
class ApplicantApporval(APIView):

	def post(self, request, format=None):
		reqserializer = ApplicantSerializer(data = request.data)
		if reqserializer.is_valid():
			rawdata = svm_predictor(reqserializer.data)
			print(rawdata)
			prediction = rawdata.predict()
			serializedpred = PredictionSerializer(prediction)
			return Response(serializedpred.data, status=status.HTTP_201_CREATED)
		return Response(reqserializer.errors, status=status.HTTP_400_BAD_REQUEST)