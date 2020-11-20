from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions.serializer import ManufacturerSchema, ProductSchema
from ..extensions.database import Session
from ..extensions.database import Manufacturer
from ..extensions.database import Product
from sympy import var, diff, Lambda, solve, init_printing

def lucro_max(Q, C):
  """
  Q = Quantidade
  C = Custo
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
    sold_price, lucro = lucro_max(int(product_info['quantity']), int(product_info['production_cost']))
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
