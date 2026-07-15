import pandas as pd
from services.grafico_barras import GraphBarras
from services.grafico_lineal import GraphLineal
from main import Main


main = Main()
graph_type = input('Que tipo de grafico deseas crear? (1 = barras/ 2 = lineal)')

# if graph_type == '1':
#   dataFrameFile = pd.read_csv('graficos//data_income.csv')
#   barras = GraphBarras(dataFrameFile)
#   main.run(barras, 'fuente', 'ingreso')

# elif graph_type == '2':
#   dataFrameFile = pd.read_csv('graficos//data_first.csv')
#   lineal = GraphLineal(dataFrameFile)
#   main.run(lineal, 'accion', 'valor')
# else:
#   print('Opcion no valida')


# /////////////////////////////////////
# OPCION CORRECTA SIGUIENDO PRINCIPIO OPEN/CLOSE
# /////////////////////////////////////
graph_registry = {
  '1': {'class': GraphBarras, 'file': 'graficos//data_income.csv', 'x': 'fuente', 'y': 'ingreso'},
  '2': {'class': GraphLineal, 'file': 'graficos//data_first.csv', 'x': 'accion', 'y': 'valor'}
}

graph_selected = graph_registry.get(graph_type)

if graph_selected:
  dataFrameFile = pd.read_csv(graph_selected['file'])
  # print(dataFrameFile.head(2))
  graph_instance = graph_selected['class'](dataFrameFile)
  main.run(graph_instance, graph_selected['x'], graph_selected['y'])
else:
  print('Opcion no valida')