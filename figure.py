import pygame
import random
import keyboard

class StickFigure:
    def __init__(self, hip=(250, 250), shoulder=(250, 150), width=500, height=500):

        pygame.init()
        self.display = pygame.display.set_mode((width, height))
        self.width = 500
        self.height = 500
        self.color = 200, 0, 255
        self.over = False

        self.shoulder = shoulder
        self.hip = hip

        # joint angle parameters
        self.left_elbow_pos = shoulder[1]
        self.right_elbow_pos = shoulder[1]
        self.left_hand_pos = 30
        self.right_hand_pos = 30
        self.right_knee_pos = 1.25
        self.left_knee_pos = 1.25
        self.right_foot_pos = 25
        self.left_foot_pos = 25


    def update_joints(self):
        """
        Update joint angles with new parameter values.
        """

        self.primary_joints = {
                'hip': self.hip,
                'shoulder': self.shoulder,
                'right_elbow': (self.shoulder[0] + 85, self.right_elbow_pos),
                'left_elbow': (self.shoulder[0] - 85, self.left_elbow_pos),
                'right_knee': (self.hip[0] * 1.25, self.hip[1] * self.right_knee_pos),
                'left_knee': (self.hip[0] * 0.75, self.hip[1] * self.left_knee_pos),
        }


        self.secondary_joints = {
                'right_hand': (self.primary_joints['right_elbow'][0] + 20, self.primary_joints['right_elbow'][1] + self.right_hand_pos),
                'left_hand': (self.primary_joints['left_elbow'][0] - 20, self.primary_joints['left_elbow'][1] + self.left_hand_pos),
                'right_foot': (self.primary_joints['right_knee'][0] + 10, self.primary_joints['right_knee'][1] + self.right_foot_pos),
                'left_foot': (self.primary_joints['left_knee'][0] - 10, self.primary_joints['left_knee'][1] + self.left_foot_pos),
        }


    def _draw_figure(self):
        """
        Checks for joint position updates and draws figure.
        """

        self.update_joints()

        draw = lambda x, y: pygame.draw.line(self.display, self.color, x, y)

        # body
        draw(self.primary_joints['shoulder'], self.primary_joints['hip'])

        # arms
        draw(self.primary_joints['shoulder'], self.primary_joints['right_elbow'])
        draw(self.primary_joints['shoulder'], self.primary_joints['left_elbow'])

        # hands
        draw(self.primary_joints['right_elbow'], self.secondary_joints['right_hand'])
        draw(self.primary_joints['left_elbow'], self.secondary_joints['left_hand'])

        # legs
        draw(self.primary_joints['hip'], self.primary_joints['right_knee'])
        draw(self.primary_joints['hip'], self.primary_joints['left_knee'])

        # feet
        draw(self.primary_joints['right_knee'], self.secondary_joints['right_foot'])
        draw(self.primary_joints['left_knee'], self.secondary_joints['left_foot'])


    def _dance(self, feet=False, right_elbow=False, left_elbow=False):
        """
        Changes coordinates of limbs.
        """
        
        ru = random.uniform



        if feet:
            self.right_knee_pos = ru(1.1, 1.4)
            self.left_knee_pos = ru(1.1, 1.4)
            self.left_foot_pos = ru(10, 45)
            self.right_foot_pos = ru(10, 45)
        elif right_elbow:
            self.right_elbow_pos = ru(25, 175)
        elif left_elbow:
            self.left_elbow_pos = ru(25, 175)
        else:
            self.left_elbow_pos = ru(75, 175)  
            self.right_elbow_pos = ru(75, 175)
            self.left_hand_pos = ru(10, 50)
            self.right_hand_pos = ru(10, 50)

    def show(self):
        """
        Renders figure and waits for inputs.
        """

        while not self.over:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.over = True
            
            keyboard.on_press_key('h', lambda _: self._dance(), suppress=True)
            keyboard.on_press_key('f', lambda _: self._dance(feet=True), suppress=True)
            keyboard.on_press_key('y', lambda _: self._dance(right_elbow=True), suppress=True)
            keyboard.on_press_key('n', lambda _: self._dance(left_elbow=True), suppress=True)

            self.display.fill((0, 0, 0))
            self._draw_figure()

            pygame.display.update()

if __name__ == '__main__':
    sf = StickFigure()
    sf.show()

