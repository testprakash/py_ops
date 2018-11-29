## Introduction

The purpose of dversionproject is to update version in pom file. According to following requirements:
 * It must validate the pom is syntactically correct
 * It must confirm the version is a snapshot prior to making any changes
 * The resulting pom version needs to match this format `ci_{git hub org name here}_{branch name here}-SNAPSHOT`


## Prerequisites

* [docker](https://www.docker.com/)

## Running the Application

    docker-compose build
    docker-compose run project <command line arguments>

## Testing

    docker-compose run test


## Running tests manualy

cd dversion 
python -m tests

