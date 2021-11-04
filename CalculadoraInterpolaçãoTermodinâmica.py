# Calculadora de interpolação

def interpol(yequiv,xmin, ymin, xmax, ymax):
    quero = xmin + (xmax - xmin)*(yequiv - ymin)/(ymax - ymin)
    return quero

result = interpol(706.61, 7.70903, 692.12, 7.74010, 713.56);
print(result)

# Tutorial:
# Esboço da regra de 3

# ymin   <->  xmin
# yequiv <->  quero
# ymax   <->  xmax