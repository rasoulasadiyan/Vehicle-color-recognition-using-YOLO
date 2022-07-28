# color recognition

vehicle color recognition with yolo trained_model for detect cars in image and K-nearest neighbors algorithm for training colors 

### build Dockerfile

```bash
git clone https://github.com/rasoulasadiyan/color-recognition.git 
```
change directory to repository direct

```bash
cd color_recognition
```
build dockerfile (. is current directory Dockerfile )

```bash
docker build -t image_name .
```
convert image to container run this command :

```bash
docker run --name container_name -p 5000:5000 image_name
```

you can remove this image after stopping add --rm to command


```bash
docker run --rm --name container_name -p 5000:5000 image_name
```
◘**if not work download yolov4.weights from [HERE](https://github.com/rasoulasadiyan/color-recognition/raw/master/dnn_model/yolov4.weights) and paste to dnn_model instead previous file** 
