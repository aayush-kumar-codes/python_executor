from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class TestApiView(APIView):
    def post(self,request):
        script=request.data.get("script")
        if script is None:
            return Response(
                {
                    "success":False,
                    "message":"script field required",
                    "result":""
                },status=status.HTTP_400_BAD_REQUEST
            )
        Vars = {}
        try:
            exec(script, Vars)
        except Exception as e:
            return Response(
                {
                    "success":False,
                    "message":"not a valid code",
                    "result":""
                },status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {
                "success":True,
                "message":"executed successfully",
                "result":Vars["result"]
            },status=status.HTTP_200_OK
        )