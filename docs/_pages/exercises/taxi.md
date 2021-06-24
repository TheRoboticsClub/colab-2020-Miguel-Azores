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
- url: /assets/images/exercises/taxi/weights.png
  image_path: /assets/images/exercises/taxi/weights.png
  alt: "Wafe front"
  title: "Wafe front"

path:
- url: /assets/images/exercises/taxi/pathExample.png
  image_path: /assets/images/exercises/taxi/pathExample.png
  alt: "path"
  title: "path"

---
## GOAL

The objective of this practice is to implement the logic of a Gradient Path Planning (GPP) algorithm. To implement this, we have to divide the exercise in two parts, first we have to select a destination and find the shortest path to it. Once the path has been selected, se have to implement an algorithm to follow this path and reach the destination.

{% include gallery caption="Gallery" %}

You can find all the information about this exercise in [JdeRobot Academy](http://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/)

## Create a grid with a Front Wave algorithm.

We have to see the map as a grid. On this grid, we start giving to each box who is over the road a 255 value, for the rest os boxes we assign the 0 value. Now we hace a grid where we can wath our road map "painted" with 255 value.
After this, we have to create an algorithm for the gradient expansion. We are going to start in the destination and put his box value in 0. We have to expand this value to all neighbors adding 1 to current value who are in line and √2 to al diagonals boxes. We have one wave front array to expand our wave, each iteration we increment the value of the cells.

## Find the shortest path

When we have our grid with values of weights for each grid starting in the target an finishing in our taxi, we can create the shortest path. To do this, we are goins to start in the car position and, iteratively, we want always the lowest value around the position, just with one wafe front. This algorithm give us the shortest path walking over the lowest values of each iteration. The image below will be a good exaple of this algoritm.

{% include gallery id="path" caption="path example" %}

## Follow path

To follow the path, we take two angles and compare them. The first angle is the orientation of the car in terms of the global map. The second one is the angle of the lowest point of the gradient, to the car. With these two angles we will know how much has to rotate the car and his direction. To define the lineal velocity y had set a constant value. If angular velocity is high, low lineal speed.

## VIDEO OF THE SOLUTION

[Youtube link](https://www.youtube.com/watch?v=B5lmRhTmefE)
