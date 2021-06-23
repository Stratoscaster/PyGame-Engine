import pygame
from tools.command import *
import tools.constants as c

class EventHandler():
    def __init__(self):
        # Keyboard Command
        self.up_arrow_cmd = Command(c.UP_ARROW)
        self.down_arrow_cmd = Command(c.DOWN_ARROW)
        self.left_arrow_cmd = Command(c.LEFT_ARROW)
        self.right_arrow_cmd = Command(c.RIGHT_ARROW)

        self.up_arrow_release_cmd = Command(c.UP_ARROW_RELEASE)
        self.down_arrow_release_cmd = Command(c.DOWN_ARROW_RELEASE)
        self.left_arrow_release_cmd = Command(c.LEFT_ARROW_RELEASE)
        self.right_arrow_release_cmd = Command(c.RIGHT_ARROW_RELEASE)

        # Controller Command
        self.a_btn_cmd = Command(c.A_BTN)
        self.b_btn_cmd = Command(c.B_BTN)
        self.x_btn_cmd = Command(c.X_BTN)
        self.y_btn_cmd = Command(c.Y_BTN)
        self.start_btn_cmd = Command(c.START_BTN)
        self.select_btn_cmd = Command(c.SELECT_BTN)

        self.previous_pressed_keys_state = None


    def handle_events(self, actor):
        for event in pygame.event.get():
            self.handle_quit_events(event)
            self.handle_keyboard_events(event, actor)
            self.handle_joystick_events(event, actor)

    def handle_quit_events(self, event):
        if event.type == pygame.QUIT:
            self.quit_game()

    def handle_keyboard_events(self, event, actor):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:  # Up
            self.up_arrow_cmd.execute(actor)
        if pressed_keys[pygame.K_s]: # Down
            self.down_arrow_cmd.execute(actor)
        if pressed_keys[pygame.K_a]: # Left
            self.left_arrow_cmd.execute(actor)
        elif pressed_keys[pygame.K_d]: # Right
            self.right_arrow_cmd.execute(actor)

        # Handle Key Releases
        if self.previous_pressed_keys_state is not None:
            if not pressed_keys[pygame.K_w] and self.previous_pressed_keys_state[pygame.K_w]:  # Up released
                self.up_arrow_release_cmd.execute(actor)
            if not pressed_keys[pygame.K_s] and self.previous_pressed_keys_state[pygame.K_s]: # Down released
                self.down_arrow_release_cmd.execute(actor)
            if not pressed_keys[pygame.K_a] and self.previous_pressed_keys_state[pygame.K_a]: # Left released
                self.left_arrow_release_cmd.execute(actor)
            elif not pressed_keys[pygame.K_d] and self.previous_pressed_keys_state[pygame.K_d]: # Right released
                self.right_arrow_release_cmd.execute(actor)

        # if pressed_keys[pygame.K_b]: # B button
        #     self.a_btn_cmd.execute(actor)




        self.previous_pressed_keys_state = pressed_keys

        # ---- Previous key handling method ----
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w: # Up
        #         self.up_arrow_cmd.execute(actor)
        #     elif event.key == pygame.K_s: # Down
        #         self.down_arrow_cmd.execute(actor)
        #     elif event.key == pygame.K_a: # Left
        #         self.left_arrow_cmd.execute(actor)
        #     elif event.key == pygame.K_d: # Right
        #         self.right_arrow_cmd.execute(actor)
        #     if event.key == pygame.K_b:
        #         self.a_btn_cmd.execute(actor)
    def handle_joystick_events(self, event, actor):
        pass


    @staticmethod

    def quit_game():
        pygame.quit()
        quit()