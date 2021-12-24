docker start ocrtoc-whu
sudo xhost +local:`docker inspect --format='{{ .Config.Hostname }}' ocrtoc-whu`
