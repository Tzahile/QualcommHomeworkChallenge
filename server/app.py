from flask import Flask
from routes.versions import mainPage, GetVersions, ModifyVersion

app = Flask(__name__,
            template_folder='./dist',
            static_folder='./dist/static')


@app.route('/', methods=['GET'])
def Main():
    return mainPage()


@app.route('/versions', methods=['GET'])
def Versions():
    return GetVersions()


@app.route('/versions/<id>', methods=['POST', 'DELETE', 'PUT'])
def Version(id):
    return ModifyVersion(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
