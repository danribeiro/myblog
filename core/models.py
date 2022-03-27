from re import L
from tabnanny import verbose
from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        verbose_name = "Nome",
        max_length = 100
    )
    last_name = models.CharField(
        verbose_name = "Sobrenome",
        max_length = 100
    )
    
    class Meta:
        db_table = "author"
        verbose_name = "Autores"
        verbose_name_plural = "Autor"
    
    def __str__(self):
        return  "{} {}".format(self.first_name, self.last_name)
    

class Category(models.Model):
    name = models.CharField(
        verbose_name = "Categoria",
        max_length = 100
    )
    slug = models.SlugField(
        max_length = 100
    )

    class Meta:
        db_table = "category"
        verbose_name = "Categorias"
        verbose_name_plural = "categoria"
    
    def __str__(self):
        return  self.name


class Article(models.Model):
    title = models.CharField(
        max_length = 255
    )
    subtitle = models.CharField(
        max_length = 255,
        blank = True
    )
    body = models.TextField()

    class Meta:
        db_table = "article"
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    def __str__(self):
        return self.title


class Publish(models.Model):
    author = models.OneToOneField(
        Author,
        on_delete = models.PROTECT
    )
    article = models.OneToOneField(
        Article,
        on_delete = models.PROTECT
    )
    category = models.ManyToManyField(
        Category,
        related_name = "publishes"
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )

    class Meta:
        db_table = "publish"
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"

    def __str__(self):
        return self.article.title
    