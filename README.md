# Harvest Data Validator

A command line tool used to validate crop harvest data and return data points that have issues.

## Prerequisite

* For Docker deployment option:
  * Docker Engine
  * OS: Windows, macOS, your preferred Linux Distro (Ubuntu in my case) 
* For pyenv deployment option:
  * Python 3.7+
  * Unix-based Operating System - MacOS, Ubuntu

## Deployment

### Docker

* Install Docker depending on your operating system's requirements
* Go to root of the project
* Build the docker image: `docker build -t harvest_validator:latest .`
* Use the new Docker image to run an interactive container to process the data:

```bash
docker run -v /path/to/harvest/data:/app/data -it harvest_validator python run.py --folder=./data

```

For the `docker run -v` flag this involves mounting the data folder source on the host machine to the `/app/data` folder in the Docker container.

The above command will provide data in the following format per the specified check:

```json
{
   "violation_rule":"",
   "data":[
      {
         "farm_id":"",
         "crop":"",
         "location":"",
         "wet_weight":0.0,
         "dry_weight":0.0
      },
      {
         "farm_id":"",
         "crop":"",
         "location":"",
         "wet_weight":0.0,
         "dry_weight":0.0
      }
   ]
}
```

For example, to check where the dry weight measurement exceeds the corresponding wet weight measurement, the following is the response:

```json
{
   "violation_rule":"Dry weight exceeds corresponding wet weight",
   "data":[
      {
         "farm_id":"91a23192111b",
         "crop":"sorghum",
         "location":"-1.1907708187237365, 36.81878372676805",
         "wet_weight":41.04,
         "dry_weight":42.21
      }
   ]
}
```

### Pyenv Deployment

* Install pyenv for your specified Operating System environment
* Install virtualenv for pyenv via the `pyenv-virtualenv` [plugin](https://github.com/pyenv/pyenv-virtualenv)
* Install virtual environment for a specific Python version: `pyenv virtualenv 3.8.3 harvest-data-validator`
* Activate the virtual environment: `pyenv activate harvest-data-validator`
* Run the following command to process and validate the harvest data:

```bash
python run.py --folder=/path/to/harvest/data
```


### Results

The following checks have been implemented to validate the harvest data and check for submissions that break a rule:

1. Flag all submissions where there are multiple measurements for the same crop in a single farm
2. Flag all submissions where the dry weight measurement exceeds the corresponding wet weight measurement
3. Flag all submissions where the dry weight is outside the standard deviation of all other submissions for the same crop

