from django.db import models

# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length=100)

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    QUESTION_TYPES = (
        ('text', 'Text'),
        ('radio', 'Radio'),
        ('checkbox', 'Checkbox'),
    )
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
