## Introduction

The purpose of dversion project is to update version in pom file. According to following requirements:

 * It must validate the pom is syntactically correct
 * It must confirm the version is a snapshot prior to making any changes
 * The resulting pom version needs to match this format `ci_{git hub org name here}_{branch name here}-SNAPSHOT`


## Prerequisites

* [docker](https://docs.docker.com/install/)

* [docker-compose](https://docs.docker.com/compose/install/)


## With docker

### Running

    docker-compose build
    docker-compose run dversion <command line arguments>
    docker run -it dversion_dversion
### Testing

    docker-compose run test


## Without docker

###  Running 

```
  ./bin/run_project --org github_org --branch branchName --pom pom.xml
```

### Testing 
```
  ./bin/run_tests
```
