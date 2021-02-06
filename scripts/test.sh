#!/bin/bash

export PYTHONPATH=src

# run tests
coverage run --source=./src/ -m pytest tests/
unit_test_result=$?

# generate reports
coverage report -m
coverage html -d htmlcov_unit

if [ $unit_test_result -ne 0 ]; then
    echo Tests Failed
    exit 1
fi
