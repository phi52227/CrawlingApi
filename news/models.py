from django.db import models


class PoliticsNews(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    posting_date = models.CharField(max_length=30)
    content = models.TextField()
    order = models.CharField(max_length=12)

    def __str__(self):
        return self.title


class EconomyNews(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    posting_date = models.CharField(max_length=30)
    content = models.TextField()
    order = models.CharField(max_length=12)

    def __str__(self):
        return self.title


class SocietyNews(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    posting_date = models.CharField(max_length=30)
    content = models.TextField()
    order = models.CharField(max_length=12)

    def __str__(self):
        return self.title


class LifeCultureNews(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    posting_date = models.CharField(max_length=30)
    content = models.TextField()
    order = models.CharField(max_length=12)

    def __str__(self):
        return self.title


class ItScienceNews(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    posting_date = models.CharField(max_length=30)
    content = models.TextField()
    order = models.CharField(max_length=12)

    def __str__(self):
        return self.title
