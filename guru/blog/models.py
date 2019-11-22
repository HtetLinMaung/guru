from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Article(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
