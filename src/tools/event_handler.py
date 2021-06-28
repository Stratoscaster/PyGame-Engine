import pygame
from tools.command import *
import tools.constants as c
from game_states.game_state import GameState
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

        self.left_mouse_button_cmd = Command(c.LEFT_MOUSE_BTN)
        self.freeze_frame_command = Command(c.FREEZE_FRAME_KEY)
        # Controller Command
        self.a_btn_cmd = Command(c.A_BTN)
        self.b_btn_cmd = Command(c.B_BTN)
        self.x_btn_cmd = Command(c.X_BTN)
        self.y_btn_cmd = Command(c.Y_BTN)
        self.start_btn_cmd = Command(c.START_BTN)
        self.select_btn_cmd = Command(c.SELECT_BTN)

        self.previous_pressed_keys_state = None


    def handle_events(self, actor, state: GameState):
        for event in pygame.event.get():
            self.handle_quit_events(event)
            self.handle_keyboard_events(event, actor, state)
            self.handle_joystick_events(event, actor, state)

    def handle_quit_events(self, event):
        if event.type == pygame.QUIT:
            self.quit_game()

    def handle_keyboard_events(self, event, actor, state):
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

        mouse_btns = pygame.mouse.get_pressed()
        if mouse_btns[0]:
            self.left_mouse_button_cmd.execute(actor)


        if pressed_keys[pygame.K_BACKQUOTE]:
            self.freeze_frame_command.execute(state)


        # if pressed_keys[pygame.K_b]: # B button
        #     self.a_btn_cmd.execute(actor)

        # keep at bottom
        self.previous_pressed_keys_state = pressed_keys

    def handle_joystick_events(self, event, actor, state):
        pass


    @staticmethod
    def quit_game():
        pygame.quit()
        quit()