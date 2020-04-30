from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def retorna_ok():
    return 'OK!'

@app.route('/site_de_filmes')
def site_de_filmes():
    filme = request.args.get('filme')
    return '<h1>O filme procurado foi: {}</h1>'.format(filme)

if __name__ == '__main__':
    app.run(debug=True, port=5000)