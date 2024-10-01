import colorsys

def hsb_to_rgb(hue, saturation, brightness):
    hue = hue/360  # 色相需要从度转换为0到1之间的值
    saturation = saturation/100
    brightness = brightness/100
    rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
    # 将rgb中的值从0到1的浮点数转换为0到255的整数
    return tuple(int(i * 255) for i in rgb)

# HSB:202, 38, 97 对应的RGB值
rgb_values = hsb_to_rgb(136, 54, 65)
print(rgb_values)
