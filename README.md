# django_oauth
Google OAuth2.0 integration with a Django app

## Requirements

1. Python 3.8
1. Docker

## Usage

To setup and run the app in the Docker containers, run below command from the root directory:

    `make all`

This will install all the pre-requisites and build the docker images and finally launch the containers.

You can then access the application in your browser by opening the address:

    http://localhost/

        OR

    http://127.0.0.1/


To kill the app, stop and destroy the containers, run the command:

    `make nuke-it-all`
