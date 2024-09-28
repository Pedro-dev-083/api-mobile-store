"""Módulo focado apenas no teste do modelo"""
from model import Carregador, Preditor, Avaliador

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
preditor = Preditor()
avaliador = Avaliador()

URL_DADOS = "./MachineLearning/data/test_dataset_mobile.csv"
colunas = ['battery_power','blue','clock_speed',
           'dual_sim','fc','four_g','int_memory',
           'm_dep','mobile_wt','model','n_cores',
           'pc','px_height','px_width','ram','sc_h',
           'sc_w','talk_time','three_g','touch_screen','wifi']

# Carga dos dados
dataset = Carregador.carregar_dados(carregador, URL_DADOS, colunas)
array = dataset.values
X = array[:,0:-1]
y = array[:,-1]

def test_modelo():
    """Método para testar a acurácia do modelo"""
    path = './MachineLearning/models/model.pkl'
    preditor.carrega_modelo(path)

    acuracia = avaliador.avaliar(preditor, X, y)

    assert acuracia >= 0.96
