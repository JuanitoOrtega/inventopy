from config.wsgi import *
from erp.models import *

data = [
    'Leche y derivados',
    'Carnes, pescados y huevos',
    'Patatas, legumbres, frutos secos',
    'Verduras y Hortalizas',
    'Frutas',
    'Cereales y derivados, azúcar y dulces',
    'Grasas, aceite y mantequilla'
]

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado con registro Nro.{}'.format(cat.id))
