# OpenGL Project

This project is an OpenGL app made in Python with PyOpenGL and PyGame. It has an OpenGL-rendered cube, a triangular pyramid, and a triangle prism.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Current Shape](#currentShape)
- [Files](#files)
- [Run the application](#runApp)
- [Contributing](#contributing)
- [License](#license)

## Requirements
Python 3.x
PyOpenGL
PyGame

## Installation

Clone the repository:
git clone https://github.com/Godfrey-Marosha/OpenGL-3D-Model-Viewer.git 

cd opengl-project
pip install --user PyOpenGL PyOpenGL_accelerate pygame

## Usage

Use the arrow keys or mouse to rotate the 3D shapes rendered in the window.
Press Esc to exit the application.

## Controls
Spacebar: Cycle through shapes (Cube, Prism, Pyramid)
A: Toggle drawing all shapes at once

## Current Shape
Translation:

Arrow Keys (←, →, ↑, ↓): Translate the model on the x and y axes.
W and S: Translate the model on the z axis.
Rotation:

Q and E: Rotate the model around the x axis.
A and D: Rotate the model around the y axis.
Z and C: Rotate the model around the z axis.
Scaling:

L and J: Scale the model on the x axis.
I and K: Scale the model on the y axis.
U and M: Scale the model on the z axis.
Switching Shapes:

Spacebar: Cycle through different shapes (Cube, Prism, Pyramid)

Press ESC or close the window to exit the program.

## Files
main.py: The main Python script that initializes the OpenGL application.
Cube.py: Contains the vertex and edge information for the cube.
Pyramid.py: Contains the vertex and edge information for the triangular pyramid.
Prism.py: Contains the vertex and edge information for the triangular prism.

## Run the application:
python main.py

## Contributing

[Explain how others can contribute to the project. Include guidelines for submitting pull requests or reporting issues.]


## License

[Specify the license under which the project is distributed.]
