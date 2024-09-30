"""Coordinates"""

__author__ = "730602202"


def get_coords(xs: str, ys: str) -> None:
    idx_x = 0
    while idx_x < len(xs):
        idx_y = 0
        while idx_y < len(ys):
            print("(" + xs[idx_x] + "," + ys[idx_y] + ")")
            idx_y += 1
        idx_x += 1
