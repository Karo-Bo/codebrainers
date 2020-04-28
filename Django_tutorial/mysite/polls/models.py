from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(help_text='Date published')

    def __str__(self):
        return self.question_text # + str(self.pub_date)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    # tworzymy klucz obcy do tabeli Question, parametr on_delete - można
    # usunąć Question tylko jeśli nie ma dla niego żadnego Choice'a
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



# "O której godzinie powinna być przerwa w trakcie sobotnich zajęć?" - Question
# a) 11.00 - Choice
# b) 12.00 - Choice
# c) 12.30 - Choice
# d) kolor żółty - Choice