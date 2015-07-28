from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Files(models.Model):
    docfile = models.FileField(upload_to='files/%Y%m%d')

class Document(models.Model):
    '''
    status = { 
                in-warehouse,
                in-courier,
                destroyed,
                incorrect-input
             }
    location = {
                    storage 1
                    storage 2
                    storage 3
    }
    '''
    active = models.BooleanField(default = True)
    status = models.TextField()
    location = models.TextField()
    officeStartDate = models.DateField(blank = True, null = True)
    centralManagementStartDate = models.DateField(blank = True, null = True)
    archiveStartDate = models.DateField(blank = True, null=True)
    userID = models.ForeignKey(User)
    fileID = models.ForeignKey(Files, blank=True, null=True)
    
class Criterion(models.Model):
    # Трябва да ни се дадат кои ще са критериите,
    # Понеже така ще стане много сложно
    documentID = models.ForeignKey(Document)
    field1 = models.TextField(blank=True, null=True)
    field2 = models.TextField(blank=True, null=True)
    field3 = models.TextField(blank=True, null=True)
    field4 = models.TextField(blank=True, null=True)
    field5 = models.TextField(blank=True, null=True)
    field6 = models.TextField(blank=True, null=True)
    field7 = models.TextField(blank=True, null=True)
    field8 = models.TextField(blank=True, null=True)
    field9 = models.TextField(blank=True, null=True)


class Requests(models.Model):
    '''
    protocolID has to be the autoincrement 
    for every new bundle of requests, so 
    there will be more documents in one paper protocol.
    status = {
                in-progress,
                verified,
                not-verified,
                incorrect,
                not-sended
    }
    '''
    userID = models.ForeignKey(User)
    documentID = models.ForeignKey(Document)
    requestDate = models.DateField()
    status = models.TextField()
    fromLocation = models.TextField()
    toLocation = models.TextField()
    protocolID = models.IntegerField()


