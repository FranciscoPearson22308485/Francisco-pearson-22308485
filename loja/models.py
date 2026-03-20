from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} de {self.cliente}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto}"
