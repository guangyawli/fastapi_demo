# Overview
Pull MySQL from DockerHub and build Fast API environment with DockerCompose

# Install
Create and Running
```
$ docker-compose up --build
```

# Demo
## Document of API
http://localhost:8000/docs

You can try upload , listFiles, 
upload files would save into project/data folder

## ex) upload
```
$ curl -X 'POST' 'http://localhost:8000/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@kern.log;type=text/x-log'
```
Result
```
{
  "file_name": "kern.log",
  "file_size": "903.48KB",
  "file_type": "text/x-log",
  "file_path": "/usr/src"
}
```
## ex) listFiles
```
$ curl -X 'GET' 'http://localhost:8000/listFiles' -H 'accept: application/json'
```

Result
```
[
  {
    "id": 1,
    "file_path": "/usr/src",
    "file_type": "application/octet-stream",
    "file_name": "dmesg",
    "file_size": "47.67KB"
  },
  {
    "id": 2,
    "file_path": "/usr/src",
    "file_type": "text/x-log",
    "file_name": "kern.log",
    "file_size": "903.48KB"
  }
]
```
