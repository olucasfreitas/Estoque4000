from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions.serializer import ProviderSchema, ProductSchema
from ..extensions.database import db, Provider

bp = Blueprint('view', __name__, template_folder='templates', static_folder='static')

@bp.route('/buy_products', methods=['GET', 'POST'])
def buy():
  if request.method == 'GET':
    providers = Provider.query.all()
    return render_template('comprar_produto.html', providers=providers)
  else:
    product = ProductSchema()
    product_info = request.form.to_dict()
    product_load = product.load(product_info)
    db.session.add(product_load)
    db.session.commit()
    return redirect(url_for('view.list_produtcs'))

@bp.route('/create_provider', methods=['GET', 'POST'])
def create_provider():
  if request.method == 'GET':
    return render_template('criar_fornecedor.html')
  else:
    provider = ProviderSchema()
    provider_info = request.form.to_dict()
    provider_load = provider.load(provider_info)
    db.session.add(provider_load)
    db.session.commit()
    return redirect(url_for('view.list_produtcs'))

@bp.route('/list_produtcs')
def list_produtcs():
  return render_template('lista.html')

def init_app(app):
  app.register_blueprint(bp)
