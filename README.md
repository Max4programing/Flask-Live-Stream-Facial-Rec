# Flask-Live-Stream-Facial-Rec
Live stream with password protection. 
To start normal live stream install the needed packages and then run main.py with terminal. 
The Password for the live stream is pass1234.
If you want to run the To run live stream with facial rec go into data set and add folder with your name.
Open headshots.py and change name to the name of your folder. Run this script with terminal. and take 10 pictures (aprox) of your self. After this run train_model.py. Then run facestream.py with terminal. (same password)
To change the password go into static and open password. Change writing with "Var b; and then on next line b = "your password". You can then obsculate this with https://obfuscator.io/. Make sure to save file.
Trouble shooting. If the video dons't work it is probly becasue you are using a web cam change "video = cv2.VideoCapture(0)" to "video = cv2.VideoCapture(2)" in both facestream and main .py files. 
