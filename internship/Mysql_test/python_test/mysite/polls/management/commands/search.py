import os, re
from django.db.models import Q
from polls.models import Patient, Study, Series, MR_Params, US_Params, CT_Params, Review
from django.core.management.base import BaseCommand
from operator import __or__ as OR



class Command(BaseCommand):
    help = 'Find .dcm files and complite tables'


    def handle(self, *args, **options):

        #search_fields=['Patient','Study', 'Series']
        #print('make a query: ')
        print(' ')
        #query_string=input()
        #query=None
        #query_string=re.compile(r'[^\s";,.:]+').findall(query_string)
        #print('search fileds: ')
        #search_fields=input()



    def normalize_query(query_string):
        re.compile(r'[^\s";,.:]+').findall(query_string)
        print(query_string)
        return(query_string)

    def get_query(query_string,search_fields):  
        query=None 
        query_string=re.compile(r'[^\s";,.:]+').findall(query_string)
        terms = query_string
                # init our q objects variable to use .add() on it
        #q_objects = Q()

        for term in terms:
            or_query = None
            for field_name in search_fields:
                q = Q(**{"%s__icontains" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
        return(query)


      
    qry = get_query(' DIFFUSION  888 021Y ', ['SeriesDescription','SeriesInstanceUID'])

    print(qry)

    fe=Series.objects.filter(qry)
    fe.query
    print(fe.query)
