from selenium import webdriver # slenium for å lage en slags webemulator som du kan bruke

options = webdriver.ChromeOptions() # lager en variabel som gir tillang på Chrome options
options.add_argument('--headless') # legger til ett argument så jeg slipper å se nettleseren
driver = webdriver.Chrome("/Applications/chromedriver", options = options) # lager nettleseren med Chromedriver som er en programmfil 

driver.get("https://mon.ruter.no/departures/59.936551-10.917014") # åpner nettsiden


def hent_avgang(avgang):
    element = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[3]/div['+ avgang +']/div[3]') # finn elementet
    return(element.text) # returner elementet

def hent_linje(avgang):
    element = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[3]/div['+ avgang +']/div[1]/div/div')
    return(element.text)

def hent_destinasjon(avgang):
    element = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[3]/div['+ avgang +']/div[2]/span')
    return(element.text)

def hent_plattform(avgang):
    element = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[3]/div['+ avgang +']/div[4]/div')
    return(element.text)

# driver.quit()