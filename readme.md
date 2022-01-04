### Code-010320220-amiya_mandal
#### dev env
1. python==3.9

##### to run code
```bash
$ python dev.py
```

#### deployment env
1. docker

##### to run code
```bash
$ docker build -t bmi_cal .
$ docker run -dp 8000:8000 bmi_cal
```
#### test case run
```bash
$ pip install -r requirements.txt
$ pytest
```
