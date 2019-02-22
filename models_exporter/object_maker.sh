#!/bin/bash
# Opens Blender using templates as files to generate the Models
# from the particles of the scene

#Create a folder to store models
mkdir -p /Users/edgarfigueiras/Desktop/models

#Unpack the zip with all templates
unzip templates.zip -d templates

#Loop to generate all the models reading all the templates
for value in templates/*.blend
do
    ./blender "$value" --background --python exporter.py
done
