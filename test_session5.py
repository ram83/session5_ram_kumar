import pytest
import random
import string
import session5
import os
import decimal
from decimal import Decimal
import cmath
import inspect
import re
import math
import pandas as pd

README_CONTENT_CHECK_FOR = [

    'squared_power',
    'polygon_area',
    'temp_converter',
    'speed_converter',
    'Positional Arguments',
    'Named Arguments',
    'Default Arguments'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_squared_power():
    
    q = session5.squared_power_list(2,start=0,end=5)
    assert q!=0.0, f"sqruared power function is returning null"

def test_polygon_area():
    q = session5.polygon_area(15, sides = 3)
    assert q!=0.0, f"area of polygon is 0"

def test_temp_converter():
    q = session5.temp_converter(100, temp_given_in = 'f')
    assert q!=0.0, f"Temperature conversion is returning 0"


def test_speed_converter1():
    q = session5.speed_converter(100, dist='km', time='min')
    assert q!=0.0, f"Km/Hr to Km/min conversion is returning 0"

def test_speed_converter2():
    q = session5.speed_converter(100, dist='km', time='s')
    assert q!=0.0, f"Km/Hr to Km/s conversion is returning 0"
def test_speed_converter3():
    q = session5.speed_converter(100, dist='km', time='ms')
    assert q!=0.0, f"Km/Hr to Km/ms conversion is returning 0"
def test_speed_converter4():
    q = session5.speed_converter(100, dist='km', time='day')
    assert q!=0.0, f"Km/Hr to Km/day conversion is returning 0"
def test_speed_converter5():
    q = session5.speed_converter(100, dist='km', time='hr')
    assert q!=0.0, f"Km/Hr to Km/hr conversion is returning 0"
def test_speed_converter6():
    q = session5.speed_converter(100, dist='m', time='s')
    assert q!=0.0, f"Km/Hr to m/s conversion is returning 0"
def test_speed_converter7():
    q = session5.speed_converter(100, dist='m', time='min')
    assert q!=0.0, f"Km/Hr to m/min conversion is returning 0"
def test_speed_converter8():
    q = session5.speed_converter(100, dist='m', time='ms')
    assert q!=0.0, f"Km/Hr to m/ms conversion is returning 0"
def test_speed_converter9():
    q = session5.speed_converter(100, dist='m', time='hr')
    assert q!=0.0, f"Km/Hr to m/hr conversion is returning 0"
def test_speed_converter10():
    q = session5.speed_converter(100, dist='m', time='day')
    assert q!=0.0, f"Km/Hr to m/day conversion is returning 0"
def test_speed_converter11():
    q = session5.speed_converter(100, dist='ft', time='s')
    assert q!=0.0, f"Km/Hr to ft/s conversion is returning 0"
def test_speed_converter12():
    q = session5.speed_converter(100, dist='ft', time='ms')
    assert q!=0.0, f"Km/Hr to ft/ms conversion is returning 0"
def test_speed_converter13():
    q = session5.speed_converter(100, dist='ft', time='min')
    assert q!=0.0, f"Km/Hr to ft/min conversion is returning 0"
def test_speed_converter14():
    q = session5.speed_converter(100, dist='ft', time='hr')
    assert q!=0.0, f"Km/Hr to ft/hr conversion is returning 0"
def test_speed_converter15():
    q = session5.speed_converter(100, dist='ft', time='day')
    assert q!=0.0, f"Km/Hr to ft/day conversion is returning 0"
def test_speed_converter16():
    q = session5.speed_converter(100, dist='yrd', time='s')
    assert q!=0.0, f"Km/Hr to yrd/s conversion is returning 0"
def test_speed_converter17():
    q = session5.speed_converter(100, dist='yrd', time='ms')
    assert q!=0.0, f"Km/Hr to yrd/ms conversion is returning 0"
def test_speed_converter18():
    q = session5.speed_converter(100, dist='yrd', time='min')
    assert q!=0.0, f"Km/Hr to yrd/min conversion is returning 0"
def test_speed_converter19():
    q = session5.speed_converter(100, dist='yrd', time='hr')
    assert q!=0.0, f"Km/Hr to yrd/hr conversion is returning 0"
def test_speed_converter20():
    q = session5.speed_converter(100, dist='yrd', time='day')
    assert q!=0.0, f"Km/Hr to yrd/hr conversion is returning 0"