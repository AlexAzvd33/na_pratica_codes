from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = " Bom dia pessoa"
        self.grupos = ["nome_do_grupo"]
        self.mensagem = "this is a test"
        self.grupos_ou_pessoas = ["nome_do_grupo"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        #<span dir="auto" title="Família" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Família</span>
        #<div tabindex="-1" class="p3_M1">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(45)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(5)
            grupo.click()
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(5)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(8)
            botao_enviar.click()
            time.sleep(8)

bot = WhatsappBot()
bot.EnviarMensagens()
