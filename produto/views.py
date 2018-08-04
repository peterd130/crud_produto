from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'inicio.html', {'produtos': produtos})


def cadastrar_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    return render(request, 'cadastro_produto.html', {'form': form})


def modificar_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    return render(request, 'modifica_produto.html', {'form': form, 'produto': produto})


def apagar_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')

    return render(request, 'prod-delete-confirm.html', {'produto': produto})
