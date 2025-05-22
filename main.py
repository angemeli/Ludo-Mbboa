import pygame
import dices
import pions

pygame.init()

resolution = (1600,837)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Ludo Mboa")

back_sound = pygame.mixer.Sound("sounds/bg002.mp3")
back_sound.set_volume(0.8)
back_sound.play(100)

clock = pygame.time.Clock()


#background
background = pygame.image.load("images/background.png")
background.convert()

wait_face = pygame.image.load("images/wait.png")
wait_face.convert()

dices.dice_b.can_roll = True

################# BOUCLE PRINCIPALE #################
################# BOUCLE PRINCIPALE #################

running = True

while running :

    screen.blit(background, (0,0))
    pions.draw_all_on_screen(screen, pions.pions_bleus, dices.dice_b, pions.parcours_bleu)
    pions.draw_all_on_screen(screen, pions.pions_rouges, dices.dice_r, pions.parcours_rouge)
    pions.draw_all_on_screen(screen, pions.pions_verts, dices.dice_v, pions.parcours_vert)
    pions.draw_all_on_screen(screen, pions.pions_jaunes, dices.dice_j, pions.parcours_jaune)

    pions.create_barriere(pions.pions_bleus, dices.dice_b)
    pions.create_barriere(pions.pions_rouges, dices.dice_r)
    pions.create_barriere(pions.pions_verts, dices.dice_v)
    pions.create_barriere(pions.pions_jaunes, dices.dice_j)
    

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        elif event.type == pygame.KEYDOWN :
            ######### JOUEUR 1 #########
            if (event.key == pygame.K_1) : 
                if dices.dice_b.nbp_finished == 4 :
                    dices.dice_b.can_roll == False
                    dices.dice_r.can_roll = True
                    break
                else :
                    if dices.dice_b.can_roll == True :
                        dices.draw_dices(screen, wait_face, dices.dice_b, (215,625), background)
                        dices.dice_b.can_roll = False
                        dices.dice_b.sum_blocked = 0
                        for bleu_ in pions.pions_bleus :
                            pions.choice_pion_to_move(bleu_, dices.dice_b, dices.dice_r, pions.parcours_bleu, dices.dice_r, dices.dice_v, dices.dice_j)

                        if dices.dice_b.face == "images/dé - 6.png" :
                            dices.dice_r.can_roll = False
                        else :
                            dices.dice_r.can_roll = True

            
            ########## JOUEUR 2 ##########
            elif (event.key == pygame.K_2) : 
                if dices.dice_r.nbp_finished == 4 :
                    dices.dice_r.can_roll == False
                    dices.dice_v.can_roll = True
                    break
                else :
                    if dices.dice_r.can_roll == True :
                        dices.draw_dices(screen, wait_face, dices.dice_r, (213,115), background)
                        dices.dice_r.can_roll = False
                        dices.dice_r.sum_blocked = 0
                        for rouge_ in pions.pions_rouges :
                            pions.choice_pion_to_move(rouge_, dices.dice_r, dices.dice_v, pions.parcours_rouge, dices.dice_v, dices.dice_j, dices.dice_b)

                        if dices.dice_r.face == "images/dé - 6.png" :
                            dices.dice_v.can_roll = False
                        else :
                            dices.dice_v.can_roll = True


            ######### JOUEUR 3 ##########
            elif (event.key == pygame.K_3) :
                if dices.dice_v.nbp_finished == 4 :
                    dices.dice_v.can_roll == False
                    dices.dice_j.can_roll = True
                    break
                else :
                    if dices.dice_v.can_roll == True :
                        dices.draw_dices(screen, wait_face, dices.dice_v, (1307,116), background)
                        dices.dice_v.can_roll = False
                        dices.dice_v.sum_blocked = 0
                        for vert_ in pions.pions_verts :
                            pions.choice_pion_to_move(vert_, dices.dice_v, dices.dice_j, pions.parcours_vert, dices.dice_j, dices.dice_b, dices.dice_r)

                        if dices.dice_v.face == "images/dé - 6.png" :
                            dices.dice_j.can_roll = False
                        else :
                            dices.dice_j.can_roll = True
            

            ########## JOUEUR 4 ###########
            elif (event.key == pygame.K_4) :
                if dices.dice_j.nbp_finished == 4 :
                    dices.dice_j.can_roll == False
                    dices.dice_b.can_roll = True
                    break
                else :
                    if dices.dice_j.can_roll == True :
                        dices.draw_dices(screen, wait_face, dices.dice_j, (1306,633), background)
                        dices.dice_j.can_roll = False
                        dices.dice_j.sum_blocked = 0
                        for jaune_ in pions.pions_jaunes :
                            pions.choice_pion_to_move(jaune_, dices.dice_j, dices.dice_b, pions.parcours_jaune, dices.dice_b, dices.dice_r, dices.dice_v)

                        if dices.dice_j.face == "images/dé - 6.png" :
                            dices.dice_b.can_roll = False
                        else :
                            dices.dice_b.can_roll = True


        ############# DEPLACEMENTS ##############
        ############# DEPLACEMENTS ##############

        ######### JOUEUR 1 #########
        sum_b = dices.dice_b.sum_blocked
        fin_b = dices.dice_b.nbp_finished
        if (sum_b==3 and fin_b==0) or (sum_b==2 and fin_b==1) or (sum_b==1 and fin_b==2) or (sum_b==0 and fin_b==3) :
            for pion_ in pions.pions_bleus :
                if pion_.onclick == True :
                    pions.auto_move_pion(screen, background, pion_, pions.pions_bleus, dices.dice_b, dices.dice_r)
                    pions.tchop_pion(pion_, dices.dice_b, dices.dice_r, pions.pions_rouges, pions.pions_verts, pions.pions_jaunes, pions.prison_bleu)
        else :
            if event.type == pygame.MOUSEBUTTONDOWN :
                for pion_ in pions.pions_bleus :
                    if pion_.onclick == True :
                        pions.move_pion_choised(screen, background, event, pion_, pions.pions_bleus, dices.dice_b, dices.dice_r)
                        pions.tchop_pion(pion_, dices.dice_b, dices.dice_r, pions.pions_rouges, pions.pions_verts, pions.pions_jaunes, pions.prison_bleu)


        ######### JOUEUR 2 #########
        sum_r = dices.dice_r.sum_blocked
        fin_r = dices.dice_r.nbp_finished

        if (sum_r==3 and fin_r==0) or (sum_r==2 and fin_r==1) or (sum_r==1 and fin_r==2) or (sum_r==0 and fin_r==3) :
            for pion_ in pions.pions_rouges :
                if pion_.onclick == True :
                    pions.auto_move_pion(screen, background, pion_, pions.pions_rouges, dices.dice_r, dices.dice_v)
                    pions.tchop_pion(pion_, dices.dice_r, dices.dice_v, pions.pions_verts, pions.pions_jaunes, pions.pions_bleus, pions.prison_rouge)
        else :
            if event.type == pygame.MOUSEBUTTONDOWN :
                for pion_ in pions.pions_rouges :
                    if pion_.onclick == True :
                        pions.move_pion_choised(screen, background, event, pion_, pions.pions_rouges, dices.dice_r, dices.dice_v)
                        pions.tchop_pion(pion_, dices.dice_r, dices.dice_v, pions.pions_verts, pions.pions_jaunes, pions.pions_bleus, pions.prison_rouge)


        ######### JOUEUR 3 #########
        sum_v = dices.dice_v.sum_blocked
        fin_v = dices.dice_v.nbp_finished

        if (sum_v==3 and fin_v==0) or (sum_v==2 and fin_v==1) or (sum_v==1 and fin_v==2) or (sum_v==0 and fin_v==3) :
            for pion_ in pions.pions_verts :
                if pion_.onclick == True :
                    pions.auto_move_pion(screen, background, pion_, pions.pions_verts, dices.dice_v, dices.dice_j)
                    pions.tchop_pion(pion_, dices.dice_v, dices.dice_j, pions.pions_jaunes, pions.pions_bleus, pions.pions_rouges, pions.prison_vert)
        else :
            if event.type == pygame.MOUSEBUTTONDOWN :
                for pion_ in pions.pions_verts :
                    if pion_.onclick == True :
                        pions.move_pion_choised(screen, background, event, pion_, pions.pions_verts, dices.dice_v, dices.dice_j)
                        pions.tchop_pion(pion_, dices.dice_v, dices.dice_j, pions.pions_jaunes, pions.pions_bleus, pions.pions_rouges, pions.prison_vert)


        ######### JOUEUR 4 #########
        sum_j = dices.dice_j.sum_blocked
        fin_j = dices.dice_j.nbp_finished

        if (sum_j==3 and fin_j==0) or (sum_j==2 and fin_j==1) or (sum_j==1 and fin_j==2) or (sum_j==0 and fin_j==3) :
            for pion_ in pions.pions_jaunes :
                if pion_.onclick == True :
                    pions.auto_move_pion(screen, background, pion_, pions.pions_jaunes, dices.dice_j, dices.dice_b)
                    pions.tchop_pion(pion_, dices.dice_j, dices.dice_b, pions.pions_bleus, pions.pions_rouges, pions.pions_verts, pions.prison_jaune)
        else :
            if event.type == pygame.MOUSEBUTTONDOWN :
                for pion_ in pions.pions_jaunes :
                    if pion_.onclick == True :
                        pions.move_pion_choised(screen, background, event, pion_, pions.pions_jaunes, dices.dice_j, dices.dice_b)
                        pions.tchop_pion(pion_, dices.dice_j, dices.dice_b, pions.pions_bleus, pions.pions_rouges, pions.pions_verts, pions.prison_jaune)


    pygame.display.flip()
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] :
        break


pygame.quit()