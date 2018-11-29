## Introduction

The purpose of dversion project is to update version in pom file. According to following requirements:

 * It must validate the pom is syntactically correct
 * It must confirm the version is a snapshot prior to making any changes
 * The resulting pom version needs to match this format `ci_{git hub org name here}_{branch name here}-SNAPSHOT`


## Prerequisites

* [docker](https://docs.docker.com/install/)

* [docker-compose](https://docs.docker.com/compose/install/)


## With docker

Build first:
    docker-compose build
### Running

   * using docker 
     ./bin/drun_project `pwd`/tpom.xml -o org -b branch 
      
### Testing

    docker-compose run test


## Without docker

###  Running 

```
  cp pom.xml tpom.xml # top keep original file intact

  ./bin/run_project --org github_org --branch branchName --pom tpom.xml

   #  or directly 

  python -m project --pom tpom.xml -o org -b branch

  diff pom.xml tpom.xml # to see difference 
```

### Testing 
```
  pip install -r test/requirements.txt 
  ./bin/run_tests
```
