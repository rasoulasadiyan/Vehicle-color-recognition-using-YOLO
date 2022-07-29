# color recognition

vehicle color recognition with yolo trained_model for detect cars in image and K-nearest neighbors algorithm for training colors 

### Build Dockerfile

#### 1. 
```bash
git clone https://github.com/rasoulasadiyan/color-recognition.git 
```
#### 2. change directory to repository direct

```bash
cd color_recognition
```
#### 3. build Dockerfile in current directory **.**

```bash
docker build -t image_name .
```
#### 4. convert image to container run this command 

```bash
docker run --name container_name -p 5000:5000 image_name
```

#### 5. to removing this image after stop running add --rm to command

```bash
docker run --rm --name container_name -p 5000:5000 image_name
```
**if not work [download zip this repository](https://github.com/rasoulasadiyan/color-recognition/archive/refs/heads/master.zip) and download yolov4.weights from [HERE](https://github.com/rasoulasadiyan/color-recognition/raw/master/dnn_model/yolov4.weights) then replace with previous file in dnn_model directoty** 

.If everything goes well, the app is running on localhost port 5000
