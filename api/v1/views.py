from rest_framework.response import Response
from rest_framework.views import APIView


class PostAPIView(APIView):
    def get(self, req):
        return Response({'title': 'Some title'})
