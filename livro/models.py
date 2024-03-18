from django.db import models

# Create your models here.
class Escritor(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField(null=True)

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    escritor = models.ForeignKey(Escritor, on_delete=models.CASCADE)

    # O modelo Livro, poderia possuir outras relações Many-to-one
    # tal como, idioma e categoria principal