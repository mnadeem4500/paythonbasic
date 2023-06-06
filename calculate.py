from django.http import HttpResponse

class Student:

    def __init__(self, name, math, urdu, english):
        self.name=name
        self.math=math
        self.urdu=urdu
        self.english=english


    def calculate_sum(self):
        return self.Urdu+self.Math+self.English
    def calculate_avg(self):
        return self.calculate_sum()/3



