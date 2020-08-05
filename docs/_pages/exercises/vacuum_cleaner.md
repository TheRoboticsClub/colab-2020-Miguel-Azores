---
title: Vacuum Cleaner
layout: archive
permalink: /vacuum_cleaner/

classes: wide

sidebar:
  nav: "docs"

toc: true
toc_label: "TOC Visual Vacuum_cleaner"
toc_icon: "cog"

<!--- layout: archive --->

<!--- classes: wide --->

gallery:
- url: /assets/images/exercises/vacuum_cleaner/vacuum_cleaner.png
  image_path: /assets/images/exercises/vacuum_cleaner/vacuum_cleaner.png
  alt: "Vacuum init"
  title: "Vacuum init"
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

The goal of this exercise is to implement the logic of a navigation algorithm for an autonomous vacuum. The main objective will be to cover the largest area of ​​a house using the programmed algorithm.

{% include gallery caption="Gallery" %}

You can find all the information about this exercise in [JdeRobot Academy](http://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/)

## THEORY

Implementation of navigation algorithms for an autonomous vacuum is the basic requirement for this exercise. The main objective is to cover the largest area of a house. First, let us understand what is Coverage Algorithms.

*Coverage Algorithms*
Coverage Path Planning is an important area of research in Path Planning for robotics, which involves finding a path that passes through every reachable position in its environment. In this exercise, We are using a very basic coverage algorithm called Random Exploration.

{% include gallery id="imageproc" caption="image processing" %}

## MY IMPLEMENTATION

For the implementation of the control algorithm I have worked with an equation that regulates the angular and linear velocity according to the position in which the center point of the line is located, which I mentioned in the previous section.
I have obtained this equation by assigning a certain speed to each point on the green line.

{% include gallery id="equation" caption="velocity equation" %}

## VIDEO OF THE SOLUTION

[Youtube link](https://www.youtube.com/watch?v=9kCj6eeHf3Y&t=1s)

- [X] Lap time simulation: 48 seconds.
- [X] Lap time real: 48 seconds.
