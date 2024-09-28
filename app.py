"""Módulo Prinicipal para a execução do projeto"""
from urllib.parse import unquote
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from flask_cors import CORS
from model import Session, Mobile, PreProcessador, Preditor
from logger import logger
from schemas import MobileViewSchema, MobilePriceRangeSchema, ErrorSchema, MobileSchema
from schemas import MobileBuscaSchema, apresenta_mobile, apresenta_mobiles, retorna_price_range

# Instanciando o objeto OpenAPI
info = Info(title="API Mobile Store", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
DESCRIPTION_HOME = "Seleção de documentação: Swagger, Redoc ou RapiDoc"
home_tag = Tag(name="Documentação", description=DESCRIPTION_HOME)
mobile_tag = Tag(name="Mobile", description="Adição, visualização, remoção e predição de celulares")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de listagem de celulares
@app.get('/mobiles', tags=[mobile_tag],
         responses={"200": MobileViewSchema, "404": ErrorSchema})
def get_mobiles():
    """Lista todos os celulares cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de celulares cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os celulares")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os celulares
    mobiles = session.query(Mobile).all()

    if not mobiles:
        # Se não houver celulares
        return {"mobiles": []}, 200

    logger.debug("%s Celulares encontrados", len(mobiles))
    print(mobiles)
    return apresenta_mobiles(mobiles), 200

# Métodos baseados em modelo
# Rota de busca de celular por modelo
@app.get('/mobile', tags=[mobile_tag],
         responses={"200": MobileViewSchema, "404": ErrorSchema})
def get_mobile(query: MobileBuscaSchema):
    """Faz a busca por um celular cadastrado na base a partir do modelo

    Args:
        modelo (str): modelo do celular
        
    Returns:
        dict: representação do celular
    """

    mobile_model = query.model
    logger.debug("Coletando dados sobre celular %s", mobile_model)
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    mobile = session.query(Mobile).filter(Mobile.model == mobile_model).first()

    if not mobile:
        # se o celular não foi encontrado
        error_msg = f"Celular {mobile_model} não encontrado na base."
        logger.warning("Erro ao buscar celular '%s', %s", mobile_model, error_msg)
        return {"message": error_msg}, 404

    logger.debug("%s Celular encontrado:", mobile.model)
    # retorna a representação do celular
    return apresenta_mobile(mobile), 200

# Rota de predição de mobile
@app.post('/mobilePredict', tags=[mobile_tag],
          responses={"200": MobileViewSchema, "400": ErrorSchema, "409": ErrorSchema})
# pylint: disable=R0914:too-many-locals
def predict(form: MobilePriceRangeSchema):
    """Prediz o price_range do celular.
    
    Args:
        battery_power (int): Total de energia da bateria em mAh.
        blue (bool): Se possui bluetooth.
        clock_speed (float): Velocidade do microprocessador do celular em GHz.
        dual_sim (bool): Se o celular suporta dois sims (Chips).
        fc (int): Mega pixels da câmera frontal.
        four_g (bool): Se possui 4G.
        int_memory (int): Memória interna em GB (Gigabytes).
        m_dep (float): Profundidade do Celular em cm (centímetros).
        manufacturer (str): Fabricante do celular (Ex: Samsung, Motorola).
        mobile_wt (int): Peso do celular em gramas.
        model (str): Modelo do celular (Ex: Galaxy A11, Moto G5).
        n_cores (int): Números de núcleos do processador.
        pc (int): Mega pixels da câmera principal.
        price_range_predicted (int): Alcance de preço predito. 
        price_final (int): Preço final decidido pelo varejista.
        px_height (int): Altura da resolução em pixels.
        px_width (int): Largura da resolução em pixels.        
        ram (int): Memória RAM em MB (Megabytes).
        sc_h (int): Altura da tela do celular em cm (centímetros).
        sc_w (int): Largura da tela do celular em cm (centímetros);
        talk_time (int): Maior tempo que uma única carga de bateria irá durar durante uma ligação.
        three_g (bool): Se possui 3G.
        touch_screen (bool): Se possui tela sensível a toque.
        wifi (bool): Se possui Wi-fi.
        
    Returns:
        dict: Price_range e sua descrição
    """

    try:
        pre_processador = PreProcessador()
        preditor = Preditor()
        # Preparando os dados para o modelo
        x_input = pre_processador.preparar_form(form)
        # Carregando modelo
        model_path = './MachineLearning/models/model.pkl'
        preditor.carrega_modelo(model_path)
        # Realizando a predição
        outcome = int(preditor.predizer(x_input)[0])
        # Concluindo a transação
        logger.debug("%s Price_range", outcome)
        return retorna_price_range(outcome), 200

    # Caso ocorra algum erro na predição
    # pylint: disable=W0718:broad-exception-caught
    except Exception:
        error_msg = "Não foi possível prever novo item."
        logger.warning("Erro ao prever o price_range")
        return {"message": error_msg}, 400

@app.post('/mobile', tags=[mobile_tag],
          responses={"200": MobileViewSchema, "400": ErrorSchema, "409": ErrorSchema})

# pylint: disable=R0914:too-many-locals
def salvar_mobile(form: MobileSchema):
    """Adiciona um novo celular à base de dados.
        
    Args:
        battery_power (int): Total de energia da bateria em mAh.
        blue (bool): Se possui bluetooth.
        clock_speed (float): Velocidade do microprocessador do celular em GHz.
        dual_sim (bool): Se o celular suporta dois sims (Chips).
        fc (int): Mega pixels da câmera frontal.
        four_g (bool): Se possui 4G.
        int_memory (int): Memória interna em GB (Gigabytes).
        m_dep (float): Profundidade do Celular em cm (centímetros).
        manufacturer (str): Fabricante do celular (Ex: Samsung, Motorola).
        mobile_wt (int): Peso do celular em gramas.
        model (str): Modelo do celular (Ex: Galaxy A11, Moto G5).
        n_cores (int): Números de núcleos do processador.
        pc (int): Mega pixels da câmera principal.
        price_range_predicted (int): Alcance de preço predito. 
        price_final (int): Preço final decidido pelo varejista.
        px_height (int): Altura da resolução em pixels.
        px_width (int): Largura da resolução em pixels.        
        ram (int): Memória RAM em MB (Megabytes).
        sc_h (int): Altura da tela do celular em cm (centímetros).
        sc_w (int): Largura da tela do celular em cm (centímetros);
        talk_time (int): Maior tempo que uma única carga de bateria irá durar durante uma ligação.
        three_g (bool): Se possui 3G.
        touch_screen (bool): Se possui tela sensível a toque.
        wifi (bool): Se possui Wi-fi.
        
    Returns:
        dict: representação do celular adicionado
    """
    mobile = Mobile(
        battery_power = form.battery_power,
        blue = form.blue,
        clock_speed = form.clock_speed,
        dual_sim = form.dual_sim,
        fc = form.fc,
        four_g = form.four_g,
        int_memory = form.int_memory,
        m_dep = form.m_dep,
        manufacturer = form.manufacturer,
        mobile_wt = form.mobile_wt,
        model = form.model,
        n_cores = form.n_cores,
        pc = form.pc,
        price_range_predicted = form.price_range_predicted,
        price_final = form.price_final,
        px_height = form.px_height,
        px_width = form.px_width,
        ram = form.ram,
        sc_h = form.sc_h,
        sc_w = form.sc_w,
        talk_time = form.talk_time,
        three_g = form.three_g,
        touch_screen = form.touch_screen,
        wifi = form.wifi
    )
    logger.debug("%s Adicionando celular", mobile.model)

    try:
        # Criando conexão com a base
        session = Session()

        # Checando se celular já existe na base
        if session.query(Mobile).filter(Mobile.model == form.model).first():
            error_msg = "Celular já existente na base."
            logger.warning("Erro ao adicionar celular '%s', %s", mobile.model, error_msg)
            return {"message": error_msg}, 409

        # Adicionando celular
        session.add(mobile)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug("%s Adicionado celular", mobile.model)
        return apresenta_mobile(mobile), 200

    # Caso ocorra algum erro na adição
    # pylint: disable=W0718:broad-exception-caught
    except Exception:
        error_msg = "Não foi possível salvar novo item."
        logger.warning("Erro ao adicionar celular '%s', %s", mobile.model, error_msg)
        return {"message": error_msg}, 400

# Rota de remoção de celular por modelo
@app.delete('/mobile', tags=[mobile_tag],
            responses={"200": MobileViewSchema, "404": ErrorSchema})
def delete_celular(query: MobileBuscaSchema):
    """Remove um celular cadastrado na base a partir do modelo

    Args:
        modelo (str): modelo do celular
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """

    mobile_model = unquote(query.model)
    logger.debug("%s Deletando dados sobre o celular", mobile_model)

    # Criando conexão com a base
    session = Session()

    # Buscando celular
    mobile = session.query(Mobile).filter(Mobile.model == mobile_model).first()

    if not mobile:
        error_msg = "Celular não encontrado na base :/"
        logger.warning("Erro ao deletar celular '%s', %s", mobile_model, error_msg)
        return {"message": error_msg}, 404

    session.delete(mobile)
    session.commit()
    logger.debug("%s Deletado celular", mobile_model)
    return {"message": f"Celular {mobile_model} removido com sucesso!"}, 200

if __name__ == '__main__':
    app.run(debug=True)
