# Face recognition
This includes 3 steps
1. [Face detection] - This is whereby we detect a face in an image/video.
2. [Feature extraction using face embedding] --This is whereby we extract features from a face using a face embedding model.
3. [Facial recognition] - Here we pass a face to our system, it calculates the embedding and compares it to the faces we already have. In the end a face is recognized if its embedding mtaches a face already in the database. 

Libraries used in this project are;
a) Opencv
b) dlib
c) face_recognition