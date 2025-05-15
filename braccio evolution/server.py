from flask import Flask, request, render_template
from flask_cors import CORS
import serial

app = Flask(__name__)
CORS(app)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

@app.route('/')
def home():
    return render_template('Fattobene.html')  # serve la tua pagina HTML

@app.route('/move', methods=['POST'])
def move():
    print("Content-Type ricevuto:", request.content_type)
    data = request.get_json(force=True)
    angle1 = data.get('angolo1')
    angle2 = data.get('angolo2')

    if angle1 is None or angle2 is None:
        return {'status': 'errore', 'msg': 'angoli mancanti'}, 400

    command = f"{angle1},{angle2}\n"
    print("Invio al seriale:", command)
    ser.write(command.encode())

    return {'status': 'successo'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
