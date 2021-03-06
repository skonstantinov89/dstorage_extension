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
    field10 = models.TextField(blank=True, null=True)
    field11 = models.TextField(blank=True, null=True)
    field12 = models.TextField(blank=True, null=True)

    # 1. Име на регион(или сигнатура)
    # 2. Име на клон(сигнатура)
    # 3. Клиентски номер
    # 4. ЕИК/Булстат
    # 5. Име на клиент
    # 6. Дата на договор
    # 7. Номер на сметка
    # 8. Размер на кредит
    # 9. Валута
    # 10. КИ идентификатор
    # 11. Вид на документ
    # 12. Описание



class Protocols (models.Model):
    userID = models.ForeignKey(User)
    requestDate = models.DateField()
    fromLocation = models.TextField()
    toLocation = models.TextField()
    
class Requests(models.Model):
    '''
    protocolID has to be the autoincrement 
    for every new bundle of requests, so 
    there will be more documents in one paper protocol.
    status = {
                in-progress,    # when we send it from office
                verified,       # when its verified at central
                not-verified,   # when its not verified at central
                incorrect,      # when we correct the returned documents
                not-sended      # when we correct the returned documents
    }
    '''
    verifierID = models.ForeignKey(User, blank=True, null=True)
    documentID = models.ForeignKey(Document)
    protocolID = models.ForeignKey(Protocols)
    status = models.TextField()



