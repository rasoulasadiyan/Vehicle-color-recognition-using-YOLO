# color recognition

vehicle color recognition with yolo trained_model for detect cars in image and K-nearest neighbors algorithm which is trained by R, G, B Color Histogram. It can classify White, Black, Red, Green, Blue, Orange, Yellow, Gray, Brown and Violet

### Build Dockerfile

#### 1. 
```bash
git lfs clone https://github.com/rasoulasadiyan/color-recognition.git 
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
docker run --rm --name container_name -p 5000:5000 image_name
```


### If everything goes well, the app is running on localhost port 5000
