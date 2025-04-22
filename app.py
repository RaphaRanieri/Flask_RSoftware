from flask import Flask

app = Flask(__name__)

#Rota principal
@app.route('/')
def home():
    return "Olá! Bem-vindo à aplicação Flask."

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
