#!/usr/bin/env bash

nosetests --with-coverage \
          --cover-erase --cover-html \
          --cover-package circular_references $1 $2
