#!/bin/zsh

curl http://localhost:9001/api/users
curl http://localhost:9001/api/users\?\username\=asd\&email\=asd@bar.com\&password\=asd -X POST
curl http://localhost:9001/api/users\?\username\=moo\&email\=moo@bar.com\&password\=moo -X POST
curl http://localhost:9001/api/login -u "asd:asd"
curl http://localhost:9001/api/users
