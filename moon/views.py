from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from moon.logic import get_moon_info  # we’ll build this

@api_view(['GET'])
def moon_info(request):
    date_str = request.GET.get('date')
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except:
        return Response({"error": "Invalid date format"}, status=400)

    data = get_moon_info(date)
    return Response(data)
