from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name': 'Javascript'}, {'name': 'swift'}, {'name': 'python'}]


@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works'})


@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
    language = request.get_json('name')
    languages.append(language)
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):

    langs = []
    for l in languages:
        if l['name'] == name:
            langs.append(l)
    print(langs)
    langs[0]['name'] = request.get_json(['name'])
    return jsonify({'language': langs[0]})


if __name__ == '__main__':
    app.run(port=8080)
