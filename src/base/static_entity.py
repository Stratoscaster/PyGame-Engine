import pygame
import tools.constants as c
import tools.color_list as colors

# StaticEntity is a class that inherits Sprite
# StaticEntity would represent something that can only move, and nothing else. It would not have game-based mechanics such as health, etc
# StaticEntity cannot be controlled by the player
# StaticEntities do not have animations or states

class StaticEntity(pygame.sprite.Sprite):
    def __init__(self, image=pygame.Surface(c.MEDIUM_TILE_SIZE)):
        super(StaticEntity, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        # self.color = colors.YELLOW
        # self.image.fill(self.color)
        self.pos_x = 0.0
        self.pos_y = 0.0
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.acc_x = 0.0
        self.acc_y = 0.0
        self.gravity_acceleration = 0.0
        self.dt = 1
        self.target_vel_x = 0.0
        self.target_vel_y = 0.0
        self.target_vel_x_active = False
        self.target_vel_y_active = False
        self.stay_on_target_vel_x = False
        self.stay_on_target_vel_y = False
        self.collision_enabled = False

    def update(self):
        self.update_vel()
        self.update_pos()

    def update_vel(self):
        if not self.target_vel_x_active:
            self.vel_x = self.vel_x + (self.acc_x * self.dt)
        else:
            # for velocity targeting
            # if velocity not at target, increase until it is within acceleration of target, then set
            # if velocity over target, decrease vel until it is under target, then

            accel_dir = 1
            if self.target_vel_x > self.vel_x:
                accel_dir = 1
            elif self.target_vel_x < self.vel_x:
                accel_dir = -1
            else:
                accel_dir = 0

            accel_vector = self.acc_x * accel_dir
            # print('accel_vector=',str(accel_vector))

            if self.target_vel_x - self.vel_x <= accel_vector:
                self.vel_x = self.target_vel_x
            else:
                self.vel_x = self.vel_x + (self.acc_x * self.dt * accel_vector)

            if not self.stay_on_target_vel_x and (self.vel_x == self.target_vel_x):
                self.unset_target_vel_x()
                self.acc_x = 0.0


        if not self.target_vel_y_active:
            self.vel_y = self.vel_y + ((self.acc_y - (self.gravity_acceleration * -1)) * self.dt)
        else:
            accel_dir = 1
            if self.target_vel_y > self.vel_y:
                accel_dir = 1
            elif self.target_vel_y < self.vel_y:
                accel_dir = -1
            else:
                accel_dir = 0

            accel_vector = self.acc_y * accel_dir
            # print('accel_vector=', str(accel_vector))

            if self.target_vel_y - self.vel_y <= accel_vector:
                self.vel_y = self.target_vel_y
            else:
                self.vel_y = self.vel_y + (self.acc_y * self.dt * accel_vector)

        # print('Current Velocity Vector:', str((self.vel_x, self.vel_y)))



    def update_pos(self):

        self.pos_x += self.vel_x * self.dt
        self.pos_y += self.vel_y * self.dt
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

    #####################
    # Getters & Setters #
    #####################

    def set_pos(self, xy):
        self.pos_x = xy[0]
        self.pos_y = xy[1]

    def get_pos(self):
        return (self.pos_x, self.pos_y)

    def update_dt_frame_scaling(self, dt):
        self.dt = dt

    def set_vel_x(self, velocity):
        self.vel_x = velocity

    def set_vel_y(self, velocity):
        self.vel_y = velocity

    def get_velocity_vector(self):
        return (self.vel_x, self.vel_y)

    def set_acc_x(self, acceleration):
        self.acc_x = acceleration

    def set_acc_y(self, acceleration):
        self.acc_y = acceleration

    def set_target_vel_x(self, target_vel_x, acc_x=None, stay_on_target_vel_x=False):
        if acc_x is None:
            acc_x = self.acc_x
        self.target_vel_x = target_vel_x
        self.acc_x = abs(acc_x)
        self.target_vel_x_active = True
        self.stay_on_target_vel_x = stay_on_target_vel_x

    def set_target_vel_y(self, target_vel_y, acc_y=None, stay_on_target_vel_y=False):
        if acc_y is None:
            acc_y = self.acc_y
        self.target_vel_y = target_vel_y


        self.acc_y = abs(acc_y)
        self.target_vel_y_active = True
        self.stay_on_target_vel_y = stay_on_target_vel_y

    def unset_target_vel_x(self):
        self.target_vel_x_active = False
        self.stay_on_target_vel_x = False

    def unset_target_vel_y(self):
        self.target_vel_y_active = False
        self.stay_on_target_vel_y = False


    def unset_target_vel(self):
        self.unset_target_vel_x()
        self.unset_target_vel_y()

    def set_gravity(self, gravity_acceleration):
        self.gravity_acceleration = gravity_acceleration

    def impulse_y(self, impulse_acceleration, invert_axis=True):
        pass

    def set_collision(self, collision_enabled):
        self.collision_enabled = collision_enabled


