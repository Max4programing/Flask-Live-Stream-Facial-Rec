#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application streamerves aender_temmotion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import os
from datetime import datetime
video = cv2.VideoCapture(0)





# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('final2.html') #you can customze index.html here
@app.route('/ydghjsgfbjke,jfl;.,fmmdnbhhejgfjhmncbvdbnvnbc', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('index1.html')
@app.route('/secert', methods=['GET', 'POST'])
def secert():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('web.html')

def gen(video):
    while True:
        sus,image = video.read()
        ret,jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
# Take a photo when pressing camera button
@app.route('/picture')
def take_picture():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    sus,image = video.read()
    filename = current_time+".png" 
    cv2.imwrite(filename,image)
    return "None"

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
