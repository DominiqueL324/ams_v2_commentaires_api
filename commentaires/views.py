from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions, generics,mixins,status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from datetime import date, datetime,time,timedelta
import string, json,  requests
from .models import Commentaire
from .serializer import CommentaireSerializer
from bson import ObjectId
from django.core.paginator import Paginator
from djongo.models import Q


class CommentaireApi(APIView):

    def post(self,request):
        data = json.loads(request.body)
        com =  Commentaire(commentaire=data['commentaire'],nature=data['nature'],key=data['key'],code=data['code'],status=data['status'],numero_ordre=data['numero_ordre'])
        com.save()
        all_comments = Commentaire.objects.all()[Commentaire.objects.all().__len__()-1]
        serializer = CommentaireSerializer(Commentaire.objects.filter(pk=all_comments.id),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 

    def get(self,request):
        all_comments = Commentaire.objects.all()

        # Number of items per page
        page_number = request.GET.get('page') 
         
        # Cas sans pagination
        if page_number is None:
            serializer = CommentaireSerializer(all_comments,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK) 
        
        # Cas avec pagination
        paginator = Paginator(all_comments, per_page=10)  
        try:
            page_obj = paginator.page(page_number)
        except :
            # Handle invalid page number error
            return JsonResponse({'error': 'Invalid page number'}, status=400)
        pagination_metadata = {
            'current_page': page_obj.number,
            'num_pages': paginator.num_pages,
            'total_items': paginator.count,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next(),
        }
        serializer = CommentaireSerializer(page_obj,many=True)
        res={}
        res['info_pagination'] = pagination_metadata
        res['results']= serializer.data
        return Response(res,status=status.HTTP_200_OK)

class CommentairEditeApi(APIView):

    def put(self,request,id):
        data = json.loads(request.body)
        com = Commentaire.objects.filter(pk= ObjectId(id))
        com = com.first()
        if com is not None:
            com.commentaire = data['commentaire']
            com.nature =data['nature']
            com.key = data['key']
            com.code = data['code']
            com.status = data['status']
            com.numero_ordre = data['numero_ordre']
            com.save()
            com = Commentaire.objects.filter(pk= ObjectId(id))
            serializer = CommentaireSerializer(com,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"status":"none"}, status=status.HTTP_204_NO_CONTENT)

    def get(self,request,id):
        com = Commentaire.objects.filter(pk= ObjectId(id))
        com = com.first()
        if com is not None:
            com = Commentaire.objects.filter(pk= ObjectId(id))
            serializer = CommentaireSerializer(com,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"status":"none"}, status=status.HTTP_204_NO_CONTENT)
    
class CommentaireFiltreApi(APIView):
    def get(self,request):
        contenu = request.GET.get('to_find')
        rubrique = request.GET.get('rubrique')
        query = Q()
        if contenu is not None:
            query &= Q(commentaire__icontains = str(contenu))

        if rubrique is not None:
            query &= Q(key = str(rubrique)) 

        all_comments = Commentaire.objects.filter(query)
        serializer = CommentaireSerializer(all_comments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
            