from django.db import models


class News(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    posting_date = models.CharField(max_length=30)
    content = models.TextField()
    order = models.CharField(max_length=12)

    def __str__(self):
        return self.title
