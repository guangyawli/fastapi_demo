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
curl -X 'POST' \
  'http://localhost:8000/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@dmesg.0'
```
Result
```
{
  "file_name": "dmesg.0",
  "file_size": "47.67KB",
  "file_type": "application/octet-stream",
  "file_path": "/upload_files/"
}
```
## ex) listFiles
```
curl -X 'GET' \
  'http://localhost:8000/listFiles' \
  -H 'accept: application/json'
```

Result
```
[
  {
    "file_type": "application/octet-stream",
    "file_name": "vboxadd-setup.log.2",
    "file_size": "44.12KB"
  },
  {
    "file_type": "application/octet-stream",
    "file_name": "vboxadd-setup.log.4",
    "file_size": "44.12KB"
  },
  {
    "file_type": "application/octet-stream",
    "file_name": "dmesg.0",
    "file_size": "47.67KB"
  }
]
```
