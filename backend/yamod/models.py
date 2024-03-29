from django.db import models


class Country(models.Model):

    name = models.TextField()
    capital = models.TextField(null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):

    CHOICES = (
        ('a', 'Action'),
        ('c', 'Comedy')
    )

    title = models.TextField()
    genre = models.CharField(max_length=1, choices=CHOICES, null=True)
    release_date = models.DateField()
    plot = models.TextField()
    duration = models.PositiveIntegerField(help_text='in Minutes')
    black_and_white = models.BooleanField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField('Person', blank=True)

    def __str__(self):
        return self.title


class Person(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    year_of_birth = models.IntegerField()

    def __str__(self):
        return '%s %s (%s)' % (self.first_name, self.last_name, self.year_of_birth)
