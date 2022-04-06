# Templated repo <!-- Change to repo name! -->

<!-- Insert a very short description of what the script/repo is for -->

<!-- TABLE OF CONTENTS -->
<!--
If VERY heavy readme, update and use this TOC
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
-->

## Description

This code set is build to expose relation between MRID of AMP measurments used for DLR with the MRID Line Segments.
There can be many Amps measurement used for same lime segment as example differnt phases. 
Code set read file in .csv format with header information. There is no limitation for number of coloms for future expansion.
In our case this file generated from ETS application.

This file is cleaned up using python pandas lib and result dataframe is exposed on REST API with Singupy/API.
.csv file is read with a given interval in sec. and can be tunned while running container.

### Exposed environment variables

|Name|Default|Description|
|--|--|--|
|cycle_time|900|cycle to read .csv file|
|database_expose|xxxx|database name to be query from rest api|
|file_name|dlr_mrid_PROD.csv|.csv file to be read|

### File handling / Input

Every cycle_time file_name(env variable) file is read 

### Output

Data exposed via REST API. with database name came be read via

````bash
curl -X POST http://localhost:port -H 'Content-Type: application/json' -d '{"sql-query": "SELECT * FROM database_expose;"}
````
-->

<!-- GETTING STARTED -->
## Getting Started

This code set is build to expose relation between MRID of AMP measurments used for DLR with the MRID Line Segments.
There can be many Amps measurement used for same lime segment as example differnt phases. 
Code set read file in .csv format with header information. There is no limitation for number of coloms for future expansion.
In our case this file generated from ETS application.

This file is cleaned up using python pandas lib and result dataframe is exposed on REST API with Singupy/API.
.csv file is read with a given interval in sec. and can be tunned while running container.

### Dependencies

https://github.com/energinet-singularity/singupy
  
#### Python (if not run as part of the container)

This python script can probably run on any python 3.9+ version, but your best option will be to check the Dockerfile and use the same version as the container. Further requirements (python packages) can be found in the app/requirements.txt file.

#### Docker

<!--
Describe here what is needed before it can be run in docker - environment variables, volumes etc.

Give an example if relevant:

Example:
```sh
docker run my_script -v someVolume:/data -e MYVAR=smith"
```
 -->
Built and tested on version 20.10.7.


#### HELM (only relevant if using HELM for deployment)

<!--
Describe here what is needed before it can be run in docker - environment variables, volumes etc.

You could use this:
The default helm values/properties are set in a way that allows the helm chart to be installed and run without crashes, but it will not be useful. To spin up the environment with helm, make sure to set (or overwrite) values to something meaningful.
-->
Built and tested on version 3.7.0.

### Running container

<!-- PLEASE REMEMBER TO UPDATE THIS GUIDE!!! -->

1. Clone the repo to a suitable place
````bash
git clone https://github.com/energinet-singularity/dlr-mrid.git
````

2. Build the container
````bash
docker build dlr_mrid/ -t dlr_mrid:latest
docker volume create XXXX
````

3. Start the container in docker (change variables to fit your environment)
````bash
docker run -v XXX:/dlr_mrid_PROD.csv -e cycle_time=900 --rm dlr_mrid:latest
docker run -v XXX:/dlr_mrid_PROD.csv -e cycle_time=900 -e database_expose="testdata" --rm dlr_mrid:latest
````

## Help
<!-- replace 'open issues' below with link like this: [open issues](https://github.com/energinet-singularity/<repo-name>/issues) -->
See the open issues for a full list of proposed features (and known issues).
If you are facing unidentified issues with the application, please submit an issue or ask the authors.

## Version History

* 0.0.1:
    * First ever version - nice!

## License

This project is licensed under the Apache-2.0 License - see the LICENSE and NOTICE file for further details.
