
import sys
import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

# Inject Aurelio into path
BACKEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'aurelio'))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from core import orchestrator
from database import db
from models import model_manager

# Init Aurelio
try:
    orchestrator.inicializar_sistema()
    GLOBAL_SESSION = orchestrator.nova_sessao()
except Exception as e:
    print('Erro ao inicializar Aurelio:', e)
    GLOBAL_SESSION = 'default'

class SecondBrainHandler(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, 'ok')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            mensagem = data.get('mensagem', '')
            
            try:
                resultado = orchestrator.pipeline_principal(mensagem, GLOBAL_SESSION)
            except Exception as e:
                resultado = {'resposta': f'Erro: {str(e)}'}
                
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(resultado).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(port=8765):
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, SecondBrainHandler)
    print(f'Starting Second Brain API + Static Server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    run(port)

