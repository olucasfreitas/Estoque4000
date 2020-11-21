from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions.serializer import ManufacturerSchema, ProductSchema
from ..extensions.database import Session
from ..extensions.database import Manufacturer
from ..extensions.database import Product
from sympy import var, diff, Lambda, solve, init_printing

def lucro_max(Q, C):
  """
  Usamos como base o seguinte exemplo para construir nossa função:

  "Um fabricante pode produzir calçados ao custo de R$ 20,00 o par.
   Estima-se que, se cada par for vendido por x reais, o fabricante venderá
   por mês 80 – x (0 ≤ x ≤ 80) pares de sapatos. Assim, o lucro mensal do fabricante
   é uma função do preço de venda. Qual deve ser o preço de venda, de modo que o lucro
   mensal seja máximo?"

   Precisamos ficar atento para que:

   Q = Quantidade
   x = Preço do produto a venda.
   0 ≤ x ≤ Q
   Logo, nosso preço precisa ser abaixo da quantidade.

   Também precisamos ficar atento para:

   Q - x = É o número que o fabricante venderá por mês para que obtenha o lucro máximo, logo,
   Se por exemplo o preço de um produto for de 10 reais e vendessemos 30 unidades dele.
   Q = Quantidade, 
   Q = 30
   x = Preço
   x = 10
   Q - x = 30 - 10 = 20.
   20 é o número de unidades que precisaria ser vendida por mês para que se obtesse o lucro máximo com
   o preço de 10 reais.



  C = Custo de produção
  Q = Quantidade
  x = Preço de venda
  Função custo:
    C(x) = C(Q - x)
  Função receita:
    R(x) = (Q - x) * x
  Função lucro:
    L(x) = R(x) - C(x)
  Logo, temos:
    L(x) = (Q - x) * x - C(Q - x)
    L(x)= Q.x - x² - C.Q + C.x
  :param custo:
  :param venda:
  :return:
  """
  init_printing()
  var('x,y')
  f = Lambda(x, (- x ** 2 + (Q+C)*x - C*Q))
  print("Expressão: " ,f'- x² + {Q+C}.x - {C*Q}')
  derivada = diff(f(x), x)
  print("Derivada: ", derivada)
  preco = solve(derivada)[0]
  print("Preço para obter lucro máximo: ", preco)
  lucro = -preco**2 + (Q+C)*preco - C*Q
  return preco, lucro
bp = Blueprint('view', __name__, template_folder='templates', static_folder='static')

@bp.route('/produce', methods=['GET', 'POST'])
def produce():
  if request.method == 'GET':
    return render_template('produzir.html')
  else:
    product = ProductSchema()
    product_info = request.form.to_dict()
    sold_price, lucro = lucro_max(float(product_info['quantity']), float(product_info['production_cost']))
    if int(sold_price) > int(product_info["quantity"]):
      flash("Para obter o lucro máximo com seu preço, o seu preço deve ser menor que a quantidade.\n"
            "Sua quantidade {}, preço encontrado {}".format(product_info["quantity"], sold_price), "danger")
      return redirect(url_for("view.produce"))
    product_info["sold_price"] = sold_price
    product_info["maximum_profit"] = lucro
    product_load = product.load(product_info)
    Session.add(product_load)
    Session.commit()
    return redirect(url_for('view.list_produtcs'))

@bp.route('/list_produtcs')
@bp.route('/')
def list_produtcs():
  return render_template('lista.html', produtos=Product.query.all())

def init_app(app):
  app.register_blueprint(bp)
