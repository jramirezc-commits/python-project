# ///////////////////
# EJERCICIO CON POO
# ///////////////////

from services.grafico_barras import GraphBarras

class Main:
  def run(self, graph_type, x, y):
    if isinstance(graph_type, GraphBarras):
      print(graph_type.income_total())
    graph_type.show_graph(x, y)
