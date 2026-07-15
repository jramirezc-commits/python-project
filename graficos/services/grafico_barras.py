import seaborn as sns
import matplotlib.pyplot as plt


# df_file = pd.read_csv('graficos//data_income.csv')
# sns.barplot(data=df_file, x='fuente', y='ingreso')
# plt.plot('Netflix', 680, 'D')# Se dibuja un diamante en la coordenada dada
# plt.show()

class GraphBarras:
  def __init__(self, data):
    self.data = data

  def show_graph(self, x, y):
    sns.barplot(data= self.data, x= x, y= y, palette='viridis')
    plt.title('Grafico de Barras')
    plt.show()
  
  def income_total(self):
    total_income = self.data['ingreso'].sum()
    return f'Total en ingresos: {total_income} USD'