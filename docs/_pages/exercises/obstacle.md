---
title: Obstacle Avoidance
layout: archive
permalink: /obstacle/

classes: wide

sidebar:
  nav: "docs"

toc: true
toc_label: "TOC Visual Obstacle Avoidance"
toc_icon: "cog"

<!--- layout: archive --->

<!--- classes: wide --->

gallery:
- url: /assets/images/exercises/obstacle/obstacle.png
  image_path: /assets/images/exercises/obstacle/obstacle.png
  alt: "obstacle init"
  title: "car before obstacle"

vff:
- url: /assets/images/exercises/obstacle/Virtual-Force-Field-algorithm.png
  image_path: /assets/images/exercises/obstacle/Virtual-Force-Field-algorithm.png
  alt: "Virtual Force Field"
  title: "Virtual Force Field"

equation:
- url: /assets/images/exercises/follow_line/geogebra.png
  image_path: /assets/images/exercises/follow_line/geogebra.png
  alt: "equation."
  title: "equation."

---
## GOAL

The goal of this exercise is to implement the logic of the Virtual Force Field (VFF) navigation algorithm in a car who has to avoid obstacles in a race.

{% include gallery %}

You can find all the information about this exercise in [JdeRobot Academy](http://jderobot.github.io/RoboticsAcademy/exercises/MobileRobots/vacuum_cleaner)

## THEORY

In this exercise we have to use two tipes of navigation , global and local navigation. Global Navigation involves the use of a map of the environment to plan a path from point A to point B. Local Navigation involves a dynamically changing path plan taking into consideration the changing surroundings and the vehicle constraints. 
The virtual Force Field Algorithm generate an atractive vector (force) to the waiypoint that points towards the waypoint. The robot assigns a repulsive vector to the obstacle according to its sensor readings that points away from the waypoint. This is done by summing all the vectors that are translated from the sensor readings.The robot follows the vector obtained by summing the target and obstacle vector.

{% include gallery id="vff" %}

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
