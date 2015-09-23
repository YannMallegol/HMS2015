
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
        
    '''def target_table(self,query_string): 

        #query_string=re.compile(r'[^\s";,.:]+').findall(query_string)
        new_query=query_string.split()
        terms = new_query

        #for term in terms:
        
        if term[0] == "PatientAge" or term[0] == "PatientSex"or term[0] == "PatientID" or term[0] == "PatientName" or term[0] == "PatientPatientBirthDate" or term[0] == "PatientPatientBirthTime":
                
            table= "Patient"
            search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']

                

        elif term[0] == "StudyDescription" or term[0] == "StationName" or term[0] == "ManufacturerModelName" or term[0] == "StudyInstanceUID" or term[0] == "Pathology" or term[0] == "StudyDate" or term[0] == "StudyTime" or term[0] == "InstitutionName" or term[0] == "ReferringPhysicianName" or term[0] == "PerformingPhysicianName"or term[0] == "ModalitiesInStudy" or term[0] == "MagneticFieldStrength":
            table="Study"
            search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                
           
        else:
            table="Series"  
            search_fields=['SeriesDescription','SeriesInstanceUID']                

        return(table, search_fields)'''



    def get_query(query_string,search_fields):  
        
        query=None 
        #query_string=re.compile(r'[^\s";,.:]+').findall(query_string)
        new_query=query_string.split()
        dimension_query = len(new_query)
        term=new_query

        if term[0] == "PatientAge" or term[0] == "PatientSex"or term[0] == "PatientID" or term[0] == "PatientName" or term[0] == "PatientPatientBirthDate" or term[0] == "PatientPatientBirthTime":
                
            table= "Patient"
            table_patient=term[]
            search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']

                

        elif term[0] == "StudyDescription" or term[0] == "StationName" or term[0] == "ManufacturerModelName" or term[0] == "StudyInstanceUID" or term[0] == "Pathology" or term[0] == "StudyDate" or term[0] == "StudyTime" or term[0] == "InstitutionName" or term[0] == "ReferringPhysicianName" or term[0] == "PerformingPhysicianName"or term[0] == "ModalitiesInStudy" or term[0] == "MagneticFieldStrength":
            table="Study"
            table_study=term[]
            search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                
           
        else:
            table="Series"  
            table_series=term[]
            search_fields=['SeriesDescription','SeriesInstanceUID']  

        #print(new_query)
        print(dimension_query)
        #terms = new_query
        print(term)
        print(table)
        #self.target_table(query_string)
        print(search_fields)
        for each_term in term:
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


    




    qry = get_query(' PatientSex : 14001 M ',['PatientSex'])

    

 
    


   # fe=table.objects.filter(qry)
   # print(fe)