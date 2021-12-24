sudo docker rm -f ocrtoc-kr

sudo docker run -i -d --gpus all --name ocrtoc-kr --network host \
        --privileged -v /dev:/dev -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v $HOME/Desktop/docker:/root/upload \
        aiforfactory/ocrtoc2021:1
sudo xhost +local:`docker inspect --format='{{ .Config.Hostname }}' ocrtoc-kr`
