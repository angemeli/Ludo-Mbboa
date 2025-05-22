import pygame
import time
import dices

pygame.init()
scr = pygame.display.set_mode((0,0))

font = pygame.font.SysFont("Cambria", 10)

xpsb,ypsb = (782,730)
xpsr,ypsr = (425,397)
xpsv,ypsv = (782,63)
xpsj,ypsj = (1140,397)

### --------- POSITIONS SPECIALES DES PIONS ---------- ###
pos_bleu = []
pos_rouge = []
pos_vert = []
pos_jaune = []

for _ in range(6) :
    pos_bleu.append((xpsb,ypsb))
    ypsb -= 57
    pos_rouge.append((xpsr,ypsr))
    xpsr += 61
    pos_vert.append((xpsv,ypsv))
    ypsv += 57
    pos_jaune.append((xpsj,ypsj))
    xpsj -= 61


### ------ POSITIONS ORDINAIRES DES PIONS -------- ###
xb,yb = (837,503)
xr,yr = (668,448)
xv,yv = (727,291)
xj,yj = (896,345)

blue_parc = [(xb,yb)]
red_parc = [(xr,yr)]
green_parc = [(xv,yv)]
yellow_parc = [(xj,yj)]

for _ in range(1,13) : #Bleu
    if _<=5 :
        yb+=57        
        blue_parc.append((xb,yb))
    elif _>5 and _<=7 :
        xb-=55
        blue_parc.append((xb,yb))
    elif _>7 and _<=12 :
        yb-=57
        blue_parc.append((xb,yb))
for _ in range(1,13) : #Rouge
    if _<=5 :
        xr-=61        
        red_parc.append((xr,yr))
    elif _>5 and _<=7 :
        yr-=52
        red_parc.append((xr,yr))
    elif _>7 and _<=12 :
        xr+=61
        red_parc.append((xr,yr))
for _ in range(1,13) : #Vert
    if _<=5 :
        yv-=57        
        green_parc.append((xv,yv))
    elif _>5 and _<=7 :
        xv+=55
        green_parc.append((xv,yv))
    elif _>7 and _<=12 :
        yv+=57
        green_parc.append((xv,yv))
for _ in range(1,13) : #Jaune
    if _<=5 :
        xj+=61       
        yellow_parc.append((xj,yj))
    elif _>5 and _<=7 :
        yj+=52
        yellow_parc.append((xj,yj))
    elif _>7 and _<=12 :
        xj-=61
        yellow_parc.append((xj,yj))

parcours_bleu = []
parcours_rouge = []
parcours_vert = []
parcours_jaune = []

def parc_auto_appender(parcours, parc, p1, p2, p3, ps) :
    for _ in range(8,13) :
        parcours.append(parc[_])
    for _ in p1 :
        parcours.append(_)
    for _ in p2 :
        parcours.append(_)
    for _ in p3 :
        parcours.append(_)
    for _ in range(0,7) :
        parcours.append(parc[_])
    for _ in ps :
        parcours.append(_)

parc_auto_appender(parcours_bleu, blue_parc, red_parc, green_parc, yellow_parc, pos_bleu)
parc_auto_appender(parcours_rouge, red_parc, green_parc, yellow_parc, blue_parc, pos_rouge)
parc_auto_appender(parcours_vert, green_parc, yellow_parc, blue_parc, red_parc, pos_vert)
parc_auto_appender(parcours_jaune, yellow_parc, blue_parc, red_parc, green_parc, pos_jaune)

############ Positions en prison ############
prison_bleu = [(365,740), (365,675), (365,610), (365,550),   (415,505), (485,505), (550,505), (620,505),   (665,550), (665,610), (665,675), (665,740)]
prison_rouge = [(415,10), (485,10), (550,10), (620,10),   (665,55), (665,115), (665,180), (665,240),   (620,285), (550,285), (485,285), (415,285)]
prison_vert = [(1200,55), (1200,115), (1200,180), (1200,240),   (1155,285), (1085,285), (1020,285), (950,285),   (900,240), (900,180), (900,115), (900,55)]
prison_jaune = [(1155,780), (1085,780), (1020,780), (950,780),   (900,740), (900,680), (900,615), (900,555),   (950,505), (1020,505), (1085,505), (1155,505)]
        








class Pion_bleu() :
    def __init__(self, pos_ini, ind = 0, block = 1, click = False, home = True, prison = False, statut = False) :
        self.name = "Bleu"
        
        self.color = pygame.image.load("images/pion bleu.png")
        self.color.convert()

        self.is_blocked = block
        self.init_pos = pos_ini
        self.pos_ind = ind
        self.at_home = home
        self.at_prison = prison
        self.position = pos_ini
        self.onclick = click
        self.finished = statut


    def place_pion(self, ecran) :
        if self.at_home == True :
            ecran.blit(self.color, self.init_pos)
        else :
            ecran.blit(self.color, self.position)

    def deplacement_pion(self, ecran, fond_ecran) :

        if dices.dice_b.move == 6 and self.at_home == True :
            self.onclick = True
            self.position = parcours_bleu[0]
            self.pos_ind = 0
            dices.dice_b.nbp_at_home -= 1
            self.is_blocked = 0
            ecran.blit(fond_ecran, (0,0))
            ecran.blit(self.color, self.position)
            draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
            draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
            draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
            draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
            pygame.display.flip()
            self.at_home = False
        elif dices.dice_b.move == 6 and self.at_prison == True :
            self.onclick = True
            self.at_home = True
            self.position = self.init_pos
            dices.dice_b.nbp_at_home += 1
            self.is_blocked = 1
            ecran.blit(fond_ecran, (0,0))
            ecran.blit(self.color, self.position)
            draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
            draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
            draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
            draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
            pygame.display.flip()
            self.at_prison = False

        elif self.at_home == False and self.at_prison == False :
            i = parcours_bleu.index(self.position)
            self.pos_ind = i
            j = i + dices.dice_b.move
            if i >= 51 :
                if dices.dice_b.move > (56-i) :
                    self.is_blocked = 1
                    self.onclick = False
                    pass
                else :
                    self.onclick = True
                    for _ in range(i,j+1) :
                        self.is_blocked = 0
                        self.position = parcours_bleu[_]
                        self.pos_ind = i
                        ecran.blit(fond_ecran, (0,0))
                        ecran.blit(self.color, self.position)
                        draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
                        draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
                        draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
                        draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
                        pygame.display.flip()
                        time.sleep(0.15)
                        if self.position == parcours_bleu[56] :
                            self.pos_ind = i
                            self.finished = True
                            self.onclick = False
                            dices.dice_b.nbp_finished += 1
                            self.is_blocked = 1
                            break
            else :
                self.onclick = True
                for _ in range(i,j+1) :
                    self.is_blocked = 0
                    self.position = parcours_bleu[_]
                    self.pos_ind = i
                    ecran.blit(fond_ecran, (0,0))
                    ecran.blit(self.color, self.position)
                    draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
                    draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
                    draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
                    draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
                    pygame.display.flip()
                    time.sleep(0.15)

            self.pos_ind = parcours_bleu.index(self.position)

class Pion_rouge() :
    def __init__(self, pos_ini, ind = 0, block = 1, click = False, home = True, prison = False, statut = False) :
        self.name = "Rouge"
        
        self.color = pygame.image.load("images/pion rouge.png")
        self.color.convert()

        self.is_blocked = block
        self.init_pos = pos_ini
        self.pos_ind = ind
        self.at_home = home
        self.at_prison = prison
        self.position = pos_ini
        self.onclick = click
        self.finished = statut


    def place_pion(self, ecran) :
        if self.at_home == True :
            ecran.blit(self.color, self.init_pos)
        else :
            ecran.blit(self.color, self.position)

    def deplacement_pion(self, ecran, fond_ecran) :

        if dices.dice_r.move == 6 and self.at_home == True :
            self.onclick = True
            self.position = parcours_rouge[0]
            self.pos_ind = 0
            dices.dice_r.nbp_at_home -= 1
            self.is_blocked = 0
            ecran.blit(fond_ecran, (0,0))
            ecran.blit(self.color, self.position)
            draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
            draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
            draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
            draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
            pygame.display.flip()
            self.at_home = False
        elif dices.dice_r.move == 6 and self.at_prison == True :
            self.onclick = True
            self.at_home = True
            self.position = self.init_pos
            dices.dice_r.nbp_at_home += 1
            self.is_blocked = 1
            ecran.blit(fond_ecran, (0,0))
            ecran.blit(self.color, self.position)
            draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
            draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
            draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
            draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
            pygame.display.flip()
            self.at_prison = False

        elif self.at_home == False and self.at_prison == False :
            i = parcours_rouge.index(self.position)
            self.pos_ind = i
            j = i + dices.dice_r.move
            if i >= 51 :
                if dices.dice_r.move > (56-i) :
                    self.is_blocked = 1
                    self.onclick = False
                    pass
                else :
                    self.onclick = True
                    for _ in range(i,j+1) :
                        self.is_blocked = 0
                        self.position = parcours_rouge[_]
                        self.pos_ind = i
                        ecran.blit(fond_ecran, (0,0))
                        ecran.blit(self.color, self.position)
                        draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
                        draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
                        draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
                        draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
                        pygame.display.flip()
                        time.sleep(0.15)
                        if self.position == parcours_rouge[56] :
                            self.pos_ind = i
                            self.finished = True
                            self.onclick = False
                            dices.dice_r.nbp_finished += 1
                            self.is_blocked = 1
                            break
            else :
                self.onclick = True
                for _ in range(i,j+1) :
                    self.is_blocked = 0
                    self.position = parcours_rouge[_]
                    self.pos_ind = i
                    ecran.blit(fond_ecran, (0,0))
                    ecran.blit(self.color, self.position)
                    draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
                    draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
                    draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
                    draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
                    pygame.display.flip()
                    time.sleep(0.15)

            self.pos_ind = parcours_rouge.index(self.position)

class Pion_vert() :
    def __init__(self, pos_ini, ind = 0, block = 1, click = False, home = True, prison = False, statut = False) :
        self.name = "Vert"
        
        self.color = pygame.image.load("images/pion vert.png")
        self.color.convert()

        self.is_blocked = block
        self.init_pos = pos_ini
        self.pos_ind = ind
        self.at_home = home
        self.at_prison = prison
        self.position = pos_ini
        self.onclick = click
        self.finished = statut


    def place_pion(self, ecran) :
        if self.at_home == True :
            ecran.blit(self.color, self.init_pos)
        else :
            ecran.blit(self.color, self.position)

    def deplacement_pion(self, ecran, fond_ecran) :

        if dices.dice_v.move == 6 and self.at_home == True :
            self.onclick = True
            self.position = parcours_vert[0]
            self.pos_ind = 0
            dices.dice_v.nbp_at_home -= 1
            self.is_blocked = 0
            ecran.blit(fond_ecran, (0,0))
            ecran.blit(self.color, self.position)
            draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
            draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
            draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
            draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
            pygame.display.flip()
            self.at_home = False
        elif dices.dice_v.move == 6 and self.at_prison == True :
            self.onclick = True
            self.at_home = True
            self.position = self.init_pos
            dices.dice_v.nbp_at_home += 1
            self.is_blocked = 1
            ecran.blit(fond_ecran, (0,0))
            ecran.blit(self.color, self.position)
            draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
            draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
            draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
            draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
            pygame.display.flip()
            self.at_prison = False

        elif self.at_home == False and self.at_prison == False :
            i = parcours_vert.index(self.position)
            self.pos_ind = i
            j = i + dices.dice_v.move
            if i >= 51 :
                if dices.dice_v.move > (56-i) :
                    self.is_blocked = 1
                    self.onclick = False
                    pass
                else :
                    self.onclick = True
                    for _ in range(i,j+1) :
                        self.is_blocked = 0
                        self.position = parcours_vert[_]
                        self.pos_ind = i
                        ecran.blit(fond_ecran, (0,0))
                        ecran.blit(self.color, self.position)
                        draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
                        draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
                        draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
                        draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
                        pygame.display.flip()
                        time.sleep(0.15)
                        if self.position == parcours_vert[56] :
                            self.pos_ind = i
                            self.finished = True
                            self.onclick = False
                            dices.dice_v.nbp_finished += 1
                            self.is_blocked = 1
                            break
            else :
                self.onclick = True
                for _ in range(i,j+1) :
                    self.is_blocked = 0
                    self.position = parcours_vert[_]
                    self.pos_ind = i
                    ecran.blit(fond_ecran, (0,0))
                    ecran.blit(self.color, self.position)
                    draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
                    draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
                    draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
                    draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
                    pygame.display.flip()
                    time.sleep(0.15)

            self.pos_ind = parcours_vert.index(self.position)

class Pion_jaune() :
    def __init__(self, pos_ini, ind = 0, block = 1, click = False, home = True, prison = False, statut = False) :
        self.name = "Jaune"
        
        self.color = pygame.image.load("images/pion jaune.png")
        self.color.convert()

        self.is_blocked = block
        self.init_pos = pos_ini
        self.pos_ind = ind
        self.at_home = home
        self.at_prison = prison
        self.position = pos_ini
        self.onclick = click
        self.finished = statut


    def place_pion(self, ecran) :
        if self.at_home == True :
            ecran.blit(self.color, self.init_pos)
        else :
            ecran.blit(self.color, self.position)

    def deplacement_pion(self, ecran, fond_ecran) :

        if dices.dice_j.move == 6 and self.at_home == True :
            self.onclick = True
            self.position = parcours_jaune[0]
            self.pos_ind = 0
            dices.dice_j.nbp_at_home -= 1
            self.is_blocked = 0
            ecran.blit(fond_ecran, (0,0))
            ecran.blit(self.color, self.position)
            draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
            draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
            draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
            draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
            pygame.display.flip()
            self.at_home = False
        elif dices.dice_j.move == 6 and self.at_prison == True :
            self.onclick = True
            self.at_home = True
            self.position = self.init_pos
            dices.dice_j.nbp_at_home += 1
            self.is_blocked = 1
            ecran.blit(fond_ecran, (0,0))
            ecran.blit(self.color, self.position)
            draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
            draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
            draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
            draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
            pygame.display.flip()
            self.at_prison = False

        elif self.at_home == False and self.at_prison == False :
            i = parcours_jaune.index(self.position)
            self.pos_ind = i
            j = i + dices.dice_j.move
            if i >= 51 :
                if dices.dice_j.move > (56-i) :
                    self.is_blocked = 1
                    self.onclick = False
                    pass
                else :
                    self.onclick = True
                    for _ in range(i,j+1) :
                        self.is_blocked = 0
                        self.position = parcours_jaune[_]
                        self.pos_ind = i
                        ecran.blit(fond_ecran, (0,0))
                        ecran.blit(self.color, self.position)
                        draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
                        draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
                        draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
                        draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
                        pygame.display.flip()
                        time.sleep(0.15)
                        if self.position == parcours_jaune[56] :
                            self.pos_ind = i
                            self.finished = True
                            self.onclick = False
                            dices.dice_j.nbp_finished += 1
                            self.is_blocked = 1
                            break
            else :
                self.onclick = True
                for _ in range(i,j+1) :
                    self.is_blocked = 0
                    self.position = parcours_jaune[_]
                    self.pos_ind = i
                    ecran.blit(fond_ecran, (0,0))
                    ecran.blit(self.color, self.position)
                    draw_all_on_screen(ecran, pions_bleus, dices.dice_b, parcours_bleu)
                    draw_all_on_screen(ecran, pions_rouges, dices.dice_r, parcours_rouge)
                    draw_all_on_screen(ecran, pions_verts, dices.dice_v, parcours_vert)
                    draw_all_on_screen(ecran, pions_jaunes, dices.dice_j, parcours_jaune)
                    pygame.display.flip()
                    time.sleep(0.15)

            self.pos_ind = parcours_jaune.index(self.position)







####################### CREATION DES PIONS ######################
####################### CREATION DES PIONS ######################

pb1,pb2,pb3,pb4 = ((435,715),(435,575),(590,575),(590,715))
bleu_1 = Pion_bleu(pb1)
bleu_2 = Pion_bleu(pb2)
bleu_3 = Pion_bleu(pb3)
bleu_4 = Pion_bleu(pb4)
pions_bleus = [bleu_1, bleu_2, bleu_3, bleu_4]

pr1,pr2,pr3,pr4 = ((435,215),(435,75),(590,75),(590,215))
rouge_1 = Pion_rouge(pr1)
rouge_2 = Pion_rouge(pr2)
rouge_3 = Pion_rouge(pr3)
rouge_4 = Pion_rouge(pr4)
pions_rouges = [rouge_1, rouge_2, rouge_3, rouge_4]

pv1,pv2,pv3,pv4 = ((970,215),(970,75),(1125,75),(1125,215))
vert_1 = Pion_vert(pv1)
vert_2 = Pion_vert(pv2)
vert_3 = Pion_vert(pv3)
vert_4 = Pion_vert(pv4)
pions_verts = [vert_1, vert_2, vert_3, vert_4]

pj1,pj2,pj3,pj4 = ((970,715),(970,575),(1125,575),(1125,715))
jaune_1 = Pion_jaune(pj1)
jaune_2 = Pion_jaune(pj2)
jaune_3 = Pion_jaune(pj3)
jaune_4 = Pion_jaune(pj4)
pions_jaunes = [jaune_1, jaune_2, jaune_3, jaune_4]

##### ----------------################-------------- #######
##### ----------------################-------------- #######

def draw_all_on_screen(ecran, pion_ens, dice_, parcours_) :
    s_font = pygame.font.SysFont("Malgun Ghotic", 40)
    b_font = pygame.font.SysFont("Malgun Ghotic", 70)
    for p_ in pion_ens :
        p_.place_pion(ecran)

    b_text = b_font.render(f"{dice_.nbp_finished}", False, (255,255,255))
    ecran.blit(b_text, (parcours_[56][0] + 9, parcours_[56][1]))

    lis_pos = []
    for p_ in pion_ens :
        lis_pos.append(p_.position)
    pos_repetition = {}
    for p in lis_pos :
        if p in pos_repetition :
            pos_repetition[p] += 1
        else :
            pos_repetition[p] = 1
    
    for p in pos_repetition.items() :
        if p[1] > 1 :
            s_text = s_font.render(f"{p[1]}", False, (255,255,255))
            ecran.blit(s_text, (p[0][0]+15, p[0][1]+11))
            pygame.display.flip()

def choice_pion_to_move(pion_, dice_, next_dice, parcours_, dice_adv_1, dice_adv_2, dice_adv_3) :
    i = pion_.pos_ind
    h = dice_.nbp_at_home

    #cas où tous les pions sont à la maison
    if h==4 :
        if dice_.face != "images/dé - 6.png"  :
            pion_.onclick = False
            pion_.is_blocked = 1
        else :
            pion_.onclick = True
            pion_.is_blocked = 0
    
    #S'assurer qu'un pion à la maison ne peut être déplacé qu'en jouant 6
    elif pion_.at_home == True : 
        if dice_.face != "images/dé - 6.png" :
            pion_.onclick = False
            pion_.is_blocked = 1
        else :
            pion_.onclick = True
            pion_.is_blocked = 0
    
    #S'assurer qu'un pion en prison ne peut être déplacé qu'en jouant 6
    if pion_.at_prison == True :
        if dice_.face != "images/dé - 6.png" :
            pion_.onclick = False
            pion_.is_blocked = 1
        else :
            pion_.onclick = True
            pion_.is_blocked = 0

    # Pour les pions sur le point de loger (ayant terminé le parcours jusqu'à l'entrée finale)
    if pion_.at_home == False and pion_.at_prison == False :
        if i >= 51 :
            if dice_.move > (56-i) :
                pion_.onclick = False
                pion_.is_blocked = 1
                dice_.can_roll = False
                next_dice.can_roll = True
            else :
                pion_.onclick = True
                pion_.is_blocked = 0
        else :
            pion_.onclick = True
            pion_.is_blocked = 0
    
    # Détection des barrières
    list_bar_adv = []
    liste_dices_adv = [dice_adv_1, dice_adv_2, dice_adv_3]
    for di in liste_dices_adv :
        for z in range(len(di.barrieres)) :
            list_bar_adv.append(di.barrieres[z])
    
    bar_principale = (0,0)
    for bar in list_bar_adv :
        bar_index = parcours_.index(bar)
        if bar_index - i <= 6 and bar_index - i > 0 :
            bar_principale = bar
            break
    
    # Passer ou être bloqué par la barrière
    if bar_principale != (0,0) :
        bar_index = parcours_.index(bar_principale)
        print("Joueur ", pion_.name, " : Barrière principale à la position ", bar_principale)
        if dice_.face != "images/dé - 6.png" :
            if dice_.move >= bar_index - i :
                pion_.onclick = False
                pion_.is_blocked = 1
            else :
                pion_.onclick = True
                pion_.is_blocked = 0
        else :
            if bar_index - i == 6 :
                pion_.onclick = False
                pion_.is_blocked = 1
            else :
                pion_.onclick = True
                pion_.is_blocked = 0


    dice_.sum_blocked += pion_.is_blocked

##### --------------------------------------- #######

def move_pion_choised(ecran, fond_ecran, event, pion_, pions_ens, dice_, next_dice) :
    font = pygame.font.SysFont("Malgun Ghotic", 70)
    if (event.button == 1) and ((event.pos[0] > pion_.position[0]) and (event.pos[0] < pion_.position[0]+40)) and ((event.pos[1] > pion_.position[1]) and (event.pos[1] < pion_.position[1]+40)) :
        pion_.deplacement_pion(ecran, fond_ecran)
        for p_ in pions_ens :
            p_.onclick = False

        if dice_.face == "images/dé - 6.png" :
            if pion_.pos_ind >= 51 :
                dice_.can_roll = False
                next_dice.can_roll = True
            else :
                dice_.can_roll = True
                next_dice.can_roll = False
        else :
            if pion_.pos_ind >= 51 :
                if dice_.move < 56-pion_.pos_ind :
                    dice_.can_roll = False
                    next_dice.can_roll = True
            elif pion_.at_home == True :
                dice_.can_roll = False
                next_dice.can_roll = True


        if pion_.finished == True :
            text = font.render(f"{dice_.nbp_finished}", False, (255,255,255))
            ecran.blit(text, (parcours_bleu[56][0] + 9, parcours_bleu[56][1]))
            pions_ens.remove(pion_)
            pygame.display.flip()
            dice_.can_roll = True
            next_dice.can_roll = False
            

def auto_move_pion (ecran, fond_ecran, pion_, pions_ens, dice_, next_dice):
    font = pygame.font.SysFont("Malgun Ghotic", 70)
    pion_.deplacement_pion(ecran, fond_ecran)
    for p_ in pions_ens :
        p_.onclick = False

    if dice_.face == "images/dé - 6.png" :
        if pion_.pos_ind >= 51 :
            dice_.can_roll = False
            next_dice.can_roll = True
        else :
            dice_.can_roll = True
            next_dice.can_roll = False
    else :
        if pion_.pos_ind >= 51 :
            if dice_.move < 56-pion_.pos_ind :
                dice_.can_roll = False
                next_dice.can_roll = True
        elif pion_.at_home == True :
            dice_.can_roll = False
            next_dice.can_roll = True
    
    if pion_.finished == True :
        text = font.render(f"{dice_.nbp_finished}", False, (255,255,255))
        ecran.blit(text, (parcours_bleu[56][0] + 9, parcours_bleu[56][1]))
        pions_ens.remove(pion_)
        pygame.display.flip()
        dice_.can_roll = True
        next_dice.can_roll = False

def tchop_pion(pion_, dice_, next_dice, pions_adv_1, pions_adv_2, pions_adv_3, prison) :
    liste_pions_adv = []
    for pi in pions_adv_1 :
        liste_pions_adv.append(pi)
    for pi in pions_adv_2 :
        liste_pions_adv.append(pi)
    for pi in pions_adv_3 :
        liste_pions_adv.append(pi)
    
    dice_.nb_prisonners = 0
    for adv in liste_pions_adv :
        for pri_pos in prison :
            if adv.position == pri_pos :
                dice_.nb_prisonners += 1

    pri_occ = False
    for adv in liste_pions_adv :
        if pion_.position == adv.position :
            for pri_pos in prison :
                for advers in liste_pions_adv :
                    if advers.position == pri_pos :
                        pri_occ = True
                        break
                    else :
                        pri_occ = False
                if pri_occ == False :
                    adv.position = pri_pos
                    break
            adv.at_prison = True
            adv.at_home = False
            adv.onclick = False
            adv.is_blocked = 1
            dice_.can_roll = True
            next_dice.can_roll = False

def create_barriere(pion_ens, dice_) :
    lis_pos = []
    for p_ in pion_ens :
        lis_pos.append(p_.position)
    pos_repetition = {}
    for p in lis_pos :
        if p in pos_repetition :
            pos_repetition[p] += 1
        else :
            pos_repetition[p] = 1
    
    nb_barr = 0
    for p in pos_repetition.items() :
        if p[1] > 1 :
            dice_.barrieres.append(p[0])
            nb_barr += 1
            dice_.bar_existence = True
    
    if nb_barr == 0 :
        dice_.barrieres = []
        dice_.bar_existence = False


pygame.quit()