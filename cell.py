from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win == None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo = False):
        if self._win == None:
            return
        self_x_center = (self._x1 + self._x2) / 2
        self_y_center = (self._y1 + self._y2) / 2
        to_cell_x_center = (to_cell._x1 + to_cell._x2) / 2
        to_cell_y_center = (to_cell._y1 + to_cell._y2) / 2
        if undo == False:
            fill_color = "red"
        else:
            fill_color = "gray"
        #moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, self_y_center), Point(self_x_center,self_y_center))
            self._win.draw_line(line,fill_color)
            line = Line(Point(to_cell_x_center,to_cell_y_center), Point(to_cell._x2,to_cell_y_center))
            self._win.draw_line(line,fill_color)

        #moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(self_x_center,self_y_center),Point(self._x2,self_y_center))
            self._win.draw_line(line,fill_color)
            line = Line(Point(to_cell._x1,to_cell_y_center), Point(to_cell_x_center,to_cell_y_center))
            self._win.draw_line(line,fill_color)

        #moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(self_x_center,self_y_center),Point(self_x_center,self._y2))
            self._win.draw_line(line,fill_color)
            line = Line(Point(to_cell_x_center,to_cell._y1),Point(to_cell_x_center,to_cell_y_center))
            self._win.draw_line(line,fill_color)

        #moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(self_x_center,self_y_center),Point(self_x_center,self._y1))
            self._win.draw_line(line,fill_color)
            line = Line(Point(to_cell_x_center,to_cell._y2),Point(to_cell_x_center,to_cell_y_center))
            self._win.draw_line(line,fill_color)

