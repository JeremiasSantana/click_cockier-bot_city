import logging
import os
from datetime import datetime

def loggin():
    data_atual = datetime.now().strftime('%d/%m/%y')  # noqa: DTZ005
    caminho = os.path.join("logs", data_atual)


    os.makedirs(caminho, exist_ok=True)
    caminho_diretorio = os.path.join(caminho, "pasta_log.log")

    logging.basicConfig(
        level=logging.INFO,
        filename=caminho_diretorio,
        encoding='utf-8',
        filemode='a',
        format='[%(asctime)s][%(levelname)s] - %(message)s',
        datefmt='%H:%M:%S'
    )

    loggin = logging.getLogger(__name__)
    return loggin
if __name__ == "__main__":
    pass