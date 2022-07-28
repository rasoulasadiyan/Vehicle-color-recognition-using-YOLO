import string
from flask import Flask,request,url_for,render_template,flash,redirect
from imageio import imsave,imread
import os
import base64
import numpy as np
import cv2
import werkzeug
from flask import json
from werkzeug.exceptions import HTTPException
from flask import abort
global model,graph
from vehicle_detector import VehicleDetector
from PIL import Image
from color_classification_image import recegnizion_color

vd = VehicleDetector()

path=os.path.join('static','Uploads')
os.makedirs(path,exist_ok=True)

img_folder='static/Uploads'
allowed_types={'png','jpg'}

def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.')[-1].lower() in allowed_types


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('img_upload.html')

@app.route('/',methods=['POST'])
def upload():
    if 'img_file' not in request.files:
        msg='img_file not in request.files.'
        return render_template('msg.html',massage=msg)
        
    else:
        file=request.files['img_file']
      
        try:
            if allowed_file(file.filename):
                file.save(os.path.join('static/Uploads/' + file.filename))

                global img_name
                img_name=file.filename
                return render_template('img_upload.html' ,_img=file.filename)
            else:
                msg="file format must be '.png' or '.jpg' "
                return render_template('msg.html',massage = msg)

        except Exception as ex:
            
            return redirect(request.url)

@app.route('/')
def display(filename):
    img=Image.open('/static/Uploads/detect.jpg')
    w=img.width
    h=img.height

    return render_template('img_upload.html',_img= filename,img_size=[w,h])


@app.route('/detect_car',methods=['POST'])
def detect_car():
    
    path='static/Uploads/' + img_name
    img=cv2.imread(path)

    vehicle_boxes = vd.detect_vehicles(img)
    imag_for_crop=Image.open(path)
    i=1
    if( len(vehicle_boxes) == 0) :

        w2=imag_for_crop.width
        h2=imag_for_crop.height
        x2=int(w2/2)
        y2=int(h2/2)

        name='croped'+str(i)
        imag_for_crop.save(f'static/detect_car_images/{name}.jpg')

        with open('croped_images_coordinates.txt', 'w') as myfile:
                myfile.write(str(x2/3) + ',' + str(y2/1.5) + ',' + str(x2 + w2/3) + ',' + str(y2 + h2/5) + '\n')
        i+=1
    else:
        myfile = open('croped_images_coordinates.txt', 'w')
        for box in vehicle_boxes:
            x, y, w, h = box
            img=cv2.rectangle(img, (x, y), (x + w, y + h), (50, 150, 180), 3)

            croped_image=imag_for_crop.crop((x,y,x+w,y+h))

            w2=croped_image.width
            h2=croped_image.height
            x2=int(w2/2)
            y2=int(h2/2)

            name='croped'+str(i)
            croped_image.save(f'static/detect_car_images/{name}.jpg')
            
            
            myfile.write(str(x2/3) + ',' + str(y2/1.5) + ',' + str(x2 + w2/3) + ',' + str(y2 + h2/5) + '\n')

            i+=1

        myfile.close()

    cv2.imwrite('static/detect_car_images/detected.jpg',img)

    global predict
    prediction=recegnizion_color(i)
    result=str(prediction)

    return render_template('msg.html',massage=result)


@app.route('/detect_car/recegnize_color',methods=['POST'])
def recegnize_color():
    pre=predict
    return render_template('msg.html',massage=pre)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')