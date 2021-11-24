# Training

## Server

update ubuntu
```
sudo apt update
```

install python3 for ubuntu (link)[https://www.python.org/download/releases/3.0/]
```
sudo apt install python3.8
```

install pip3 for ubuntu
```
sudo apt-get -y install python3-pip
```

run install python dependency
```
cd to_project_directory
pip3 install -r requirements.txt
```

Config some connection

start server
```
python3 server.py
```

## Web from

start web
```
cd to_project_directory
python3 -m http.server
```

open web via ip in your browser