import django
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FormEntry
from .serializers import FormEntrySerializer

django.setup()

@api_view(['POST'])
def submit_form(request):
    serializer = FormEntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
