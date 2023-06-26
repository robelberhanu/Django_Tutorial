from django.db import models

# Model for Questions.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pup_date = models.DateField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)