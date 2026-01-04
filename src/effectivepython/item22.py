"""
Prefer Helper Classes Over Bookkeeping with Dictionaries and Tuples
"""
import os
import sys
import logging



class SimpleGradeBook(object):
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = []
    
    def report_grade(self, name, score):
        self._grades[name].append(score)
    
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades)/len(grades)

# Extending class above to include different subject
class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}
    
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)
    
    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total/count
    
"""
Proper design -> refactoring in the smaller classes
- When the bookkeeping is getting more complicated, then break it all out into classes
- That let you provide well-defined interfaces
"""
grades = []
grades.append((95, 0.45))


"""
named tuple provides cleaner interface comparing with plain tuple
"""
import collections
from collections import namedtuple

trade = ("AAPL", 100, 195.5)
symbol = trade[0]

# Interface is Trade , variable name is trade
Trade = namedtuple("Trade", ["symbol", "quantity", "price"])
trade = Trade("AAPL", 100, 195.5)
# This wont be allowed as namedtuple is immutable
trade.price = 200.0

Point = namedtuple("Point",  ["x", "y"])
p = Point(3,4)
print(p.x)
print(p.y)
print(p[0])
print(p[1])
id(p)

Grade = namedtuple('Grade', ('score', 'weight'))

class Subject(object):
    def __init__(self):
        self._grades = []
    
    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total/total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}
    
    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total/count

class Gradebook(object):
    def __init__(self):
        self._students = {}
    
    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]



if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO) 


    logger.info("Test 1:")
    book = SimpleGradeBook()
    book.add_student("Thanh")
    book.report_grade("Thanh", 90.0)
    print(book.average_grade('Thanh'))

    logger.info("Test 2:")
    book = BySubjectGradebook()
    book.add_student("Thanh")
    book.report_grade("Thanh", "Math", 90.0)
    book.report_grade("Thanh", "IT", 90.2)
    book.report_grade("Thanh", "Math", 98.0)
    print(book.average_grade('Thanh'))

    logger.info("Test 3: good")
    book = Gradebook()
    albert = book.student('Albert Enstein')
    math = albert.subject("Math")
    math.report_grade(80, 0.10)
    
