#importing stuff
import pygame
import random
import math

def main():
    #second thing the code should do
    pygame.init()

    scissors = pygame.mixer.Sound("Sounds/scissors.mp3")

    end = False
    winner = ""
    displayX = 730
    displayY = 1000

    speed = 0.1

    #debug stuff
    debug = False
    font = ""
    textRect = ""
    text = ""
    if debug:
        font = pygame.font.Font('freesansbold.ttf', 32)
        #text = font.render("x: " + paperX[i] + "  " + "y: " + paperY[i], True, green, blue)

    #number of rocks, papers and scisors spawned (can get laggy with larger numbers)
    n_rock = 50
    n_paper = 50
    n_scisors = 50

    #sprites
    s_rock = []
    s_paper = []
    s_scisors = []


    #rock
    rectr = []
    rockX = []
    rockY = []


    #paper
    rectp = []
    paperX = []
    paperY = []

    #sciscors
    rects = []
    scisorsX = []
    scisorsY = []

    def ls(list):
        """
        stands for "List Size"

        gets size of the list
        """
        size = 0
        for i in range(list):
            size += 1

        return size

    def giofsnl(list):
        """
        stands for "Get the Index OF the Smallest Number in a List"

        takes one argument, when called, returns the index of the smallest number in the list
        """
        try:
            min_num = max(list)
            for i in list:
                if i < min_num:
                    min_num = i

            return list.index(min_num)

        except:
            return None

    def sqr(num):
        """
        basic function to square a number
        """
        return num * num

    screen = pygame.display.set_mode((displayX, displayY))

    pygame.display.set_caption("rps")

    #loading the rock
    for i in range(n_rock):
        print("spawning rocks")
        rectr.append(pygame.Rect(0, 0, 36, 36))
        s_rock.append(pygame.image.load("sprites/rock.png"))
        rockX.append(random.randint(10, displayX - 10))
        rockY.append(random.randint(10, displayY - 10))
        print("position x:", rockX[i], " y:", rockY[i])

    #loading the paper
    for i in range(n_paper):
        print("spawning papers")
        rectp.append(pygame.Rect(0, 0, 36, 36))
        s_paper.append(pygame.image.load("sprites/paper.png"))
        paperX.append(random.randint(10, displayX - 10))
        paperY.append(random.randint(10, displayY - 10))
        print("position x:", paperX[i], " y:", paperY[i])

    #loading the scisors
    for i in range(n_scisors):
        print("spawning scisors")
        rects.append(pygame.Rect(0, 0, 36, 36))
        s_scisors.append(pygame.image.load("sprites/scisors.png"))
        scisorsX.append(random.randint(10, displayX - 10))
        scisorsY.append(random.randint(10, displayY - 10))
        print("position x:", paperX[i], " y:", paperY[i])

    def sprite(x, y, i):
        """
        draws the given image to the x and y coords
        """
        screen.blit(pygame.transform.scale(i, (30, 30)), (x, y))

    on = True

    while on:
        screen.fill((0, 60, 100))
        #rock, paper and sciscors

        #ENDING CONDITION:
        if ls(n_rock) <= 0 and ls(n_paper) <= 0:
            end = True
            winner = "scisors"
        elif ls(n_rock) <= 0 and ls(n_scisors) <=0:
            end = True
            winner = "paper"
        elif ls(n_paper) <= 0 and ls(n_scisors) <= 0:
            end = True
            winner = "rock"


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()

            if event.type == pygame.QUIT:
                on = False
                exit()
###################################################################################################################
        #ROCK:
        for i in range(n_rock):
            rang = []
            try:
                #figuring out the closest scisors
                for j in range(n_scisors):

                    #AB = √(|Ya - Yb|^2 + |Xa - Xb|^2)

                    Xrange = abs(rockX[i] - scisorsX[j])
                    Yrange = abs(rockY[i] - scisorsY[j])
                    sqrang = sqr(Xrange) + sqr(Yrange)
                    rang.append(math.sqrt(sqrang))

                ind = giofsnl(rang)

                #print(rang)
                #print(ind)
                if debug:
                    try:
                        pygame.draw.line(screen, (80, 20, 30), (rockX[i], rockY[i]), (scisorsX[ind], scisorsY[ind]), 3)
                    except:
                        pass

                try:
                    #movement

                    #X coordinate
                    if rockX[i] <= scisorsX[ind]:
                        #if i == 0:
                        #    print("+", rockX[i], scisorsX[ind])
                        rockX[i] += speed

                    elif rockX[i] >= scisorsX[ind]:
                        #if i == 0:
                        #    print("-", rockX[i], scisorsX[ind])
                        rockX[i] -= speed

                    elif rockX[i] == scisorsX[ind]:
                        pass


                    #Y coordinate
                    if rockY[i] <= scisorsY[ind]:
                        rockY[i] += speed

                    elif rockY[i] >= scisorsY[ind]:
                        rockY[i] -= speed

                    elif rockY[i] == scisorsY[ind]:
                        pass

                except:
                    try:
                        #figuring out the closest scisors
                        for j in range(n_scisors):

                            #AB = √(|Ya - Yb|^2 + |Xa - Xb|^2)

                            Xrange = abs(rockX[i] - scisorsX[j])
                            Yrange = abs(rockY[i] - scisorsY[j])
                            sqrang = sqr(Xrange) + sqr(Yrange)
                            rang.append(math.sqrt(sqrang))

                        ind = giofsnl(rang)


                        #movement

                        #X coordinate
                        if rockX[i] <= scisorsX[ind]:
                            #if i == 0:
                            #    print("+", rockX[i], scisorsX[ind])
                            rockX[i] += speed

                        elif rockX[i] >= scisorsX[ind]:
                            #if i == 0:
                            #    print("-", rockX[i], scisorsX[ind])
                            rockX[i] -= speed

                        elif rockX[i] == scisorsX[ind]:
                            pass


                        #Y coordinate
                        if rockY[i] <= scisorsY[ind]:
                            rockY[i] += speed

                        elif rockY[i] >= scisorsY[ind]:
                            rockY[i] -= speed

                        elif rockY[i] == scisorsY[ind]:
                            pass

                    except:
                        pass


            except:
                try:
                    #figuring out the closest scisors
                    for j in range(n_paper):

                        #AB = √(|Ya - Yb|^2 + |Xa - Xb|^2)

                        Xrange = abs(rockX[i] - paperX[j])
                        Yrange = abs(rockY[i] - paperY[j])
                        sqrang = sqr(Xrange) + sqr(Yrange)
                        rang.append(math.sqrt(sqrang))

                except:
                    #winning condition is met, simulation is ended.
                    end = True
                    winner = "rock"


                ind = giofsnl(rang)

                #print(rang)
                #print(ind)
                if debug:
                    try:
                        pygame.draw.line(screen, (80, 20, 30), (rockX[i], rockY[i]), (paperX[ind], paperY[ind]), 3)
                    except:
                        pass

                try:
                    #movement

                    #X coordinate
                    if rockX[i] <= paperX[ind]:
                        #if i == 0:
                        #    print("+", rockX[i], scisorsX[ind])
                        rockX[i] -= speed

                    elif rockX[i] >= paperX[ind]:
                        #if i == 0:
                        #    print("-", rockX[i], scisorsX[ind])
                        rockX[i] += speed


                    #Y coordinate
                    if rockY[i] <= paperY[ind]:
                        rockY[i] -= speed

                    elif rockY[i] >= paperY[ind]:
                        rockY[i] += speed

                except:
                    try:
                        #figuring out the closest scisors
                        for j in range(n_paper):

                            #AB = √(|Ya - Yb|^2 + |Xa - Xb|^2)

                            Xrange = abs(rockX[i] - paperX[j])
                            Yrange = abs(rockY[i] - paperY[j])
                            sqrang = sqr(Xrange) + sqr(Yrange)
                            rang.append(math.sqrt(sqrang))

                        #movement

                        #X coordinate
                        if rockX[i] <= paperX[ind]:
                            #if i == 0:
                            #    print("+", rockX[i], scisorsX[ind])
                            rockX[i] -= speed

                        elif rockX[i] >= paperX[ind]:
                            #if i == 0:
                            #    print("-", rockX[i], scisorsX[ind])
                            rockX[i] += speed


                        #Y coordinate
                        if rockY[i] <= paperY[ind]:
                            rockY[i] -= speed

                        elif rockY[i] >= paperY[ind]:
                            rockY[i] += speed

                    except:
                        pass


            try:
                #collider
                rectr[i].right = rockX[i] + 43
                rectr[i].bottom = rockY[i] + 43
                pygame.draw.rect(screen, (0, 60, 100), rectr[i], 1, 2)

                #collision
                if pygame.Rect.colliderect(rectr[i], rects[ind]):
                    sPosX = scisorsX[ind]
                    sPosY = scisorsY[ind]
                    n_rock += 1
                    n_scisors -= 1
                    rockX.append(sPosX)
                    rockY.append(sPosY)
                    rectr.append(pygame.Rect(0, 0, 40, 40))
                    s_rock.append(pygame.image.load("sprites/rock.png"))
                    del scisorsY[ind]
                    del scisorsX[ind]
                    del s_scisors[ind]
                    temp = "Collision detect at:\n   coordinates: {}, {}\n   idex: {}, {}\n    n_rock: {}\n    n_scisors: {}"
                    pygame.mixer.Sound.play(scissors)
                    pygame.mixer.music.stop()
                    print(temp.format(scisorsX[ind], scisorsY[ind], ind, i, n_rock, n_scisors))

            except:
                pass

            if rockX[i] >= displayX - 10:
                rockX[i] -= 2

            elif rockX[i] <= 10:
                rockX[i] += 2

            if rockY[i] >= displayY - 10:
                rockY[i] -= 2

            elif rockY[i] <= 10:
                rockY[i] += 2

            sprite(rockX[i], rockY[i], s_rock[i])
            if debug:
                #print(rang)
                #print("going for:\n" + "scisors: " + str(ind) + " (index)\n" + "X of the scisors: " + str(scisorsX[ind]) + "        Y of the sciscors: " + str(scisorsY[ind]))
                #print("location: " + str(rockX[i]) + ", " + str(rockY[i]))
                #print(i)

                text = font.render(str(i), True, (0, 100, 0))
                # textRect = text.get_rect()
                # textRect.center = (400 // 2, 400 // 2)
                screen.blit(pygame.transform.scale(text, (40, 40)), (rockX[i], rockY[i]))

####################################################################################################################
        #PAPER
        for i in range(n_paper):
            rang = []
            try:
                #figuring out the closest scisors
                for j in range(n_rock):
                    Xrange = abs(paperX[i] - rockX[j])
                    Yrange = abs(paperY[i] - rockY[j])
                    sqrang = sqr(Xrange) + sqr(Yrange)
                    rang.append(math.sqrt(sqrang))



                ind = giofsnl(rang)

                #print(rang)
                #print(ind)
                if debug:
                    try:
                        pygame.draw.line(screen, (0, 20, 90), (paperX[i], paperY[i]), (rockX[ind], rockY[ind]), 3)
                    except:
                        pass

                try:
                    #movement

                    #X coordinate
                    if paperX[i] <= rockX[ind]:
                        #if i == 0:
                        #    print("+", rockX[i], scisorsX[ind])
                        paperX[i] += speed

                    elif paperX[i] >= rockX[ind]:
                        #if i == 0:
                        #    print("-", rockX[i], scisorsX[ind])
                        paperX[i] -= speed


                    #Y coordinate
                    if paperY[i] <= rockY[ind]:
                        paperY[i] += speed

                    elif paperY[i] >= rockY[ind]:
                        paperY[i] -= speed

                except:
                    try:
                        #figuring out the closest scisors
                        for j in range(n_rock):
                            Xrange = abs(paperX[i] - rockX[j])
                            Yrange = abs(paperY[i] - rockY[j])
                            sqrang = sqr(Xrange) + sqr(Yrange)
                            rang.append(math.sqrt(sqrang))

                        #movement

                        #X coordinate
                        if paperX[i] <= rockX[ind]:
                            #if i == 0:
                            #    print("+", rockX[i], scisorsX[ind])
                            paperX[i] += speed

                        elif paperX[i] >= rockX[ind]:
                            #if i == 0:
                            #    print("-", rockX[i], scisorsX[ind])
                            paperX[i] -= speed


                        #Y coordinate
                        if paperY[i] <= rockY[ind]:
                            paperY[i] += speed

                        elif paperY[i] >= rockY[ind]:
                            paperY[i] -= speed

                    except:
                        pass


            except:
                try:
                    #figuring out the closest scisors
                    for j in range(n_scisors):
                        Xrange = abs(paperX[i] - scisorsX[j])
                        Yrange = abs(paperY[i] - scisorsY[j])
                        sqrang = sqr(Xrange) + sqr(Yrange)
                        rang.append(math.sqrt(sqrang))

                except:
                    #winning condition is met, simulation is ended.
                    end = True
                    winner = "paper"

                ind = giofsnl(rang)

                #print(rang)
                #print(ind)
                if debug:
                    try:
                        pygame.draw.line(screen, (0, 20, 90), (paperX[i], paperY[i]), (scisorsX[ind], scisorsY[ind]), 3)
                    except:
                        pass

                try:
                    #movement

                    #X coordinate
                    if paperX[i] <= scisorsX[ind]:
                        #if i == 0:
                        #    print("+", rockX[i], scisorsX[ind])
                        paperX[i] -= speed

                    elif paperX[i] >= scisorsX[ind]:
                        #if i == 0:
                        #    print("-", rockX[i], scisorsX[ind])
                        paperX[i] += speed

                    elif paperX[i] == scisorsX[ind]:
                        pass


                    #Y coordinate
                    if paperY[i] <= scisorsY[ind]:
                        paperY[i] -= speed

                    elif paperY[i] >= scisorsY[ind]:
                        paperY[i] += speed

                    elif paperY[i] == scisorsY[ind]:
                        pass

                except:
                    try:
                        #figuring out the closest scisors
                        for j in range(n_scisors):
                            Xrange = abs(paperX[i] - scisorsX[j])
                            Yrange = abs(paperY[i] - scisorsY[j])
                            sqrang = sqr(Xrange) + sqr(Yrange)
                            rang.append(math.sqrt(sqrang))
                                            #movement

                        #X coordinate
                        if paperX[i] <= scisorsX[ind]:
                            #if i == 0:
                            #    print("+", rockX[i], scisorsX[ind])
                            paperX[i] -= speed

                        elif paperX[i] >= scisorsX[ind]:
                            #if i == 0:
                            #    print("-", rockX[i], scisorsX[ind])
                            paperX[i] += speed

                        elif paperX[i] == scisorsX[ind]:
                            pass


                        #Y coordinate
                        if paperY[i] <= scisorsY[ind]:
                            paperY[i] -= speed

                        elif paperY[i] >= scisorsY[ind]:
                            paperY[i] += speed

                        elif paperY[i] == scisorsY[ind]:
                            pass

                    except:
                        pass

            try:
                #collider
                rectp[i].right = paperX[i] + 43
                rectp[i].bottom = paperY[i] + 43
                pygame.draw.rect(screen, (0, 60, 100), rectp[i], 1, 2)

                #collision
                if pygame.Rect.colliderect(rectp[i], rectr[ind]):
                    rPosX = rockX[ind]
                    rPosY = rockY[ind]
                    n_paper += 1
                    n_rock -= 1
                    paperX.append(rPosX)
                    paperY.append(rPosY)
                    s_paper.append(pygame.image.load("sprites/paper.png"))
                    rectp.append(pygame.Rect(0, 0, 40, 40))
                    del rockY[ind]
                    del rockX[ind]
                    del s_rock[ind]
                    temp = "Collision detect at:\n   coordinates: {}, {}\n   idex: {}, {}\n    n_paper: {}\n    n_rock: {}"
                    pygame.mixer.Sound.play(scissors)
                    pygame.mixer.music.stop()
                    print(temp.format(rockX[ind], rockY[ind], ind, i, n_paper, n_rock))

            except:
                pass

            if paperX[i] >= displayX - 10:
                paperX[i] -= 2

            elif paperX[i] <= 10:
                paperX[i] += 2

            if paperY[i] >= displayY - 10:
                paperY[i] -= 2

            elif paperY[i] <= 10:
                paperY[i] += 2

            sprite(paperX[i], paperY[i], s_paper[i])

####################################################################################################################
        #SCISORS
        for i in range(n_scisors):
            rang = []
            try:

                #figuring out the closest scisors
                for j in range(n_paper):
                    Xrange = abs(scisorsX[i] - paperX[j])
                    Yrange = abs(scisorsY[i] - paperY[j])
                    sqrang = sqr(Xrange) + sqr(Yrange)
                    rang.append(math.sqrt(sqrang))


                ind = giofsnl(rang)

                #print(rang)
                #print(ind)
                if debug:
                    try:
                        pygame.draw.line(screen, (0, 90, 0), (scisorsX[i], scisorsY[i]), (paperX[ind], paperY[ind]), 3)
                    except:
                        pass

                try:
                    #movement

                    #X coordinate
                    if scisorsX[i] <= paperX[ind]:
                        #if i == 0:
                        #    print("+", rockX[i], scisorsX[ind])
                        scisorsX[i] += speed

                    elif scisorsX[i] >= paperX[ind]:
                        #if i == 0:
                        #    print("-", rockX[i], scisorsX[ind])
                        scisorsX[i] -= speed

                    elif scisorsX[i] == paperX[ind]:
                        pass


                    #Y coordinate
                    if scisorsY[i] <= paperY[ind]:
                        scisorsY[i] += speed

                    elif scisorsY[i] >= paperY[ind]:
                        scisorsY[i] -= speed

                    elif scisorsY[i] == paperY[ind]:
                        pass

                except:
                    try:
                        #figuring out the closest scisors
                        for j in range(n_paper):
                            Xrange = abs(scisorsX[i] - paperX[j])
                            Yrange = abs(scisorsY[i] - paperY[j])
                            sqrang = sqr(Xrange) + sqr(Yrange)
                            rang.append(math.sqrt(sqrang))

                            #movement

                            #X coordinate
                            if scisorsX[i] <= paperX[ind]:
                                #if i == 0:
                                #    print("+", rockX[i], scisorsX[ind])
                                scisorsX[i] += speed

                            elif scisorsX[i] >= paperX[ind]:
                                #if i == 0:
                                #    print("-", rockX[i], scisorsX[ind])
                                scisorsX[i] -= speed

                            elif scisorsX[i] == paperX[ind]:
                                pass


                            #Y coordinate
                            if scisorsY[i] <= paperY[ind]:
                                scisorsY[i] += speed

                            elif scisorsY[i] >= paperY[ind]:
                                scisorsY[i] -= speed

                            elif scisorsY[i] == paperY[ind]:
                                pass
                    except:
                        pass


            except:
                try:
                    #figuring out the closest scisors
                    for j in range(n_rock):
                        Xrange = abs(scisorsX[i] - rockX[j])
                        Yrange = abs(scisorsY[i] - rockY[j])
                        sqrang = sqr(Xrange) + sqr(Yrange)
                        rang.append(math.sqrt(sqrang))

                except:
                    #winning condition is met, simulation is ended.
                    end = True
                    winner = "scisors"

                ind = giofsnl(rang)

                #print(rang)
                #print(ind)
                if debug:
                    try:
                        pygame.draw.line(screen, (0, 20, 90), (scisorsX[i], scisorsY[i]), (paperX[ind], paperY[ind]), 3)
                    except:
                        pass

                #movement
                try:
                #X coordinate
                    if scisorsX[i] <= rockX[ind]:
                        #if i == 0:
                        #    print("+", rockX[i], scisorsX[ind])
                        scisorsX[i] -= speed

                    elif scisorsX[i] >= rockX[ind]:
                        #if i == 0:
                        #    print("-", rockX[i], scisorsX[ind])
                        scisorsX[i] += speed

                    elif scisorsX[i] == rockX[ind]:
                        pass


                    #Y coordinate
                    if scisorsY[i] <= rockY[ind]:
                        scisorsY[i] -= speed

                    elif scisorsY[i] >= rockY[ind]:
                        scisorsY[i] += speed

                    elif scisorsY[i] == rockY[ind]:
                        pass

                except:
                    try:
                        #figuring out the closest scisors
                        for j in range(n_rock):
                            Xrange = abs(scisorsX[i] - rockX[j])
                            Yrange = abs(scisorsY[i] - rockY[j])
                            sqrang = sqr(Xrange) + sqr(Yrange)
                            rang.append(math.sqrt(sqrang))

                                        #X coordinate
                        if scisorsX[i] <= rockX[ind]:
                            #if i == 0:
                            #    print("+", rockX[i], scisorsX[ind])
                            scisorsX[i] -= speed

                        elif scisorsX[i] >= rockX[ind]:
                            #if i == 0:
                            #    print("-", rockX[i], scisorsX[ind])
                            scisorsX[i] += speed

                        elif scisorsX[i] == rockX[ind]:
                            pass


                        #Y coordinate
                        if scisorsY[i] <= rockY[ind]:
                            scisorsY[i] -= speed

                        elif scisorsY[i] >= rockY[ind]:
                            scisorsY[i] += speed

                        elif scisorsY[i] == rockY[ind]:
                            pass

                    except:
                        pass

            try:
                #collider:
                rects[i].right = scisorsX[i] + 43
                rects[i].bottom = scisorsY[i] + 43
                pygame.draw.rect(screen, (0, 60, 100), rects[i], 1, 2)

                #collisiion
                if pygame.Rect.colliderect(rects[i], rectp[ind]):
                    pPosX = paperX[ind]
                    pPosY = paperY[ind]
                    n_scisors += 1
                    n_paper -= 1
                    scisorsX.append(pPosX)
                    scisorsY.append(pPosY)
                    rects.append(pygame.Rect(0, 0, 40, 40))
                    s_scisors.append(pygame.image.load("sprites/scisors.png"))
                    del paperY[ind]
                    del paperX[ind]
                    del s_paper[ind]
                    temp = "Collision detect at:\n   coordinates: {}, {}\n   idex: {}, {}\n    n_scisors: {}\n    n_paper: {}"
                    pygame.mixer.Sound.play(scissors)
                    pygame.mixer.music.stop()
                    print(temp.format(paperX[ind], paperY[ind], ind, i, n_scisors, n_paper))

            except:
                pass

            if scisorsX[i] >= displayX - 10:
                scisorsX[i] -= 2

            elif scisorsX[i] <= 10:
                scisorsX[i] += 2


            if scisorsY[i] >= displayY - 10:
                scisorsY[i] -= 2

            elif scisorsY[i] <= 10:
                scisorsY[i] += 2

############# ROCK REFERENCE #####################

            # if rockX[i] >= displayX - 10:
            #     rockX[i] -= 2
            #
            # elif rockX[i] <= 10:
            #     rockX[i] += 2
            #
            # if rockY[i] >= displayY - 10:
            #     rockY[i] -= 2
            #
            # elif rockY[i] <= 10:
            #     rockY[i] += 2

            #making the sprite
            sprite(scisorsX[i], scisorsY[i], s_scisors[i])
            if debug:
                text = font.render(str(i), True, (0, 0, 0))
                # textRect = text.get_rect()
                # textRect.center = (400 // 2, 400 // 2)
                screen.blit(pygame.transform.scale(text, (40, 40)), (scisorsX[i], scisorsY[i]))
        if end:
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(winner + " won!", True, (0, 0, 0))
            # textRect = text.get_rect()
            # textRect.center = (400 // 2, 400 // 2)
            screen.blit(pygame.transform.scale(text, (400, 200)), (200, 200))
            print("..............! SIMULATION END !..............")


        pygame.display.update()

if __name__ == "__main__":
    main()
