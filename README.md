## Introduction

The purpose of dversion project is to update version in pom file. According to following requirements:
 * It must validate the pom is syntactically correct
 * It must confirm the version is a snapshot prior to making any changes
 * The resulting pom version needs to match this format `ci_{git hub org name here}_{branch name here}-SNAPSHOT`


## Prerequisites

* [docker](https://www.docker.com/)


## With docker

### Running

    docker-compose build
    docker-compose run project <command line arguments>

### Testing

    docker-compose run test


## Without docker

###  Running 

```
  ./bin/run_project
```

### Testing 
```
  ./bin/run_tests
```
