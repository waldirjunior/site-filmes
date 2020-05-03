from flask import Blueprint


buscas = Blueprint('sitefilmes', __name__)

@buscas.route('/teste-blueprint')
def api_busca_personalizada():
    return "Testando"

