# unit_test_exercise

Author: Alexa Bolin

## Introduction
This repository contains code for calculating the expected y_coordinate when given an x_coordinate on a defined line and plane. It also confirms whether a given input is on a defined line or plane. The repository also contains a test file, which has been run and fully passed by the program. The program is written in Python and follows PEP 8 style guidelines.

## Specifications 
The program runs the `new_y` function, which takes in 3 parameters: `plane_input_1, plane_input_2, new_x`. The first two define the line and the plane on which the new coordinate will be calculated. The third parameter takes in the x coordinate the user would like to input. The function then returns the corresponding y coordinate.
The program also runs the `true_false` function, which takes in 3 parameters: `plane_input_1, plane_input_2, input_3`. The first two behave similarly to the inputs in `new_y`, defining the line of interest. The third parameter is now a tuple of the coordinate of interest. If the coordinate is on the line, the function returns `True`; otherwise, it returns `False`.
