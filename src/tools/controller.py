import pygame
from tools import constants as c
from tools.event_handler import EventHandler
import time
class Controller:
    def __init__(self, display, clock, game_states, starting_state):
        self.display = display
        self.clock = clock
        self.game_states = game_states
        self.current_state = self.game_states[starting_state]()
        self.event_handler = EventHandler()
        self.running = True
        self.dt = 60

    def run_game(self):
        # Framerate independence - last frame time
        last_time = time.time()
        while self.running:
            self.dt = time.time() - last_time
            self.dt *= c.FPS # for 60 fps
            # print(str(self.dt)[:5])
            # if we are running below 60 fps, it will compensate for the low framerate and keep movement correct
            last_time = time.time()

            # Tick the Clock
            self.update_clock()

            # Handle all Events, pass through dt for frame-independent physics
            self.update_events()

            # Update Current Game State
                # Also, Check if current game state is finished, if so transition to next game state
            self.update_game_state()

            # Render Display
            self.update_display()

            # Update Environment Changes
            self.update_environment_changes()
        self.quit_game()

    def update_clock(self):
        self.clock.tick(c.FPS)

    def update_events(self):
        self.current_state.physics.update_dt_frame_scaling(self.dt)
        self.current_state.actor.update_dt_frame_scaling(self.dt)
        self.event_handler.handle_events(self.current_state.actor, self.current_state)

    def update_game_state(self):
        if self.current_state.is_done:
            previous_state = self.current_state
            self.current_state = self.game_states[self.previous_state.next_state]()
            previous_state.cleanup()
        self.current_state.update()

    def update_display(self):
        self.current_state.draw(self.display)

    def update_environment_changes(self):
        '''
        Checks to see if anything has changed during the main game loop such as:
        * Resolution change
        * Joystick configuration change
        * Keyboard configuration change
        * Audio driver change
        '''
        pass



    @staticmethod
    def quit_game():
        pygame.quit()
        quit()
