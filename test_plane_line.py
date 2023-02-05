# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:04:26 2023

@author: hboli
"""
import pytest


@pytest.mark.parametrize("plane_input_1, plane_input_2, new_x, expected",
                         [((0,0), (1,1), 0.5, 0.5),
                          ((-1, -2), (1, 2), 0, 0),
                          ((1,4), (5, 6), 3, 5)])
def test_plan_line(plane_input_1, plane_input_2, new_x, expected):
     from plane_line import new_y
     # Arrange (parameters)
     # Act
     answer = new_y(plane_input_1, plane_input_2, new_x)
     # Assert
     assert answer == expected

