import pygame
import random
import time

pygame.init()

class Dice :
    def __init__(self, dice_face = "images/dé - 6.png", roll = False, nombre = 6, sum_block = 4, prisonners = 0, nbp_ath = 4, nbp_fin = 0, mov = 0, barrer = [], bar_exist = False) :
        self.face = dice_face
        self.number = nombre
        self.can_roll = roll
        self.move = mov
        self.sum_blocked = sum_block
        self.nbp_at_home = nbp_ath
        self.nbp_finished = nbp_fin
        self.nb_prisonners = prisonners
        self.barrieres = barrer
        self.bar_existence = bar_exist
        
    def change_dice_face(self) :
        face_number = random.randint(1,6)
        if face_number == 1 :
            self.face = "images/dé - 1.png"
            self.move = 1
            return self.face
        elif face_number == 2 :
            self.face = "images/dé - 2.png"
            self.move = 2
            return self.face
        elif face_number == 3 :
            self.face = "images/dé - 3.png"
            self.move = 3
            return self.face
        elif face_number == 4 :
            self.face = "images/dé - 4.png"
            self.move = 4
            return self.face
        elif face_number == 5 :
            self.face = "images/dé - 5.png"
            self.move = 5
            return self.face
        elif face_number == 6 :
            self.face = "images/dé - 6.png"
            self.move = 6
            return self.face


def draw_dices(ecran, face_attente, player_dice, dice_pos, fond_ecran) :
    ecran.blit(face_attente, dice_pos)
    pygame.display.flip()
    time.sleep(0.5)

    blue_dice = pygame.image.load(Dice.change_dice_face(player_dice))
    blue_dice.convert()
    ecran.blit(blue_dice, dice_pos)
    pygame.display.flip()
    
    time.sleep(0.5)
    ecran.blit(fond_ecran, (0,0))

dice_b = Dice()
dice_r = Dice()
dice_v = Dice()
dice_j = Dice()


pygame.quit()