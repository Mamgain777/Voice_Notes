from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from api.models import Note
from api.serializers import NotesSerializer
from django.contrib.auth.models import User

# Create your views here.



@api_view(['GET',"POST"])
@permission_classes([IsAuthenticated])
def notes_api(request):

    user = request.user
    
    if request.method == "GET":
        # print(user.pk)
        notes = user.notes.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        
        data = request.data
        note = Note.objects.create(
            owner = user,
            body = data['body']
        )
        serializer = NotesSerializer(note, many=False)
        return Response(serializer.data)
    
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def note_api(request, pk):
    user = request.user
    if request.method == "GET":
        print(user)
        try:
            note = Note.objects.get(id=pk)
            if user == note.owner:
                serializer = NotesSerializer(note, many=False)
                return Response(serializer.data)
            else:
                return Response("fail")
        except:
            return Response('fail')
    
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
    



        
@api_view(["POST"])
def create(request):

    if request.method == "POST":
        
        username = request.data['username']
        password = request.data['password']
        result = User.objects.filter(username = username)
        if(len(result) == 0):

            new_user = User(username = username)
            new_user.set_password(password)
            new_user.save()
            return Response('sucess')
        else:
            return Response("fail")
        
    
    

    

    


