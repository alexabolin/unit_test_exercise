# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:37:48 2023

@author: hboli
"""


def new_y(plane_input_1, plane_input_2, new_x):
    slope = (plane_input_2[1] - plane_input_1[1]) / (plane_input_2[0] -
                                                     plane_input_1[0])
    y_int = plane_input_2[1] - (slope*plane_input_2[0])
    new_y = (slope*new_x) + y_int
    return new_y


def true_false(plane_input_1, plane_input_2, input_3):
    slope = (plane_input_2[1] - plane_input_1[1]) / (plane_input_2[0] -
                                                     plane_input_1[0])
    y_int = plane_input_2[1] - (slope*plane_input_2[0])
    new_y = (slope*input_3[0]) + y_int
    if new_y == input_3[1]:
        return True
    else:
        return False


if __name__ == "__main__":
    new_y()
    true_false()
