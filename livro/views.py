from django.shortcuts import render, redirect
from .models import Escritor, Livro
from random import choice

# Create your views here.

def index(request):
    escritores = Escritor.objects.all()
    return render(request, 'livro/index.html', {'escritores':escritores})

def exemplo(request, id):

    # Buscando o escritor no banco de dados
    escritor = Escritor.objects.get(id=id)

    # Criando um livro e vinculando ao escritor
    titulo_aleatorio = get_titulo_aleatorio()
    livro = Livro(titulo=titulo_aleatorio, escritor=escritor)
    livro.save()

    return redirect('livros')

def livros(request):
    livros = Livro.objects.all()
    return render(request, 'livro/livros.html', {'livros':livros})

def get_titulo_aleatorio():
    livros = ["Sombras da Meia-Noite", "O Enigma de Alabasta", "Caminhos Perdidos", "A Queda do Império Estelar", "A Herança do Dragão", "O Jardim Secreto", "A Última Fronteira", "Memórias Esquecidas", "O Círculo dos Destinos", "O Labirinto das Almas", "A Canção do Deserto", "O Segredo do Relógio", "Noites de Insônia", "A Porta do Tempo", "As Sombras do Passado", "O Refúgio das Estrelas", "O Pergaminho Mágico", "As Crônicas do Viajante", "O Legado das Fadas", "A Dança dos Destinos", "O Mistério da Ilha Solitária", "As Lágrimas do Céu", "O Tesouro do Pirata", "A Profecia dos Ancestrais", "O Segredo do Olhar"]
    palavras_adicionais = ["Sombras", "Mistério", "Aventura", "Segredo", "Destino", "Magia", "Jornada", "Amor", "Conquista", "Desafio", "Herança", "Tempo", "Espaço", "Paixão", "Recomeço", "Profecia", "Tesouro", "Fuga", "Poder", "Ilusão", "Renascimento", "Reflexo", "Solitário", "Reviravolta", "Labirinto", "Reino", "Escuridão", "Eterno", "Peregrinação", "Enigma"]
    titulo_aleatorio = choice(livros)

    if Livro.objects.filter(titulo=titulo_aleatorio):
        return f'{titulo_aleatorio} {choice(palavras_adicionais)}'
    else:
        return titulo_aleatorio




    