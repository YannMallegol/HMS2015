
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
        




    def get_query(query_string):  
        
        query=None 
        query1=None
        query2=None
        query3=None
        query4=None
        query5=None
        query6=None
        query7=None
        query8=None
        query9=None
        query10=None
        query11=None
        query12=None
        query13=None
        query14=None
        query15=None
        #query_string=re.compile(r'[^\s";,.:]+').findall(query_string)

        new_query=query_string.split()
        dimension_query = len(new_query)
        terms=new_query

        #print(terms.index()=1)

                


        table=[]
        target1= []
        target2= []
        target3= []
        tab_patient= []
        tab_study = []
        tab_series = []
        index_study = 60
        index_series = 60
        index_patient = 60



        for term_search in enumerate(terms) :
            print(term_search)

        for term in terms:
            w=(terms.index(term))
            if term == "PatientAge" or term == "PatientSex"or term == "PatientID" or term == "PatientName" or term == "PatientPatientBirthDate" or term == "PatientPatientBirthTime":

                    
            #table= "Patient"
            #table_patient=term[]
                table = term
                target1=term
                #print(terms.index(term))
                #print(index(terms))
                index_patient=(terms.index(term))

               # print(index_patient)
                
                #print(term)
                x=terms.index(term)

                
                
                #new_target == False
                search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']

                    

            elif term == "StudyDescription" or term == "StationName" or term == "ManufacturerModelName" or term == "StudyInstanceUID" or term == "Pathology" or term == "StudyDate" or term == "StudyTime" or term == "InstitutionName" or term == "ReferringPhysicianName" or term == "PerformingPhysicianName"or term == "ModalitiesInStudy" or term == "MagneticFieldStrength":
            #table="Study"
            #table_study=term[]
                target2=term
                table = term
                y=terms.index(term)
                #print(terms.index(term))
                index_study=(terms.index(term))
                #index_series=(terms.index(term))
                #new_target=True
                #print(term)
                search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    
               
            elif term == "SeriesNumber" or term == "SeriesInstanceUID" or term == "ProtocolName" or term == "Modality" or term == "SeriesDescription" or term == "SeriesTime" or term == "ContrastAgent" or term=="ScanningSequence" or term=="BodyPartExaminated" or term=="AcquisitionNumber":
                target3=term
                table= term
                #print(terms.index(term))
                index_series=(terms.index(term))
                z=terms.index(term)
                search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']

            else:      
                print('nothing to do')

            

            # boucle permettant de detecter un champ d'une table terminee    



                #regarder si les indices de study et series existent


        print('debut')
        print(index_patient)
        print(index_study)
        print(index_series)
        print('fin')




        for term in terms:
            if target1 is not None and target2 is not None and target3 is not None:

                #########################################################on cherche pour  3 targets ######################################################################



    #boucle pour determiner la premiere target table et calculer la requete

                if index_patient < index_series and index_patient < index_study and index_study < index_series:

                    first_index=index_patient

                    search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    print('test new list')
                    new_list=terms[first_index+1: index_study]
                    #for test in enumerate(new_list) :
                       # print(test)

                    print(new_list)
                    for term  in new_list:
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
                     #return query

                elif index_patient < index_series and index_patient < index_study and index_study > index_series:  

                    first_index=index_patient

                    search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    new_list=terms[first_index+1: index_series]
                    print(new_list)
                    for term  in new_list:
                        or_query1 = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query1 = or_query | q    #MODIF | to &
                        if query1 is None:
                            query1 = or_query
                        else:
                            query1 = query1 & or_query


                elif index_study < index_series and index_study < index_patient and index_patient < index_series:
                    first_index=index_study
                    search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    new_list=terms[first_index+1: index_patient]
                    print(new_list)

                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query2 is None:
                            query2 = or_query
                        else:
                            query2 = query2 & or_query


                elif index_study < index_series and index_study < index_patient and index_patient > index_series:

                    first_index=index_study
                    search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    new_list=terms[first_index+1: index_series]
                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:

                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query3 is None:
                            query3 = or_query
                        else:
                            query3 = query3 & or_query

                          
                elif index_series < index_study and index_series < index_patient and index_patient > index_study:
                    first_index=index_series
                    search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                    new_list=terms[first_index+1: index_study]
                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query4 is None:
                            query4 = or_query
                        else:
                            query4 = query4 & or_query


                elif index_series < index_study and index_series < index_patient and index_patient < index_study:
                    first_index=index_series
                    search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                    new_list=terms[first_index+1: index_patient]
                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query5 is None:
                            query5 = or_query
                        else:
                            query5 = query5 & or_query 


                    #calcul de la deuxieme target    
                             

                elif index_patient > index_study and index_patient< index_series:
                    first_index=index_patient

                    search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    #print('test new list')
                    new_list=terms[first_index+1: index_series]
                    print(new_list)
                    #for test in enumerate(new_list) :
                       # print(test)

                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query6 is None:
                            query6 = or_query
                        else:
                            query6 = query6 & or_query

                elif index_patient > index_series and index_patient< index_study:
                    first_index=index_patient

                    search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    #print('test new list')
                    new_list=terms[first_index+1: index_study]
                    print(new_list)
                    #for test in enumerate(new_list) :
                       # print(test)

                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query7 is None:
                            query7 = or_query
                        else:
                            query7 = query7 & or_query            

                elif index_study > index_patient and index_study < index_series:
                    first_index=index_study
                    search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    new_list=terms[first_index+1: index_series]

                    print(new_list)

                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query8 is None:
                            query8 = or_query
                        else:
                            query8 = query8 & or_query

                elif index_study > index_series and index_study < index_patient:
                    first_index=index_study
                    search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    new_list=terms[first_index+1: index_patient]
                    print(new_list)

                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query9 is None:
                            query9 = or_query
                        else:
                            query9 = query9 & or_query


                elif index_series > index_patient and index_series < index_study:
                    first_index=index_series
                    search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                    new_list=terms[first_index+1: index_study]
                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query10 is None:
                            query10 = or_query
                        else:
                            query10 = query10 & or_query 


                elif index_series > index_study and index_series < index_patient:
                    first_index=index_series
                    search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                    new_list=terms[first_index+1: index_patient]
                    print(new_list)
                    print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIi')
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query11 is None:
                            query11 = or_query
                        else:
                            query11 = query11 & or_query 

    ####### maintenant on esssaye de faire une troisieme target



                elif index_patient > index_study and index_patient> index_series:
                    first_index=index_patient

                    search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    #print('test new list')
                    new_list=terms[first_index+1: index.terms[-1]]
                    print(new_list)
                    #for test in enumerate(new_list) :
                       # print(test)

                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query12 is None:
                            query12 = or_query
                        else:
                            query12 = query12 & or_query

                elif index_study > index_patient and index_study > index_series:
                    first_index=index_study
                    search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    new_list=terms[first_index+1: index.terms[-1]]
                    print(new_list)

                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query13 is None:
                            query13 = or_query
                        else:
                            query13 = query13 & or_query


                elif index_series > index_study and index_series > index_patient:
                    first_index=index_series

                    search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                    new_list=terms[first_index+1: index.terms[-1]]
                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query14 is None:
                            query14 = or_query
                        else:
                            query14 = query14 & or_query




                        
                else:
                    print('ok')





            elif target1 is not None and target2 is not None and target3 is None:







                if index_patient < index_study:

                    first_index=index_patient

                    search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    print('test new list')
                    new_list=terms[first_index+1: index_study]
                    #for test in enumerate(new_list) :
                       # print(test)

                    print(new_list)
                    for term  in new_list:
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
                     #return query


                    second_index=index_study
                    new_list=terms[second_index+1: index.terms[-1]]
                    search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']

                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query1 is None:
                            query1 = or_query
                        else:
                            query1 = query1 & or_query





                elif index_study < index_patient:

                    first_index=index_study
                    search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    new_list=terms[first_index+1: index_patient]
                    print(new_list)

                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query2 is None:
                            query2 = or_query
                        else:
                            query2 = query2 & or_query


                    second_index=index_patient
                    new_list=terms[second_index+1: index.terms[-1]]

                    search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    
                    #for test in enumerate(new_list) :
                       # print(test)

                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query3 is None:
                            query3 = or_query
                        else:
                            query3 = query3 & or_query        





            elif target1 is not None and target2 is None and target3 is not None:


                if index_patient < index_series:


                    first_index=index_patient

                    search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    print('test new list')
                    new_list=terms[first_index+1: index_series]
                    for test in enumerate(new_list) :

                           # print(test)

                        print(new_list)
                        for term  in new_list:
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


                    second_index=index_series

                    search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                    print('test new list')
                    new_list=terms[second_index+1: index.terms[-1]]
                        #for test in enumerate(new_list) :
                           # print(test)

                    print(new_list)
                    for term  in new_list:
                        or_query = None
                        
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query1 is None:
                            query1 = or_query
                        else:
                            query1 = query1 & or_query                






                elif index_patient > index_series:


                    first_index=index_series

                    search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                    print('test new list')
                    new_list=terms[first_index+1: index_patient]
                        #for test in enumerate(new_list) :
                           # print(test)

                    print(new_list)
                    for term  in new_list:
                        or_query = None
                        
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query2 is None:
                            query2 = or_query
                        else:
                            query2 = query2 & or_query                



                    second_index=index_patient

                    search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    print('test new list')
                    new_list=terms[first_index+1: index.terms[-1]]
                        #for test in enumerate(new_list) :
                           # print(test)

                    print(new_list)
                    for term  in new_list:
                        or_query = None
                        
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query3 is None:
                            query3 = or_query
                        else:
                            query3 = query3 & or_query




            elif target1 is  None and target2 is not None and target3 is not None:

                if index_study > index_series:


                    first_index=index_series

                    search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                    new_list=terms[first_index+1: index_study]
                    print(new_list)
                    for term  in new_list:
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

                    second_index=index_study
                    search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    new_list=terms[first_index+1: index.terms[-1]]

                    print(new_list)

                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query1 is None:
                            query1 = or_query
                        else:
                            query1 = query1 & or_query          

                elif index_study < index_series:


                    first_index=index_study

                    search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    new_list=terms[first_index+1: index_series]
                    print(new_list)
                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query2 is None:
                            query2 = or_query
                        else:
                            query2 = query2 & or_query

                    second_index=index_study
                    search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                    new_list=terms[second_index+1: index.terms[-1]]

                    print(new_list)

                    for term  in new_list:
                        or_query = None
                    
                        for field_name in search_fields:

                            q = Q(**{"%s__icontains" % field_name: term}) 
                            if or_query is None:
                                or_query = q
                            else:
                                or_query = or_query | q    #MODIF | to &
                        if query3 is None:
                            query3 = or_query
                        else:
                            query3 = query3 & or_query   
                else:
                    print('nothing')
                                     









####### maintenant si il y a que 1 target########################################
                    


            elif target1 is not None and target2 is None and target3 is None:

                search_fields= ['PatientID','PatientName','PatientSex','PatientAge', 'PatientBirthDate', 'PatientBirthTime']
                    

                for term  in terms:
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


            elif target1 is  None and target2 is not None and target3 is None:
                search_fields=['StudyDescription','StationName','ManufacturerModelName','StudyInstanceUID','Pathology','StudyDate','StudyTime','InstitutionName','ReferringPhysicianName','PerformingPhysicianName','ModalitiesInStudy','MagneticFieldStrength']
                    
                 
                for term  in terms:
                    or_query = None
                    
                    for field_name in search_fields:

                        q = Q(**{"%s__icontains" % field_name: term}) 
                        if or_query is None:
                            or_query = q
                        else:
                            or_query = or_query | q    #MODIF | to &
                    if query1 is None:
                        query1 = or_query
                    else:
                        query1 = query1 & or_query




            elif target1 is  None and target2 is None and target3 is not None:
                search_fields= ['SeriesNumber','SeriesInstanceUID','ProtocolName','Modality', 'SeriesDescription', 'SeriesTime','ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']
                 
          

                for term  in terms:
                    or_query = None
                    
                    for field_name in search_fields:

                        q = Q(**{"%s__icontains" % field_name: term}) 
                        if or_query is None:
                            or_query = q
                        else:
                            or_query = or_query | q    #MODIF | to &
                    if query2 is None:
                        query2 = or_query
                    else:
                        query2 = query2 & or_query

                   

            else:
                print('nothing to do')










   




        return (query,query1,query2,query3,query4,query5,query6,query7,query8,query9,query10,query11,query12, query13, query14, query15)
        #return (target1,target2,tab_series,tab_study,tab_patient,query)        

        #terms.remove(terms[0])# on tire le champ indiquant la target table puis on  va regarder si le prochain ne contient pas une autre target table et ca pour chaqu terme. si le terme contient
        #un autre champ alors on cherche 


        

        
        '''for term  in terms:
            or_query = None
            if index(term) !=  
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
       ''' #return(query)
        

            



        

    
    



    qry = get_query('PatientSex M  ')
   #print(search_fields)
    print(qry) 

 
    


    #fe=Patient.objects.filter(qry)
    #fe.query
    #print(fe.query)'''