from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(max_length=150, verbose_name="Friendly URL", unique=True)
    order = models.IntegerField(verbose_name="Orden", default=0)
    hidden = models.BooleanField(verbose_name="Visible")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title