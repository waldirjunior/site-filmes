from flask import Flask, request
import json
import requests

app = Flask(__name__)

api_token = 'c158b2f342a0f004be2bf12d2a039b42'
api_url_base = 'https://api.themoviedb.org/3/search/movie?'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer{0}'.format(api_token)}

#Solução encontada para mostrar busca da API
@app.route('/filmes')
def filmes():
    token ='api_key=c158b2f342a0f004be2bf12d2a039b42'
    idioma = '&language=en-US'
    nome_filme = '&query=avatar&'
    outros = 'page=1&include_adult=false'
    api_url = '{}{}{}{}{}'.format(api_url_base, token, idioma, nome_filme, outros)
    response = requests.get(api_url, headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('UTF-8'))
    else:
        return None
# final da função

@app.route('/')
def retorna_ok():
    return 'OK!'

@app.route('/site_de_filmes')
def site_de_filmes():
    filme = request.args.get('filme')
    return '<h1>O filme procurado foi: {}</h1>'.format(filme)

if __name__ == '__main__':
    app.run(debug=True, port=5000)