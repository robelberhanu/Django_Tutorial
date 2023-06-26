from django.db import models



# Model for Questions.
class Question(models.Model):

    # String method to for convenience
    def __str__(self):
        return self.question_text
    
    question_text = models.CharField(max_length=200)
    pup_date = models.DateField("date published")


class Choice(models.Model):

    #String method to for convenience
    def __str__(self):
        return self.choice_text
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)