---
title: Autonomous taxi
layout: archive
permalink: /taxi/

classes: wide

sidebar:
  nav: "docs"

toc: true
toc_label: "TOC Visual Autonomous taxi"
toc_icon: "cog"

<!--- layout: archive --->

<!--- classes: wide --->

gallery:
- url: /assets/images/exercises/taxi/taxi_init.png
  image_path: /assets/images/exercises/taxi/taxi_init.png
  alt: "Taxi"
  title: "Taxi"
- url: /assets/images/exercises/follow_line/formula1.png
  image_path: /assets/images/exercises/follow_line/formula1.png
  alt: "First Person."
  title: "First Person."
- url: /assets/images/exercises/follow_line/formula1_2.png
  image_path: /assets/images/exercises/follow_line/formula1_2.png
  alt: "Model."
  title: "Model."

imageproc:
- url: /assets/images/exercises/follow_line/imageprocc1.png
  image_path: /assets/images/exercises/follow_line/imageprocc1.png
  alt: "Image proccesing."
  title: "Image proccesing."
- url: /assets/images/exercises/follow_line/imageprocc2.png
  image_path: /assets/images/exercises/follow_line/imageprocc2.png
  alt: "Image proccesing."
  title: "Image proccesing."

equation:
- url: /assets/images/exercises/follow_line/geogebra.png
  image_path: /assets/images/exercises/follow_line/geogebra.png
  alt: "equation."
  title: "equation."

---
## GOAL

The goal of this exercise is to perform a PID reactive control capable of following the line painted on the racing circuit.

{% include gallery caption="Gallery" %}

Had to program a Formula1 car in a race circuit to follow the red line in the middle of the road.
You can find all the information about this exercise in [JdeRobot Academy](http://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/)

## IMAGE PROCESSING

For the image processing i have used [OpenCV](https://opencv.org/).
I have searched the center point of the red line at a certain height of the image to work with in in the controller. I have drawn a green line at the same height to see the movement of the point more clearly and a vertical line in the center of the image that determines the place where the point should be. To show the error in the image, I have painted a red line on the green.

{% include gallery id="imageproc" caption="image processing" %}

## CONTROLLER

For the implementation of the control algorithm I have worked with an equation that regulates the angular and linear velocity according to the position in which the center point of the line is located, which I mentioned in the previous section.
I have obtained this equation by assigning a certain speed to each point on the green line.

{% include gallery id="equation" caption="velocity equation" %}

## VIDEO OF THE SOLUTION

[Youtube link](https://www.youtube.com/watch?v=9kCj6eeHf3Y&t=1s)

- [X] Lap time simulation: 48 seconds.
- [X] Lap time real: 48 seconds.
