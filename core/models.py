from django.db import models
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


def files_path(instance, filename):
    return 'article/{}/{}'.format(
        instance.id,
        filename
    )



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
        blank = True,
        unique = True
    )

    class Meta:
        db_table = "category"
        verbose_name = "Categorias"
        verbose_name_plural = "categoria"
    
    def __str__(self):
        return  self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug   
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(
        max_length = 255
    )
    slug = models.SlugField(
        null = True,
        blank = True,
        unique = True 
    )
    subtitle = models.CharField(
        max_length = 255,
        blank = True
    )
    body = HTMLField()
    image = models.ImageField(
        upload_to = files_path,
        verbose_name = 'Image',
        null = True,
        blank = True
    )
    attachment = models.FileField(
        upload_to = files_path,
        verbose_name = 'Attachment',
        null = True,
        blank = True
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        null = True
    )

    class Meta:
        db_table = "article"
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug   
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class Publish(models.Model):
    author = models.ManyToManyField(
        Author
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
        ordering = ['-created_at']

    def __str__(self):
        return self.article.title
    