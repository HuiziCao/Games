
from graphics import *
from math import pi, cos, sin

def draw_flower(win, center, petal_radius=5):
    # 白色的花心
    white = color_rgb(255, 255, 255)
    flower_center = Circle(center, petal_radius / 2)
    flower_center.setFill(white)
    flower_center.draw(win)

    # 莫兰迪色系的花瓣颜色
    morandi_yellow = color_rgb(235, 233, 208)  # 莫兰迪黄色
    morandi_orange = color_rgb(234, 215, 188)  # 莫兰迪橙色

    # 绘制7片花瓣，交替颜色
    colors = [morandi_orange, morandi_yellow, morandi_orange, morandi_yellow, morandi_orange, morandi_yellow, morandi_orange]
    for i in range(7):
        angle = pi / 3 * i
        petal_x = center.getX() + petal_radius * cos(angle)
        petal_y = center.getY() + petal_radius * sin(angle)
        petal = Circle(Point(petal_x, petal_y), petal_radius)
        petal.setFill(colors[i])
        petal.setOutline(colors[i])
        petal.draw(win)
    return flower_center

def place_on_circle(circle_center, circle_radius, angle):
    """在圆上给定角度的位置放置一个点"""
    x = circle_center.getX() + circle_radius * cos(angle)
    y = circle_center.getY() + circle_radius * sin(angle)
    return Point(x, y)

def draw_pentagon_points(center, radius):
    """计算五边形顶点的位置"""
    points = []
    for i in range(5):
        angle = pi / 2 + i * 2 * pi / 5  # 五边形的角度
        points.append(place_on_circle(center, radius, angle))
    return points

def flower_tree_model(win, x, y, flower_size, trunk_height=80, trunk_width=20):
    # 莫兰迪色系的树干颜色
    morandi_brown = color_rgb(87, 78, 77)
    trunk = Rectangle(Point(x, y), Point(x + trunk_width, y - trunk_height))
    trunk.setFill(morandi_brown)
    trunk.setOutline(morandi_brown)
    trunk.draw(win)
    
    # 莫兰迪色系的树叶颜色
    morandi_green = color_rgb(168, 188, 158)
    leaves_center = Point(x + trunk_width / 2, y - trunk_height)
    leaves_radius = trunk_height * 0.75  # 增加树叶的圆的大小
    leaves = Circle(leaves_center, leaves_radius)
    leaves.setFill(morandi_green)
    leaves.setOutline(morandi_green)  # 边缘也是绿色
    leaves.draw(win)

    # 计算五边形顶点的位置，留出空间以便花朵完全在树叶内
    pentagon_radius = leaves_radius - flower_size
    pentagon_points = draw_pentagon_points(leaves_center, pentagon_radius)

    # 绘制位于五边形顶点的五朵花
    flowers = []
    for point in pentagon_points:
        flower_center = draw_flower(win, point, flower_size)
        flowers.append(flower_center)

    # 在五边形中心绘制第六朵花
    flower_center = draw_flower(win, leaves_center, flower_size)
    flowers.append(flower_center)

    # 返回所有元素
    return [trunk, leaves] + flowers

# 创建窗口
win = GraphWin('Flower Tree Model', 800, 800)

# 绘制桂花树并调整花朵大小和位置
flower_tree = flower_tree_model(win, 350, 650, 5, 80, 20)

# 等待点击事件然后关闭窗口
win.getMouse()
win.close()
