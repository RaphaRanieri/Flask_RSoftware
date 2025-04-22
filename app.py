from flask import Flask, render_template, request

app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return "Olá! Bem-vindo à aplicação Flask. Acesse a página /contact para deixar seu contato"

# Rota de contato
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')
        return f"Obrigado, {nome}! Sua mensagem foi recebida."
    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)