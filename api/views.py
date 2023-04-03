from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Note
from api.serializers import NotesSerializer

# Create your views here.



@api_view(['GET',"POST"])
def notes_api(request):

    if request.method == "GET":
        notes = Note.objects.all().order_by('-updated_date')
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        data = request.data
        note = Note.objects.create(
            body = data['body']
        )
        serializer = NotesSerializer(note, many=False)
        return Response(serializer.data)
    
@api_view(['GET','PUT','DELETE'])
def note_api(request, pk):

    if request.method == "GET":
        note = Note.objects.get(id=pk)
        serializer = NotesSerializer(note, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":

        data = request.data
        note = Note.objects.get(id=pk)
        serializer = NotesSerializer(instance=note, data=data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    
    if request.method == "DELETE":
        note = Note.objects.get(id=pk)
        note.delete()

        return Response('Note Deleted')
    

    

    


