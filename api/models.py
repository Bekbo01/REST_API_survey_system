from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=128, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    TEXT = 'TEXT'
    ONEOPTION = 'ONEOPTION'
    MANYOPTION = 'MANYOPTION'
    TYPE_CHOICES = [
        (TEXT, 'TEXT'),
        (ONEOPTION, 'ONEOPTION'),
        (MANYOPTION, 'MANYOPTION')
    ]

    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250)
    question_type = models.CharField(max_length=250, choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.question_text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=250)

    def __str__(self):
        return self.option_text

class UserAnswer(models.Model):
    user = models.IntegerField()
    poll = models.ForeignKey(Poll, related_name='poll', on_delete=models.PROTECT)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.PROTECT)
    option = models.ForeignKey(Option, related_name='option', null=True, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.option_text