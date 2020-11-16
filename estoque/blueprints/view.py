from flask import Blueprint, render_template

bp = Blueprint('details', __name__, template_folder='templates', static_folder='static')

@bp.route('/sell')
def sell():
  return render_template('venda_produto.html')

@bp.route('/insert')
def insert():
  return render_template('inserir_produto.html')

@bp.route('/list')
def list():
  return render_template('lista_produtos.html')

@bp.route('/modify')
def modify():
  return render_template('modificar_produto.html')

def init_app(app):
  app.register_blueprint(bp)
