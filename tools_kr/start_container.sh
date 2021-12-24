docker start ocrtoc-kr
sudo xhost +local:`docker inspect --format='{{ .Config.Hostname }}' ocrtoc-kr`
