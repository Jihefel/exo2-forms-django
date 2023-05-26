from django.db import models

class Member(models.Model):
    GENDER_CHOICES = (
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    )
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    age = models.IntegerField()

    class Meta:
        db_table = 'members'

    def __str__(self):
        return self.name