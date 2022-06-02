
class Cliente:
  def __init__(self, nome, endereco, bairro, cidade, estado):
    self.nome = nome
    self.endereco = endereco
    self.bairro = bairro
    self.cidade = cidade
    self.estado = estado

  def myfunc(self):
    print("Hello my name is " + self.name)


clientes = open("c:\Clientes\S\Sirius\Totaldocs\JSTX0508_EmDiaTESTES.csv")
for linhaCliente in clientes:
  dadosClientes = linhaCliente.split(";");
  cliente = Cliente(dadosClientes[0], 
                    dadosClientes[1],
                    dadosClientes[2],
                    dadosClientes[3],
                    dadosClientes[4])
  print(cliente.nome)                  