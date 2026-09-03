"""
WARNING:
Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
"""

import time

from botcity.web import Browser, By, WebBot
from packaging.version import Version as LooseVersion


def main():
        
    # Instancia o WebBot
    webbot = WebBot()
    webbot.browser = Browser.FIREFOX

    webbot.headless = False
    
    
    try:

        webbot.browse("https://orteil.dashnet.org/cookieclicker/")
        webbot.maximize_window()
        print("Carregando site...🖥️")

        webbot.wait(3000)
        idioma = webbot.find_element("langSelect-PT-BR", By.ID, 30000)
        if not idioma:
            print(
            "Elemento não encontrado❎.\n"
            "Finalizando programa..."
            )
            webbot.stop_browser()
            return
        
        webbot.wait_for_element_visibility(idioma.click())
        print("Idioma Pt-br Escolhido ✅")
        

        cliques = webbot.find_element(selector="bigCookie", by=By.ID, waiting_time=30000)
        if not cliques:
            print(
            "Elemento não encontrado❎.\n"
            "Finalizando programa..."
            )
            webbot.stop_browser()
            return

        
        print("Clicando...\n")
        marcador_segundos = time.time()
        
        while True:
            tempo_atual = time.time()

            cliques.click()
            
            if tempo_atual - marcador_segundos >= 60:
                for i in range(19, -1, -1):
                    try:
                        produto = webbot.find_element(selector=f"product{i}", by=By.ID, waiting_time=10)
                        if produto and "enabled" in produto.get_attribute("class"):
                            produto.click()

                            nome_produto = webbot.find_element(selector=f"productName{i}", by=By.ID)
                            quantidade_produto = webbot.find_element(selector=f"productOwned{i}", by=By.ID)
                            print(f"\033[31mMelhoria comprada:\033[0m {nome_produto.text}({quantidade_produto.text})")

                            print('\033[34m_\033[0m' * 100)

                            marcador_segundos = time.time()
                    except Exception:  # noqa: S112
                        continue
                        
            
            if tempo_atual - marcador_segundos >= 20:
                try:
                    upgrade = webbot.find_element(selector="upgrade0", by=By.ID)
                    if upgrade and "enabled" in upgrade.get_attribute("class"):
                        upgrade.click()
                        marcador_segundos = time.time()

                        print("\033[31mUpgrade comprado\033[0m")
                        print('\033[34m_\033[0m' * 100)
                
                except:
                    pass


    except KeyboardInterrupt:
        print("Farme interropido. Houve uma parada forçada")
        webbot.stop_browser()
    
    except Exception as erro:
        print(f"Houve um erro inesperado: {erro}. Tente novamente")
    
    finally:
        print("Farm finalizado. Até mais")
        webbot.stop_browser()

        

def not_found(label):

    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
