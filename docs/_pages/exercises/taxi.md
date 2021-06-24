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
- url: /assets/images/exercises/taxi/taxi.png
  image_path: /assets/images/exercises/taxi/taxi.png
  alt: "Taxi."
  title: "Taxi."

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

The objective of this practice is to implement the logic of a Gradient Path Planning (GPP) algorithm. To implement this, we have to divide the exercise in two parts, first we have to select a destination and find the shortest path to it. Once the path has been selected, se have to implement an algorithm to follow this path and reach the destination.

{% include gallery caption="Gallery" %}

You can find all the information about this exercise in [JdeRobot Academy](http://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/)

## Find the shortest path

We have to see the map as a grid. On this grid, we start giving to each box who is over the road a 255 value, for the rest os boxes we assign the 0 value. Now we hace a grid where we can wath our road map "painted" with 255 value.
After this, we have to create an algorithm for the gradient expansion. We are going to start in the destination and put his box value in 0. We have to expand this value to all neighbors adding 1 to current value who are in line and √2 to al diagonals boxes.
{% include gallery id="imageproc" caption="image processing" %}

## CONTROLLER

For the implementation of the control algorithm I have worked with an equation that regulates the angular and linear velocity according to the position in which the center point of the line is located, which I mentioned in the previous section.
I have obtained this equation by assigning a certain speed to each point on the green line.

{% include gallery id="equation" caption="velocity equation" %}

## VIDEO OF THE SOLUTION

[Youtube link](https://www.youtube.com/watch?v=B5lmRhTmefE)

- [X] Lap time simulation: 48 seconds.
- [X] Lap time real: 48 seconds.
