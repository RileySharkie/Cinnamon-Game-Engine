

class Camera:

    # while pause is false the camera doesnt follow its object of focus
    pause = False
    location = 0, 0
    follow_speed = 10

    # the camera width and height
    width = 800
    height = 640
    # the threshold in which the camera begins to move. if the focus is beyond the thresholds, the camera moves
    xfollow = width / 2.5
    yfollow = height / 5
    # the threshold in which the camera completely locks onto the focus
    xlock = xfollow / 2
    ylock = yfollow / 2

    def __init__(self, width, height, focus=None):
        # the camera will never go farther than these bounds
        self.xbound = width
        self.ybound = height
        # the focus is what the camera follows
        self.focus = focus

    def follow(self):
        if self.focus is not None:
            focusx, focusy = self.focus.location
            camerax, cameray = self.location
            if focusx < camerax + self.xfollow:
                if focusx < camerax + self.xlock:
                    camerax = camerax - (camerax + self.xlock - focusx) - self.follow_speed
                else:
                    camerax -= self.follow_speed
            elif focusx > camerax + self.width - self.xfollow:
                if focusx > camerax + self.width - self.xlock:
                    camerax = focusx - self.width + self.xlock + self.follow_speed
                else:
                    camerax += self.follow_speed
            if focusy < cameray + self.yfollow:
                if focusy < cameray + self.ylock:
                    cameray = cameray - (cameray + self.ylock - focusy) - self.follow_speed
                else:
                    cameray += self.follow_speed
            elif focusy > cameray + self.height - self.yfollow:
                if focusy > cameray + self.height - self.ylock:
                    cameray = focusy - self.height + self.ylock + self.follow_speed
                else:
                    cameray -= self.follow_speed
            if camerax > self.xbound-self.width:
                camerax = self.xbound - self.width
            elif camerax < 0:
                camerax = 0
            if cameray > self.ybound-self.height:
                cameray = self.ybound - self.height
            elif cameray < 0:
                cameray = 0

            self.location = camerax, cameray
