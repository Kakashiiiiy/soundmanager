#!/bin/sh
pacmd stat | awk -F": " '/^Default sink name: /{print $2}'