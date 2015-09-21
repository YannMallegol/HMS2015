import os, re, sys
from django.db.models import Q
from polls.models import Patient, Study, Series, MR_Params, US_Params, CT_Params, Review
from django.core.management.base import BaseCommand
from operator import __or__ as OR

'''proj_path = "/neuro/users/yann.mallegol/Documents/internship/Mysql_test/python_test/mysite"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polls.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()'''



class Command(BaseCommand):
    help = 'Find .dcm files and complite tables'


    def handle(self, *args, **options):


        print(' ')
        



    def get_query(query_string,search_fields):  
        
        query=None 
        query_string=re.compile(r'[^\s";,.:]+').findall(query_string)
        terms = query_string
        #print(terms)
      

        for term in terms:
            or_query = None
            for field_name in search_fields:
                q = Q(**{"%s__icontains" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q    #MODIF | to &
            if query is None:
                query = or_query
            else:
                query = query & or_query
        return(query)


      
    qry = get_query(' 007M   M', ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime'])

    #print(qry)
    


    fe=Patient.objects.filter(qry)
    print(fe)
    ######### we can see the two patients: [<Patient: 4414712>, <Patient: 4448220>]
    #########it is the right answer



######### If you want more complex research :

    #fe.query
    #print(fe.query)

    



    
