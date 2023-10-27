from django.shortcuts import render
import random
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.response import Response
from .models import PhoneAuth
from rest_framework.views import APIView


class PhoneAuthAPI(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            p_num = request.data["phone_number"]
        except KeyError:
            return Response(
                {"message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            PhoneAuth.objects.update_or_create(phone_number=p_num)
            return Response({"message": "OK"})

    @csrf_exempt
    def get(self, request):
        try:
            p_num = request.query_params["phone_number"]
            a_num = request.query_params["auth_number"]
            print(p_num)
            print(a_num)
        except KeyError:
            return Response(
                {"message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            result = PhoneAuth.check_auth_number(p_num, a_num)
            return Response(
                {
                    "message": "OK",
                    "result": result,
                }
            )
