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
build Dockerfile in current directory **.**

```bash
docker build -t image_name .
```
convert image to container run this command 

```bash
docker run --name container_name -p 5000:5000 image_name
```

to removing this image after stop running add --rm to command

```bash
docker run --rm --name container_name -p 5000:5000 image_name
```
**if not work download yolov4.weights from [HERE](https://img.shields.io/steam/downloads/1521424?color=green&label=HERE&style=for-the-badge)(https://github.com/rasoulasadiyan/color-recognition/raw/master/dnn_model/yolov4.weights) and replace with previous file in dnn_model directoty ** 
