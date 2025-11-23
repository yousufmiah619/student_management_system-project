from django.shortcuts import render
from .seralizers import CourseSeralizer , SubjectSeralizer
from .models import Course, Subject
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


@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated])
def course_details(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Exception as e :
        return Response({"errors":"Course does not find"})
        
    if request.method=="GET":
        serializer=CourseSeralizer(course)
        return Response(serializer.data)
    
    if request.method=="PUT":
        serializer=CourseSeralizer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=200)
        return Response (serializer.errors , status=400)
    
    if request.method=="DELETE":
        course.delete()
        return Response ({"message":"Course delete successfully"},status=204)   
         
         
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def subject_list(request):
    if request.method == "GET" :
        subject=Subject.objects.all()
        seralizer=SubjectSeralizer(subject, many=True)
        return Response(seralizer.data, status=200)

    if request.method == "POST":
        seralizer=SubjectSeralizer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            
            return Response(seralizer.data ,status=201)
    return Response(seralizer.errors ,status=400)
    
@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated])
def subject_details(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
    except Exception as e :
        return Response({"errors":"Subject does not find"})
        
    if request.method == "GET":
        serializer=SubjectSeralizer(subject)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer=SubjectSeralizer(subject,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=200)
        return Response (serializer.errors , status=400)
    
    if request.method == "DELETE":
        subject.delete()
        return Response ({"message":"Subject delete successfully"},status=204)