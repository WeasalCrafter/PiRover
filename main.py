import os
os.system('sudo pigpiod')

from servos import forward,backward,left,right,sleep
from flask import Flask, render_template
#from camera_pi import Camera

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/forward/", methods=["POST"])
def move_forward():
    forward()
    return render_template("index.html")

@app.route("/stop/", methods=["POST"])
def stop():
    sleep()
    return render_template("index.html")

@app.route("/backward/", methods=["POST"])
def move_backward():
    backward()
    return render_template("index.html")

@app.route("/left/", methods=["POST"])
def move_left():
    left()
    return render_template("index.html")

@app.route("/right/", methods=["POST"])
def move_right():
    right()
    return render_template("index.html")

#def gen(camera):
#    while True:
#        frame = camera.get_frame()
#        yield (b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#@app.route('/video_feed')
#def video_feed():
#    return Response(gen(Camera()),
#                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=False, host='10.42.0.1')

os.system('sudo killall pigpiod')
