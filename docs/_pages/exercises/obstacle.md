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

For the implementation i have create three forces:
*Atractive force:* Is a vector from the robot to the target. To implement this vector i had to convert the absolute target coordinate to relative (formula 1 coordinates). 
*Repulsive force:* Is a vector obtained by the sumatory of all the repulsive forces. Repulsive forces are vectors from the obstacles to the robot, if the robot is near an obstacle, the repulsive force is high. This type of repulsion makes the car always prefer to be in the center of the circuit if there are no obstacles because lateral forces balance.
*Resultan force:* The resultant force is generated bades on the tentioned above. I calculate it following an acuation with especific parameters to each force.


[Youtube link](https://www.youtube.com/watch?v=Hze2KMPzR5Y)

