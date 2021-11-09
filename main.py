import pygame
import scraper


width = 800
height = 500
Programm_vindu = pygame.display.set_mode((width, height))

pygame.font.init()
fonten = pygame.font.SysFont('arial', 30)
HVIT = (255, 255, 255)

clock = pygame.time.Clock()
run = True


def oppdater_Programm_vindu():
    Programm_vindu.fill((0, 0, 0))
    Programm_vindu.blit(fonten.render("Ellingsrudåsen (T)", False, HVIT),(10, 5))
    Programm_vindu.blit(fonten.render("Linje", False, HVIT),(10, 50))
    Programm_vindu.blit(fonten.render("Destinasjon", False, HVIT),(width/4, 50))
    Programm_vindu.blit(fonten.render("Avgang", False, HVIT),(width/4*2, 50))
    Programm_vindu.blit(fonten.render("Plattform", False, HVIT),(width/4*3, 50))
    for i in range(7):
        send_index = str(i + 1)

        linje_text = scraper.hent_linje(send_index)
        Programm_vindu.blit(fonten.render(linje_text, False, HVIT),(10, 80 + 50 * (i + 1)))
        
        destinasjon_text = scraper.hent_destinasjon(send_index)
        Programm_vindu.blit(fonten.render(destinasjon_text, False, HVIT),(width/4, 80 + 50 * (i + 1)))

        avgang_text = scraper.hent_avgang(send_index)
        Programm_vindu.blit(fonten.render(avgang_text, False, HVIT),(width/4*2, 80 + 50 * (i + 1)))

        plattform_text = scraper.hent_plattform(send_index)
        Programm_vindu.blit(fonten.render(plattform_text, False, HVIT),(width/4*3, 80 + 50 * (i + 1)))

    pygame.display.update()


while run:
    clock.tick(10) #programmet skal bare oppdatere __ ganger i sekundet
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    oppdater_Programm_vindu()


scraper.driver.quit() #usikker på om dette trengs
pygame.quit()