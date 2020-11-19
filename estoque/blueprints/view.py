from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions.serializer import ManufacturerSchema, ProductSchema
from ..extensions.database import Session, Manufacturer

bp = Blueprint('view', __name__, template_folder='templates', static_folder='static')

def lucro_max(quantidade_produto, custo_produto ):
  # Q = Quantidade
  # C = Custo
  # L(x) = (Q - x) * x - C(Q - x)
  # L(x)= Q.x - x² - C.Q + C.x
  ...



@bp.route('/produce', methods=['GET', 'POST'])
def produce():
  if request.method == 'GET':
    return render_template('produzir.html')
  else:
    product = ProductSchema()
    product_info = request.form.to_dict()
    product_load = product.load(product_info)
    Session.add(product_load)
    Session.commit()
    return redirect(url_for('view.list_produtcs'))

@bp.route('/list_produtcs')
@bp.route('/')
def list_produtcs():
  return render_template('lista.html')

def init_app(app):
  app.register_blueprint(bp)
