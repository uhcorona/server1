import requests

from flask import Flask, request
from flask import Response

app = Flask(__name__)

urla = 'http://18.218.132.156/'
urlb = 'http://3.16.203.164/'

@app.route('/notes', methods=['POST'])
def postNote():
    cpu1 = requests.get(urla+'cpuusage').json()['usedcpu']
    cpu2 = requests.get(urlb+'cpuusage').json()['usedcpu']

    ram1 = requests.get(urla+'ramusage').json()['usedram']
    ram2 = requests.get(urlb+'ramusage').json()['usedram']
    
    n1 = requests.get(urla+'nnotes').json()['elements']
    n2 = requests.get(urlb+'nnotes').json()['elements']

    if n1 > n2 :
        requests.post(urlb + 'notes', data = request.data)
    elif n1 < n2 :
        requests.post(urla + 'notes', data = request.data)
    elif n1 == n2:
        if ram1 > ram2 :
            requests.post(urlb + 'notes', data = request.data)
        elif ram1 < ram2 :
            requests.post(urla + 'notes', data = request.data)
        elif ram1 == ram2:
            if cpu1 > cpu2 :
                requests.post(urlb + 'notes', data = request.data)
            elif cpu1 < cpu2 :
                requests.post(urla + 'notes', data = request.data)
            elif cpu1 == cpu2:
                requests.post(urla + 'notes', data = request.data)



    return Response(response = "{\"res\": \"true\"}", status=200, mimetype="application/json")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port = 4000)
