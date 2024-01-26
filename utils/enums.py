from enum import Enum

Grade = Enum("Grade", {"A":5, "B":4, "C":3, "D":2, "E":1})
grade_nameslist = [grade.name for grade in Grade]