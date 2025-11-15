from django.shortcuts import render
from .seralizers import CourseSeralizer , SubjectSeralizer
from .models import Course, Subjct
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser

# Create your views here.

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def course_list(request):
    if request.method == "GET" :
        course=Course.objects.all()
        seralizer=CourseSeralizer(course, many=True)
        return Response(seralizer.data, status=200)

    if request.method == "POST":
        seralizer=CourseSeralizer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            
            return Response(seralizer.data ,status=201)
    return Response(seralizer.errors ,status=400)
    
