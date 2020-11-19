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
- url: /assets/images/exercises/vacum_cleaner/vacuum_cleaner_plan.png
  image_path: /assets/images/exercises/vacum_cleaner/vacuum_cleaner_plan.png
  alt: "Vacuum init"
  title: "Vacuum init"

imageproc:
- url: /assets/images/exercises/vacum_cleaner/vacum_spiral_bump.png
  image_path: /assets/images/exercises/vacum_cleaner/vacum_spiral_bump.png
  alt: "spiral and bump."
  title: "spiral and bump."
- url: /assets/images/exercises/vacum_cleaner/full_vacum.png
  image_path: /assets/images/exercises/vacum_cleaner/full_vacum.png
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

You can find all the information about this exercise in [JdeRobot Academy](http://jderobot.github.io/RoboticsAcademy/exercises/MobileRobots/vacuum_cleaner)

## THEORY

Implementation of navigation algorithms for an autonomous vacuum is the basic requirement for this exercise. The main objective is to cover the largest area of a house. First, let us understand what is Coverage Algorithms.

**Coverage Algorithms:**
Coverage Path Planning is an important area of research in Path Planning for robotics, which involves finding a path that passes through every reachable position in its environment. In this exercise, We are using a very basic coverage algorithm called Random Exploration.

## MY IMPLEMENTATION

For the implementation i have used differents statest in order to cover the largest uncleaned area and avoid repetitions. Modes are selected by a state machine, it use an increasing circle pattern (spiral) and a bump and go algorithm.

{% include gallery id="imageproc" caption="implementations" %}

## THE WAY TO THE SOLUTION

Searching the most efficient algorithm first I tried a simple bump and go pattern using the bumper sensor and a random angular velocity but it was not an optimal solution  because, despite not being unclosed, it did not cover much surface, only lines.

After it, i tried  to make the vacuum cleaner follow a certain pattern of turns to cover the house with parallel lines, but it was impossible due to the pool quality of the motors.

Using a spiral pattern i solve the problem of the bump and yo, wich only covers in a straight line. The problem with the spiral algorith is that it always clean in the same place. To fix it, I have combined both with the aim of move around the house with bump and go and clean more sruface with spiral pattern.


[Youtube link](https://www.youtube.com/watch?v=9kCj6eeHf3Y&t=1s)

- [X] Lap time simulation: 48 seconds.
- [X] Lap time real: 48 seconds.
