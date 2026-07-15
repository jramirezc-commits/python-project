# Activar entorno virtual: source venv/bin/activate
# Desactivar entorno virtual: deactivate
import seaborn as sns
import matplotlib.pyplot as plt


# df_file = pd.read_csv('grafico_lineal//data_first.csv')
# sns.lineplot(data=df_file, x='accion', y='valor')
# plt.plot('Netflix', 680, 'o')# Se dibuja un círculo en la coordenada dada
# # plt.plot('Netflix', 680, 'D')# Se dibuja un diamante en la coordenada dada
# plt.show()


# data = {
#   'A': [1, 2, 3, 4, 5],
#   'B': [5, 4, 3, 2, 1]
# }

# df = pd.DataFrame(data)
# print(df)

# plt.plot(df['A'], df['B'])
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')
# plt.title('Gráfico de Línea')
# plt.show()



# //////////////////////////////////////////
# POO
# //////////////////////////////////////////
class GraphLineal:
  def __init__(self, data):
    self.data_frame = data
  
  def show_graph(self, x, y):
    sns.lineplot(data=self.data_frame, x=x, y=y, palette='viridis')
    plt.title('Grafico de Lineas')
    plt.show()
