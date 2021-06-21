#!/bin/sh

teardown_containers() {
  local environment=$1

case $environment in
    'development')
      docker-compose build
      docker-compose run app /bin/sh scripts/setup_app.sh
    ;;
  esac

}