from display import *
from draw import *
from parser_s import *
from matrix import *
import math

screen = new_screen()
color = [ 0,191,255]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'script', edges, polygons, transform, screen, color )
