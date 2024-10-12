from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_visitor_ip():
    # Hol die IP-Adresse des Besuchers
    visitor_ip = request.remote_addr
    return f'Die IP-Adresse des Besuchers ist: {visitor_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
