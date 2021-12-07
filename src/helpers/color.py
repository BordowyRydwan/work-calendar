def rgba(r, g, b, a):
    return float(r) / 255.0, float(g) / 255.0, float(b) / 255.0, float(a)


def rgb(r, g, b):
    return rgba(r, g, b, 1)
