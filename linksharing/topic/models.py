from django.db import models
from profiles.models import *
# Create your models here.

choices = (('CA', 'Casual'), ('SE', 'Serious'), ('VS', 'Very Serious'))
visibility = (('PR', 'private'), ('PU', 'public'))


class Topic(models.Model):
    created_by = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    visibility = models.CharField(max_length=20, choices=visibility, default=visibility[1][1])
    seriousness = models.CharField(max_length=20, choices=choices, default=choices[2][1])
    subscribers = models.ManyToManyField(UserProfile, related_name='topics_subscribe')


class LinkDocumentResource(models.Model):
    owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='link_documents')
    link = models.CharField(max_length=200, null=True, blank=True)
    document = models.FileField(upload_to='documents', null=True, blank=True)
    description = models.TextField()




