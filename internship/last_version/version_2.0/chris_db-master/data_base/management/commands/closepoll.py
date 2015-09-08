import os, pydicom
from django.core.management.base import BaseCommand, CommandError
from data_base.models import Patient, Study, Series, MR_Params
#from dicom.errors import InvalidDicomError






class Command(BaseCommand):
    help = 'that does my stuff'


    def handle(self, *args, **options):


       for dossier, sous_dossiers, fichiers in os.walk('/neuro/users/yann.mallegol/Documents/internship/last_version/version_2.0/chris_db-master/data_base/management/commands/dicom_files'):
           for fichier in fichiers:
               fullpath = os.path.join(dossier, fichier)

               print(fullpath)
               try:
                   ds = pydicom.read_file(fullpath)

                   ####################### Patient Table #####################
                   try:
                       patient_test=Patient()
                       patient_test = Patient.objects.create(PatientName=ds.PatientName,
                                                             PatientSex=ds.PatientSex,
                                                             PatientBirthdate=ds.PatientBirthdate,
                                                             PatientAge=ds.PatientAge,
                                                             PatientId=ds.PatienId)


                   except NameError:
                       patient_test.PatientName = 'undefined'
                   except NameError:
                       patient_test.PatientSex='undefined'
                   except NameError:
                       patient_test.PatientBirthdate= 'undefined'
                   except NameError:
                       patient_test.PatientAge='undefined'
                   except NameError:
                       patient_test.PatientId = 'undefined'
                   except AttributeError:
                       patient_test.PatientName = 'undefined'
                   except AttributeError:
                       patient_test.PatientSex='undefined'
                   except AttributeError:
                       patient_test.PatientBirthdate='undefined'
                   except AttributeError:
                       patient_test.PatientAge='undefined'
                   except AttributeError:
                        patient_test.PatientId = 'undefined'


                   patient_test.save()
                   

                    ######################## Study Table ##########################


                   try:
                       study_test=Study()
                       study_test = Study.objects.create(StudyName=ds.StudyName,
                                                          Pathology=ds.Pathology,
                                                          ManufacturerModelName=ds.ManufacturerModelName,
                                                          BodyPartExaminated=ds.BodyPartExaminated,
                                                          MagneticFieldStrength=ds.MagneticFieldStrength,
                                                          Modality=ds.Modality,
                                                          StudyInstanceUID=ds.StudyInstanceUID,
                                                          patient=patient_test)



                   except NameError:
                       study_test.StudyName = 'undefined'
                   except NameError:
                       study_test.Pathology='undefined'
                   except NameError:
                       study_test.ManufacturerModelName= 'undefined'
                   except NameError:
                       study_test.BodyPartExaminated='undefined'
                   except NameError:
                       study_test.MagneticFieldStrength = 'undefined'
                   except NameError:
                       study_test.Modality = 'undefined'
                   except NameError:
                       study_test.StudyInstanceUID = 'undefined'
                   except AttributeError:
                       patient_test.StudyName = 'undefined'
                   except AttributeError:
                       study_test.Pathology='undefined'
                   except AttributeError:
                       study_test.ManufacturerModelName= 'undefined'
                   except AttributeError:
                       study_test.BodyPartExaminated='undefined'
                   except AttributeError:
                       study_test.MagneticFieldStrength = 'undefined'
                   except AttributeError:
                       study_test.Modality = 'undefined'
                   except AttributeError:
                       study_test.StudyInstanceUID = 'undefined'


                   study_test.save()



                   ############### Series table #################

                   try:
                       series_test=Series()
                       series_test = Series.objects.create(SeriesName=ds.SeriesName,
                                                          SeriesInstanceUID=ds.SeriesInstanceUID,
                                                          ProtocolName=ds.ProtocolName,
                                                          study=study_test)



                   except NameError:
                       series_test.SeriesName = 'undefined'
                   except NameError:
                       series_test.SeriesInstanceUID='undefined'


                   series_test.save()






                    ############# MR_Params ###############


                   mr_params_test=MR_Params()
                   mr_params_test = MR_Params.objects.create(SliceThickness=ds.SliceThickness,
                                                                  EchoTime=ds.EchoTime,
                                                                  InversionTime=ds.InversionTime,
                                                                  RepetionTime=ds.RepetionTime,
                                                                  modality_params= series_test)















               except pydicom.errors.InvalidDicomError:
                       print('not possible to know this information')
