### Hexlet tests and linter status:
[![Actions Status](https://github.com/Goglich/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Goglich/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/ac1d05116a57935b7b26/maintainability)](https://codeclimate.com/github/Goglich/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/ac1d05116a57935b7b26/test_coverage)](https://codeclimate.com/github/Goglich/python-project-50/test_coverage)

## About gendiff
gendiff is a program that prints the differences between two json/yaml files.

## System requirements
- python 3.10+
- poetry
- git

## How to install?
```git clone git@github.com:Goglich/python-project-50.git```
```cd python-project-50```
```make package-install```
[![asciicast](https://asciinema.org/a/GMGLuXM2sT6KutbHjaHUqVscu.svg)](https://asciinema.org/a/GMGLuXM2sT6KutbHjaHUqVscu)

## Displaying help information
```gendiff -h```
[![asciicast](https://asciinema.org/a/Q0rerWDnvBoGYJxtgo4LGOuap.svg)](https://asciinema.org/a/Q0rerWDnvBoGYJxtgo4LGOuap)

## Comparison of "flat" files
```gendiff tests/fixtures/file1.json tests/fixtures/file2.json```
```gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml```
[![asciicast](https://asciinema.org/a/GTQcKP8vtpixEx09yiCSU3hkv.svg)](https://asciinema.org/a/GTQcKP8vtpixEx09yiCSU3hkv)

## Comparison of "nested" files
```gendiff tests/fixtures/file3.json tests/fixtures/file4.json```
```gendiff tests/fixtures/file3.yaml tests/fixtures/file4.yaml```
[![asciicast](https://asciinema.org/a/Et4a7R1Wk93yeSKDg1EcPCTcs.svg)](https://asciinema.org/a/Et4a7R1Wk93yeSKDg1EcPCTcs)

## Display in plain format
```gendiff -f plain tests/fixtures/file3.yaml tests/fixtures/file4.yaml```
[![asciicast](https://asciinema.org/a/GRjTfS23lDjxFwLMke7Ha80Zf.svg)](https://asciinema.org/a/GRjTfS23lDjxFwLMke7Ha80Zf)

## Display in json format
```gendiff -f json tests/fixtures/file3.yaml tests/fixtures/file4.yaml```
[![asciicast](https://asciinema.org/a/esk4PofM8pp3qUGWP89U8tof1.svg)](https://asciinema.org/a/esk4PofM8pp3qUGWP89U8tof1)