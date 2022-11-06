# tehnikum_docker_lecture

## Setup
1. Install virtualenv
```bash
$ virtualenv venv --python=3.8
```
2. Install requirements
```bash
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Run
1. Activate venv
```bash
$ . venv/bin/activate
```
2. Run
```bash
(venv) $ python3 app/main.py
```

###Troubleshoting
`ModuleNotFoundError: No module named 'app'`
Before start run
```bash
$ export PYTHONPATH='/path/to/dir/tehnikum_docker_lecture'
```
Specify your own path to root dir.
