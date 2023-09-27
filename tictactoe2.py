import pygame

from minimax import *


class Button:
    def __init__(self, x, y, width, height, text, text_color, button_color):
        self.comicSansPath = "/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/COMIC.TTF"
        self.font = pygame.font.Font(self.comicSansPath, 36)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.button_color = button_color

    def draw(self, surface):

        pygame.draw.rect(surface, self.button_color, self.rect)
        font = pygame.font.Font(self.comicSansPath, 15)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)



class MainScreen:
    def __init__(self, screen, changeScreenCallback):
        comicSansPath = "/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/COMIC.TTF"
        self.screen = screen
        self.font = pygame.font.Font(comicSansPath, 36)
        self.onePlayerButton = playOnePlayerButton = Button(200, 450, 100, 50, "1 Player X", (255,255,255), (0, 68, 102))
        self.onePlayerButtonO = playOnePlayerButtonO = Button(400, 450, 100, 50, "1 Player O", (255, 255, 255), (0,68,102))
        self.twoPlayerButton = playTwoPlayerButton = Button(600, 450, 100, 50, "2 Players", (255, 255, 255), (255, 25, 64))
        self.changeScreenCallback = changeScreenCallback
        # self.gameScreenOnePlayer = GameScreenOnePlayer(screen)

        
    def update(self):
        gray = [46,46,46]
        self.screen.fill(gray)
        self.text = self.font.render("Welcome to Tic Tac Toe!", True, (255, 255, 255))
        self.text_width, self.text_height = self.text.get_size()
        self.x = (900 - self.text_width) // 2
        self.screen.blit(self.text, (self.x,100))
        self.onePlayerButton.draw(self.screen)
        self.twoPlayerButton.draw(self.screen)
        self.onePlayerButtonO.draw(self.screen)
        pygame.display.update()

    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.onePlayerButton.is_clicked(event.pos):
                self.changeScreenCallback(GameScreenOnePlayer(self.screen, self.changeScreenCallback))
                return GameScreenOnePlayer(self.screen, self.changeScreenCallback)
                
            elif self.onePlayerButtonO.is_clicked(event.pos):
                self.changeScreenCallback(GameScreenOnePlayer2(self.screen, self.changeScreenCallback))
                return GameScreenOnePlayer2(self.screen, self.changeScreenCallback)
            
            elif self.twoPlayerButton.is_clicked(event.pos):
                self.changeScreenCallback(GameScreenTwoPlayer(self.screen, self.changeScreenCallback))
                return GameScreenTwoPlayer(self.screen, self.changeScreenCallback)


class GameScreenOnePlayer2:
    def __init__(self, screen, changeScreenCallback):
        self.currentBoardState = [0,1,2,3,4,5,6,7,8]
        comicSansPath = "/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/COMIC.TTF"
        self.font = pygame.font.Font(comicSansPath, 20)
        self.screen = screen
        self.image = pygame.image.load("/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/TicTacToeGrid.png")
        self.XPlayer = pygame.image.load("/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/x_player.png")
        self.XPlayer = pygame.transform.scale(self.XPlayer, (100,100))
        self.OPlayer = pygame.image.load("/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/o_player.png")
        self.OPlayer = pygame.transform.scale(self.OPlayer, (100,100))
        self.positions = []
        self.key_pressed = False
        self.changeScreenCallback = changeScreenCallback


    def reset(self):
        self.key_pressed = False

    def update(self):
        self.screen.blit(self.image, (0,0))
        self.text = self.font.render("Press a Button from 1 to 9!", True, (255, 255, 255))
        self.text2 = self.font.render("Press 0 to start! | Press R to restart! | Press Q to go to Main Screen!", True, (255, 255, 255))
        self.text2_width, self.text2_height = self.text2.get_size()
        self.text_width, self.text_height = self.text.get_size()
        self.x1 = (900 - self.text_width) // 2
        self.screen.blit(self.text, (self.x1, 30))

        self.x2 = (900 - self.text2_width) // 2
        self.screen.blit(self.text2, (self.x2, 650))
        for position, player in self.positions:
            self.drawMoves(position, player)
        

    def drawMoves(self, position, player):
        if player == "X":
            if position == 0:
                self.screen.blit(self.XPlayer, (150, 120))
            elif position == 1:
                self.screen.blit(self.XPlayer, (400,120))
            elif position == 2:
                self.screen.blit(self.XPlayer, (650,120))
            elif position == 3:
                self.screen.blit(self.XPlayer, (150,280))
            elif position == 4:
                self.screen.blit(self.XPlayer, (400,280))
            elif position == 5:
                self.screen.blit(self.XPlayer, (650,280))
            elif position == 6:
                self.screen.blit(self.XPlayer, (150,440))
            elif position == 7:
                self.screen.blit(self.XPlayer, (400,440))
            elif position == 8:
                self.screen.blit(self.XPlayer, (650,440))
        
        elif player == "O":
            if position == 0:
                self.screen.blit(self.OPlayer, (150,120))
            elif position == 1:
                self.screen.blit(self.OPlayer, (400,120))
            elif position == 2:
                self.screen.blit(self.OPlayer, (650, 120))
            elif position == 3:
                self.screen.blit(self.OPlayer, (150, 280))
            elif position == 4:
                self.screen.blit(self.OPlayer, (400, 280))
            elif position == 5:
                self.screen.blit(self.OPlayer, (650, 280))
            elif position == 6:
                self.screen.blit(self.OPlayer, (150, 440))
            elif position == 7:
                self.screen.blit(self.OPlayer, (400, 440))
            elif position == 8:
                self.screen.blit(self.OPlayer, (650, 440))

        





    def handleEvents(self, event):
        keys = pygame.key.get_pressed()




        if event.type == pygame.KEYUP:
            if ((event.key == pygame.K_0) or
                (event.key == pygame.K_1) or
                (event.key == pygame.K_2) or
                (event.key == pygame.K_3) or
                (event.key == pygame.K_4) or
                (event.key == pygame.K_5) or
                (event.key == pygame.K_6) or
                (event.key == pygame.K_7) or
                (event.key == pygame.K_8) or
                (event.key == pygame.K_9)):
                    self.key_pressed = False

        if keys[pygame.K_0] and not self.key_pressed:
            self.key_pressed = True     
            print(self.currentBoardState)
            _, first_play = maxValue(self.currentBoardState)
            self.positions.append((first_play, "X"))
            self.currentBoardState[first_play] = "X"
            print(self.currentBoardState)

        if keys[pygame.K_1] and not self.key_pressed and not any(0 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((0, "O"))
            self.currentBoardState[0] = "O"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = maxValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "X"))
                self.currentBoardState[response] = "X"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)


        elif keys[pygame.K_2] and not self.key_pressed and not any(1 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((1, "O"))
            self.currentBoardState[1] = "O"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = maxValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "X"))
                self.currentBoardState[response] = "X"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_3] and not self.key_pressed and not any(2 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((2, "O"))
            self.currentBoardState[2] = "O"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = maxValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "X"))
                self.currentBoardState[response] = "X"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_4] and not self.key_pressed and not any(3 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((3, "O"))
            self.currentBoardState[3] = "O"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = maxValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "X"))
                self.currentBoardState[response] = "X"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_5] and not self.key_pressed and not any(4 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((4, "O"))
            self.currentBoardState[4] = "O"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = maxValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "X"))
                self.currentBoardState[response] = "X"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)
            

        elif keys[pygame.K_6] and not self.key_pressed and not any(5 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((5, "O"))
            self.currentBoardState[5] = "O"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = maxValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "X"))
                self.currentBoardState[response] = "X"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_7] and not self.key_pressed and not any(6 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((6, "O"))
            self.currentBoardState[6] = "O"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = maxValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "X"))
                self.currentBoardState[response] = "X"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_8] and not self.key_pressed and not any(7 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((7, "O"))
            self.currentBoardState[7] = "O"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = maxValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "X"))
                self.currentBoardState[response] = "X"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_9] and not self.key_pressed and not any(8 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((8, "O"))
            self.currentBoardState[8] = "O"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = maxValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "X"))
                self.currentBoardState[response] = "X"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)
            
        elif keys[pygame.K_r] and not self.key_pressed:
            
            self.key_pressed = True
            self.currentBoardState = [0,1,2,3,4,5,6,7,8]
            self.positions = []

        elif keys[pygame.K_q] and not self.key_pressed:
            self.key_pressed = True
            self.currentBoardState = [0,1,2,3,4,5,6,7,8]
            self.positions = []
            self.changeScreenCallback(MainScreen(self.screen, self.changeScreenCallback))
            return MainScreen(self.screen, self.changeScreenCallback)
            

    


class GameScreenOnePlayer:
    def __init__(self, screen, changeScreenCallback):
        self.currentBoardState = [0,1,2,3,4,5,6,7,8]
        comicSansPath = "/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/COMIC.TTF"
        self.font = pygame.font.Font(comicSansPath, 30)
        self.screen = screen
        self.image = pygame.image.load("/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/TicTacToeGrid.png")
        self.XPlayer = pygame.image.load("/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/x_player.png")
        self.XPlayer = pygame.transform.scale(self.XPlayer, (100,100))
        self.OPlayer = pygame.image.load("/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/o_player.png")
        self.OPlayer = pygame.transform.scale(self.OPlayer, (100,100))
        self.positions = []
        self.key_pressed = False
        self.changeScreenCallback = changeScreenCallback
    
    def reset(self):
        self.key_pressed = False

    def update(self):
        self.screen.blit(self.image, (0,0))
        self.text = self.font.render("Press a Button from 1 to 9!", True, (255, 255, 255))
        self.text_width, self.text_height = self.text.get_size()
        self.x1 = (900 - self.text_width) // 2
        self.screen.blit(self.text, (self.x1, 30))
        self.text2 = self.font.render("Press R to restart! | Press Q to go to Main Screen!", True, (255, 255, 255))
        self.text2_width, self.text2_height = self.text2.get_size()
        self.x2 = (900 - self.text2_width) // 2
        self.screen.blit(self.text2, (self.x2, 650))
        for position, player in self.positions:
            self.drawMoves(position, player)

    
    def drawMoves(self, position, player):
        if player == "X":
            if position == 0:
                self.screen.blit(self.XPlayer, (150, 120))
            elif position == 1:
                self.screen.blit(self.XPlayer, (400,120))
            elif position == 2:
                self.screen.blit(self.XPlayer, (650,120))
            elif position == 3:
                self.screen.blit(self.XPlayer, (150,280))
            elif position == 4:
                self.screen.blit(self.XPlayer, (400,280))
            elif position == 5:
                self.screen.blit(self.XPlayer, (650,280))
            elif position == 6:
                self.screen.blit(self.XPlayer, (150,440))
            elif position == 7:
                self.screen.blit(self.XPlayer, (400,440))
            elif position == 8:
                self.screen.blit(self.XPlayer, (650,440))
        
        elif player == "O":
            if position == 0:
                self.screen.blit(self.OPlayer, (150,120))
            elif position == 1:
                self.screen.blit(self.OPlayer, (400,120))
            elif position == 2:
                self.screen.blit(self.OPlayer, (650, 120))
            elif position == 3:
                self.screen.blit(self.OPlayer, (150, 280))
            elif position == 4:
                self.screen.blit(self.OPlayer, (400, 280))
            elif position == 5:
                self.screen.blit(self.OPlayer, (650, 280))
            elif position == 6:
                self.screen.blit(self.OPlayer, (150, 440))
            elif position == 7:
                self.screen.blit(self.OPlayer, (400, 440))
            elif position == 8:
                self.screen.blit(self.OPlayer, (650, 440))

        





    def handleEvents(self, event):
        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYUP:
            if ((event.key == pygame.K_0) or
                (event.key == pygame.K_1) or
                (event.key == pygame.K_2) or
                (event.key == pygame.K_3) or
                (event.key == pygame.K_4) or
                (event.key == pygame.K_5) or
                (event.key == pygame.K_6) or
                (event.key == pygame.K_7) or
                (event.key == pygame.K_8) or
                (event.key == pygame.K_9)):
                    self.key_pressed = False

        if keys[pygame.K_1] and not self.key_pressed and not any(0 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((0, "X"))
            self.currentBoardState[0] = "X"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = minValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "O"))
                self.currentBoardState[response] = "O"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)


        elif keys[pygame.K_2] and not self.key_pressed and not any(1 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((1, "X"))
            self.currentBoardState[1] = "X"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = minValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "O"))
                self.currentBoardState[response] = "O"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_3] and not self.key_pressed and not any(2 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((2, "X"))
            self.currentBoardState[2] = "X"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = minValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "O"))
                self.currentBoardState[response] = "O"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_4] and not self.key_pressed and not any(3 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((3, "X"))
            self.currentBoardState[3] = "X"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = minValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "O"))
                self.currentBoardState[response] = "O"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_5] and not self.key_pressed and not any(4 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((4, "X"))
            self.currentBoardState[4] = "X"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = minValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "O"))
                self.currentBoardState[response] = "O"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)
            

        elif keys[pygame.K_6] and not self.key_pressed and not any(5 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((5, "X"))
            self.currentBoardState[5] = "X"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = minValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "O"))
                self.currentBoardState[response] = "O"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_7] and not self.key_pressed and not any(6 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((6, "X"))
            self.currentBoardState[6] = "X"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = minValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "O"))
                self.currentBoardState[response] = "O"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_8] and not self.key_pressed and not any(7 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((7, "X"))
            self.currentBoardState[7] = "X"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = minValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "O"))
                self.currentBoardState[response] = "O"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_9] and not self.key_pressed and not any(8 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.positions.append((8, "X"))
            self.currentBoardState[8] = "X"
            print(self.currentBoardState)
            if printWinner(self.currentBoardState) == False:
                _, response = minValue(self.currentBoardState)
                print(response)
                self.positions.append((response, "O"))
                self.currentBoardState[response] = "O"
                print(self.currentBoardState)
                if printWinner(self.currentBoardState) != False:
                    printWinner(self.currentBoardState)

            else:
                printWinner(self.currentBoardState)
            
        elif keys[pygame.K_r] and not self.key_pressed:
            
            self.key_pressed = True
            self.currentBoardState = [0,1,2,3,4,5,6,7,8]
            self.positions = []

        elif keys[pygame.K_q] and not self.key_pressed:
            self.key_pressed = True
            self.currentBoardState = [0,1,2,3,4,5,6,7,8]
            self.positions = []
            self.changeScreenCallback(MainScreen(self.screen, self.changeScreenCallback))
            return MainScreen(self.screen, self.changeScreenCallback)
        
class GameScreenTwoPlayer:
    def __init__(self, screen, changeScreenCallback):
        self.currentBoardState = [0,1,2,3,4,5,6,7,8]
        comicSansPath = "/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/COMIC.TTF"
        self.font = pygame.font.Font(comicSansPath, 30)
        self.screen = screen
        self.image = pygame.image.load("/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/TicTacToeGrid.png")
        self.XPlayer = pygame.image.load("/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/x_player.png")
        self.XPlayer = pygame.transform.scale(self.XPlayer, (100,100))
        self.OPlayer = pygame.image.load("/Users/gerocastano8/Documents/Python Projects/Projects/TicTacToe/o_player.png")
        self.OPlayer = pygame.transform.scale(self.OPlayer, (100,100))
        self.positions = []
        self.key_pressed = False
        self.changeScreenCallback = changeScreenCallback

    def update(self):
        self.screen.blit(self.image, (0,0))
        self.text = self.font.render("Press a Button from 1 to 9!", True, (255, 255, 255))
        self.text_width, self.text_height = self.text.get_size()
        self.x1 = (900 - self.text_width) // 2
        self.screen.blit(self.text, (self.x1, 30))
        self.text2 = self.font.render("Press R to restart! | Press Q to go to Main Screen!", True, (255, 255, 255))
        self.text2_width, self.text2_height = self.text2.get_size()
        self.x2 = (900 - self.text2_width) // 2
        self.screen.blit(self.text2, (self.x2, 650))
        for position, player in self.positions:
            self.drawMoves(position, player)
    

    def drawMoves(self, position, player):
        if player == "X":
            if position == 0:
                self.screen.blit(self.XPlayer, (150, 120))
            elif position == 1:
                self.screen.blit(self.XPlayer, (400,120))
            elif position == 2:
                self.screen.blit(self.XPlayer, (650,120))
            elif position == 3:
                self.screen.blit(self.XPlayer, (150,280))
            elif position == 4:
                self.screen.blit(self.XPlayer, (400,280))
            elif position == 5:
                self.screen.blit(self.XPlayer, (650,280))
            elif position == 6:
                self.screen.blit(self.XPlayer, (150,440))
            elif position == 7:
                self.screen.blit(self.XPlayer, (400,440))
            elif position == 8:
                self.screen.blit(self.XPlayer, (650,440))
        
        elif player == "O":
            if position == 0:
                self.screen.blit(self.OPlayer, (150,120))
            elif position == 1:
                self.screen.blit(self.OPlayer, (400,120))
            elif position == 2:
                self.screen.blit(self.OPlayer, (650, 120))
            elif position == 3:
                self.screen.blit(self.OPlayer, (150, 280))
            elif position == 4:
                self.screen.blit(self.OPlayer, (400, 280))
            elif position == 5:
                self.screen.blit(self.OPlayer, (650, 280))
            elif position == 6:
                self.screen.blit(self.OPlayer, (150, 440))
            elif position == 7:
                self.screen.blit(self.OPlayer, (400, 440))
            elif position == 8:
                self.screen.blit(self.OPlayer, (650, 440))
        
    
    def handleEvents(self, event):
        keys = pygame.key.get_pressed()




        if event.type == pygame.KEYUP:
            if ((event.key == pygame.K_0) or
                (event.key == pygame.K_1) or
                (event.key == pygame.K_2) or
                (event.key == pygame.K_3) or
                (event.key == pygame.K_4) or
                (event.key == pygame.K_5) or
                (event.key == pygame.K_6) or
                (event.key == pygame.K_7) or
                (event.key == pygame.K_8) or
                (event.key == pygame.K_9)):
                    self.key_pressed = False

        if keys[pygame.K_1] and not self.key_pressed and not any(0 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.currentMark = getCurrMark(self.currentBoardState)
            self.positions.append((0, self.currentMark))
            self.currentBoardState[0] = self.currentMark
            
            if printWinner(self.currentBoardState) != False:
                printWinner(self.currentBoardState)
        
        elif keys[pygame.K_2] and not self.key_pressed and not any(1 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.currentMark = getCurrMark(self.currentBoardState)
            self.positions.append((1, self.currentMark))
            self.currentBoardState[1] = self.currentMark

            if printWinner(self.currentBoardState) != False:
                printWinner(self.currentBoardState)

        
        elif keys[pygame.K_3] and not self.key_pressed and not any(2 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.currentMark = getCurrMark(self.currentBoardState)
            self.positions.append((2, self.currentMark))
            self.currentBoardState[2] = self.currentMark

            if printWinner(self.currentBoardState) != False:
                printWinner(self.currentBoardState)
        
        elif keys[pygame.K_4] and not self.key_pressed and not any(3 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.currentMark = getCurrMark(self.currentBoardState)
            self.positions.append((3, self.currentMark))
            self.currentBoardState[3] = self.currentMark

            if printWinner(self.currentBoardState) != False:
                printWinner(self.currentBoardState)
                
                
        
        elif keys[pygame.K_5] and not self.key_pressed and not any(4 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.currentMark = getCurrMark(self.currentBoardState)
            self.positions.append((4, self.currentMark))
            self.currentBoardState[4] = self.currentMark

            if printWinner(self.currentBoardState) != False:
                printWinner(self.currentBoardState)
        
        elif keys[pygame.K_6] and not self.key_pressed and not any(5 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.currentMark = getCurrMark(self.currentBoardState)
            self.positions.append((5, self.currentMark))
            self.currentBoardState[5] = self.currentMark

            if printWinner(self.currentBoardState) != False:
                printWinner(self.currentBoardState)
        
        elif keys[pygame.K_7] and not self.key_pressed and not any(6 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.currentMark = getCurrMark(self.currentBoardState)
            self.positions.append((6, self.currentMark))
            self.currentBoardState[6] = self.currentMark

            if printWinner(self.currentBoardState) != False:
                printWinner(self.currentBoardState)
        
        elif keys[pygame.K_8] and not self.key_pressed and not any(7 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.currentMark = getCurrMark(self.currentBoardState)
            self.positions.append((7, self.currentMark))
            self.currentBoardState[7] = self.currentMark

            if printWinner(self.currentBoardState) != False:
                printWinner(self.currentBoardState)
        
        elif keys[pygame.K_9] and not self.key_pressed and not any(8 in tpl for tpl in self.positions):
            self.key_pressed = True
            self.currentMark = getCurrMark(self.currentBoardState)
            self.positions.append((8, self.currentMark))
            self.currentBoardState[8] = self.currentMark

            if printWinner(self.currentBoardState) != False:
                printWinner(self.currentBoardState)

        elif keys[pygame.K_r] and not self.key_pressed:
            
            self.key_pressed = True
            self.currentBoardState = [0,1,2,3,4,5,6,7,8]
            self.positions = []

        elif keys[pygame.K_q] and not self.key_pressed:
            self.key_pressed = True
            self.currentBoardState = [0,1,2,3,4,5,6,7,8]
            self.positions = []
            self.changeScreenCallback(MainScreen(self.screen, self.changeScreenCallback))
            return MainScreen(self.screen, self.changeScreenCallback)
        


        
        

def main():

    pygame.init()
    WIDTH, HEIGHT = 900, 700
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")

    def change_screen(new_screen):
        nonlocal currentScreen
        currentScreen = new_screen
    currentScreen = MainScreen(WIN, change_screen)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            else:
                currentScreen.handleEvents(event)
                
        currentScreen.update()
        pygame.display.flip()



    

    pygame.quit()

if __name__ == "__main__":

    main()

    