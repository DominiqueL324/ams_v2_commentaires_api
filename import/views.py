from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions, generics,mixins,status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime, random, string
from django.contrib.auth.models import User
from django.core.mail import send_mail
from datetime import date, datetime,time,timedelta
import pandas as pd
import requests
import string, json


class ImportApi(APIView):
    def post(self,request):
        """excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        data_=request.data
        # Iterate over each row in the DataFrame
        if data_['cible'] == "rubrique":
            url = "http://195.15.218.172/edlgateway/api/v1/rubric/add"
            for index, row in df.iterrows():
                # Extract the data from each column
                data = {
                    "nom": row[2],
                    "numero_ordre": row[1],
                    "description":"",
                    "status":"on",
                    "code": row[0]
                }
                res = requests.post(url=url,data=json.dumps(data),headers={'Content-Type': 'application/json','Authorization':'0000'})
                print(json.dumps(data))
                if res.status_code != 200:
                    print("Echec")
                else:
                    print('okay')
                # Extract the data from each column
        if data_['cible'] == "cles":
            url = "http://195.15.218.172/edlgateway/api/v1/clefs/add"
            for index, row in df.iterrows():
                # Extract the data from each column
                data = {
                    "nom": row[1],
                    "description":row[2],
                    "status":"on",
                    "code": row[0]
                }
                res = requests.post(url=url,data=json.dumps(data),headers={'Content-Type': 'application/json','Authorization':'0000'})
                print(json.dumps(data))
                if res.status_code != 200:
                    print("Echec")
                else:
                    print('okay')
                # Extract the data from each column
        if data_['cible'] == "compteurs":
            url = "http://195.15.218.172/edlgateway/api/v1/compteurs/add"
            for index, row in df.iterrows():
                # Extract the data from each column
                data = {
                    "nom": row[1],
                    "description":row[2],
                    "status":"on",
                    "code": row[0]
                }
                res = requests.post(url=url,data=json.dumps(data),headers={'Content-Type': 'application/json','Authorization':'0000'})
                print(json.dumps(data))
                if res.status_code != 200:
                    print("Echec")
                else: 
                    print('okay')
                # Extract the data from each column
        if data_['cible'] == "pieces":
            url = "http://195.15.218.172/edlgateway/api/v1/piece/add"
            for index, row in df.iterrows():
                # Extract the data from each column
                data = {
                    "nom": row[3],
                    "rubriques": {},
                    "numero_ordre": row[1],
                    "description":row[4],
                    "status":"on",
                    "code": row[0]
                }
                res = requests.post(url=url,data=json.dumps(data),headers={'Content-Type': 'application/json','Authorization':'0000'})
                print(json.dumps(data))
                if res.status_code != 200:
                    print("Echec")
                else:
                    print('okay')
                # Extract the data from each column

        if data_['cible'] == "commentaires":
            url = "http://195.15.218.172/edlgateway/api/v1/commentaire/add"
            url_get = "http://195.15.218.172/edlgateway/api/v1/rubric/all?start=1&limit=10&count=10"
            rub = requests.get(url=url_get,headers={'Authorization':'0000'})
            if rub.status_code == 200:
                dataRub = rub.json()
            else:
                print(rub)
            #print(dataRub['results'])
            for index, row in df.iterrows():
                data = {
                    "commentaire": row[3],
                    "key_": "autre",
                    "nature":"autres",  
                    "status":"on",
                    "code": row[0],
                    "numero_ordre":""
                }
                if data_["type"]=="etat":
                    data['type'] = "etat"

                if data_["type"]=="action":
                    data['type'] = "action"

                if data_["type"]=="travail":
                    data['type'] = "travail"
                    data['numero_ordre'] = row[3]
                    data['commentaire'] = row[1]

                if data_["type"]=="description":
                    data['type'] = "description"
                    data['numero_ordre'] = row[1]
                    data['commentaire'] = row[3]
                    for ru in dataRub['results']:
                        if str(ru["nom"]).replace(" ","") == str(row[5]).replace(" ",""):
                            data['key_']=ru['id']
                            data['nature'] = "rubrique" 

                if data_["type"]=="defaut":
                    data['type'] = "defaut"
                    data['numero_ordre'] = row[1]
                    data['commentaire'] = row[3]
                    for ru in dataRub['results']:
                        if str(ru["nom"]).replace(" ","") == str(row[5]).replace(" ",""):
                            data['key_']=ru['id']
                            data['nature'] = "rubrique"

                if data_["type"]=="observation":
                    data['type'] = "observation"
                    data['numero_ordre'] = row[3]
                    data['commentaire'] = row[1]
                    for ru in dataRub['results']:
                        if str(ru["nom"]).replace(" ","").lower() == str(row[5]).replace(" ","").lower():
                            data['key_']=ru['id']
                            data['nature'] = "rubrique"
                # Extract the data from each column
                res = requests.post(url=url,data=json.dumps(data),headers={'Content-Type': 'application/json','Authorization':'0000'})
                print(json.dumps(data))
                if res.status_code != 200:
                    print("Echec")
                else:
                    print('okay')
                #Extract the data from each column"""
            
        return Response({},status=status.HTTP_200_OK)
            