---
title: Follow Line
layout: archive
permalink: /follow_line/

classes: wide

sidebar:
  nav: "docs"

toc: true
toc_label: "TOC Visual Follow Line"
toc_icon: "cog"

<!--- layout: archive --->

<!--- classes: wide --->

gallery:
- url: /assets/images/exercises/follow_line/formula1_circuit.png
  image_path: /assets/images/exercises/follow_line/formula1_2.png
  alt: "Racing circuit"
  title: "Racing circuit"
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
---
## GOAL

The goal of this exercise is to perform a PID reactive control capable of following the line painted on the racing circuit.

{% include gallery caption="Gallery" %}

Had to program a Formula1 car in a race circuit to follow the red line in the middle of the road.
You can find all the information about this exercise in [JdeRobot Academy](http://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/)

## Image processing

For the image processing i have used [OpenCV](https://opencv.org/).
I have searched the center point of the red line at a certain height of the image to work with in in the controller. I have drawn a green line at the same height to see the movement of the point more clearly and a vertical line in the center of the image that determines the place where the point should be. To show the error in the image, I have painted a red line on the green.

{% include gallery id="imageproc" caption="image processing" %}
