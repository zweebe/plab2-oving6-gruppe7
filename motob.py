from basic_robot.motors import Motors


class motob:


    def __init__(self):
        self.motor = Motors()
        self.value = []

    def update(self, motor_rec):
        self.value.append(motor_rec)

    def operationalize(self):
        turning = {}
        if self.value[0] == "B":
            if self.value[1] == 180:
                self.motor.backward(0.5, 1)
                self.motor.left(0.5, 1.5)

            elif self.value[1] == 90:
                self.motor.backward(0.5, 1)
                self.motor.left(0.5, 0.75)

            elif self.value[1] == 45:
                self.motor.backward(0.5, 1)
                self.motor.left(0.5, 0.375)

        elif self.value[0] == "L":
            if self.value[1] == 180:
                self.motor.left(0.5, 1.5)

            elif self.value[1] == 90:
                self.motor.left(0.5, 0.75)

            elif self.value[1] == 45:
                self.motor.left(0.5, 0.375)

        elif self.value[0] == "R":
            if self.value[1] == 180:
                self.motor.right(0.5, 1.5)

            elif self.value[1] == 90:
                self.motor.right(0.5, 90)

            elif self.value[1] == 45:
                self.motor.right(0.5, 0.375)

