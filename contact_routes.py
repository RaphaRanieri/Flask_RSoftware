from flask import Blueprint, request, render_template
from services.contact_service import processar_contato

contact_routes = Blueprint('contact', __name__)

@contact_routes.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')
        # Processa os dados do contato
        resultado = processar_contato(nome, email, mensagem)
        return resultado
    return render_template('contact_form.html')