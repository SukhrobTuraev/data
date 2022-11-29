from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


# Create your views here.
@api_view(['GET', 'POST'])
def test_get(request):
    std = Student.objects.all()
    serializer = StudentSerializer(std, many=True)
    return Response({'Status': 200, 'data': serializer.data})


@api_view(['POST'])
def test_post(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)

    if not serializer.is_valid():
        return Response({'Status': 403, 'message': 'An error occurred'})

    serializer.save()

    return Response({'Status': 200, 'data': serializer.data, 'message': 'Data received'})