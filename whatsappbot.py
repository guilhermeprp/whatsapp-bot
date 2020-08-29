from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        # self.enxerSaco = True

        #Digite o texto que será enviado
        self.mensagemPadrao = ""
        self.mensagem = [self.mensagemPadrao, self.mensagemPadrao, self.mensagemPadrao]
        
        #Digite o nome da pessoa
        self.pessoas = ""
        options = webdriver.ChromeOptions()

        #Mude %User% para seu nome de usuário do computador
        options.add_argument('--user-data-dir=C:/Users/%User%/AppData/Local/Google/Chrome/User Data/Default')
        options.add_argument('--profile-directory=Default')
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)

    def EnviarMensagem(self):


        # Se estiver usando pela primeira vez escaneie o QR Code
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)

        try:
            pessoa = self.driver.find_element_by_xpath(f"//span[@title='{self.pessoas}']")
            time.sleep(2)

        except:
            find = self.driver.find_element_by_class_name('_3FRCZ')
            time.sleep(2)
            find.click()
            find.send_keys(self.pessoas)
            time.sleep(5)
            pessoa = self.driver.find_element_by_xpath(f"//span[@title='{self.pessoas}']")
            time.sleep(2)

            
        
        pessoa.click()
        # while self.enxerSaco == True:
        for self.mensagemPadrao in self.mensagem:
            
            chat = self.driver.find_element_by_class_name('_3uMse')
            
            chat.click()
            chat.send_keys(self.mensagemPadrao)
            enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            
            enviar.click()
    
        self.driver.close()    


bot = WhatsappBot()
bot.EnviarMensagem()
