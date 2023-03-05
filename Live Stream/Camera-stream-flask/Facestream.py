

# stop the timer and display FPS information
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
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2

#Initialize 'currentname' to trigger only when a new person is identified.

#Determine faces from encodings.pickle file model created from train_model.py
encodingsP = "encodings.pickle"

# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(encodingsP, "rb").read())

# initialize the video stream and allow the camera sensor to warm up
# Set the ser to the followng
# src = 0 : for the build in single web cam, could be your laptop webcam
# src = 2 : I had to set it to 2 inorder to use the USB webcam attached to my laptop
#vs = VideoStream(src=2,framerate=10).start()
video = cv2.VideoCapture(0)
time.sleep(2.0)

# start the FPS counter
fps = FPS().start()

# loop over frames from the video file stream


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
    # loop over frames from the video file stream
    currentname = "unknown"
    while True:
            # grab the frame from the threaded video stream and resize it
            # to 500px (to speedup processing)
            sus,frame = video.read()
            frame = imutils.resize(frame, width=500)
            # Detect the fce boxes
            boxes = face_recognition.face_locations(frame)
            # compute the facial embeddings for each face bounding box
            encodings = face_recognition.face_encodings(frame, boxes)
            names = []

            # loop over the facial embeddings
            for encoding in encodings:
                    # attempt to match each face in the input image to our known
                    # encodings
                    matches = face_recognition.compare_faces(data["encodings"],
                            encoding)
                    name = "Unknown" #if face is not recognized, then print Unknown

                    # check to see if we have found a match
                    if True in matches:
                            # find the indexes of all matched faces then initialize a
                            # dictionary to count the total number of times each face
                            # was matched
                            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                            counts = {}

                            # loop over the matched indexes and maintain a count for
                            # each recognized face face
                            for i in matchedIdxs:
                                    name = data["names"][i]
                                    counts[name] = counts.get(name, 0) + 1

                            # determine the recognized face with the largest number
                            # of votes (note: in the event of an unlikely tie Python
                            # will select first entry in the dictionary)
                            name = max(counts, key=counts.get)

                            #If someone in your dataset is identified, print their name on the screen
                            if currentname != name:
                                    currentname = name
                                    print(currentname)

                    # update the list of names
                    names.append(name)

            # loop over the recognized faces
            for ((top, right, bottom, left), name) in zip(boxes, names):
                    # draw the predicted face name on the image - color is in BGR
                    cv2.rectangle(frame, (left, top), (right, bottom),
                            (0, 255, 225), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                            .8, (0, 255, 255), 2)
            ret,jpeg = cv2.imencode('.jpg', frame)
            image = jpeg.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n\r\n')

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
