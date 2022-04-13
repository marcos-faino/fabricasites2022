from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado= models.DateTimeField(auto_now=True)
    situacao = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Cargo(Base):
    cargo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=200)
    biografia = models.TextField('Bio', max_length=1000)
    cargo = models.ForeignKey('Cargo',
                              on_delete=models.SET_NULL,
                              null=True)
    foto = StdImageField('Foto', upload_to='equipe',
                         variations={'thumb': {'width': 600,
                                               'height': 600,
                                               'crop': True}})

