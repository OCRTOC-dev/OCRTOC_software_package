sudo docker rm -f ocrtoc-whu

sudo docker run -i -d --gpus all --name ocrtoc-whu --network host \
        --privileged -v /dev:/dev -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v $HOME/Desktop/docker:/root/upload \
        -v $HOME/OCRTOC_software_package/ocrtoc_materials:/root/ocrtoc_ws/src/ocrtoc_materials \
        -v $HOME/OCRTOC_software_package/ocrtoc_task:/root/ocrtoc_ws/src/ocrtoc_task \
        registry.cn-hangzhou.aliyuncs.com/wuhan_chalmers/ocrtoc_solutions:11_30
sudo xhost +local:`docker inspect --format='{{ .Config.Hostname }}' ocrtoc-whu`
