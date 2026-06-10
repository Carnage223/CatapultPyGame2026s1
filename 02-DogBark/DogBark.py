import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # TODO 1: Create an image with the 2dogs.JPG image
    dog_image = pygame.image.load("2dogs.JPG")
    # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    dog_image = pygame.transform.scale(dog_image, (IMAGE_SIZE, IMAGE_SIZE))
    # Prepare the text caption(s)
    # TODO 4: Create a font object with a size 28 font.
    font_object_1 = pygame.font.SysFont("comicsans", 28)
    fonts = pygame.font.get_fonts()
    for font in sorted(fonts):
        print(font)

    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption_1 = font_object_1.render("Two Dogs", True, BLACK)
    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("bark.wav")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(dog_image, (0, 0))
        # Draw the text onto the screen
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        screen.blit(caption_1, (screen.get_width() // 2 - caption_1.get_width() // 2,
                                screen.get_height() - caption_1.get_height()))

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.
        font_object_2 = pygame.font.SysFont("comicsans", 40)
        caption_2 = font_object_2.render("You stink...", True, WHITE)
        screen.blit(caption_2, (screen.get_width() // 2 - caption_2.get_width() // 2, 20))
        # Update the screen
        pygame.display.update()


main()
