class Character:

    def __init__(self,
                 fall_speed, max_fall_speed,
                 ground_accel, ground_max_speed,
                 air_accel, air_max_speed):
        self.fall_speed = fall_speed  # units per second of downwards acceleration
        self.max_fall_speed = max_fall_speed

        self.ground_accel = ground_accel  # units per second of grounded sideways acceleration
        self.ground_max_speed = ground_max_speed

        self.air_accel = air_accel  # units per second of aerial sideways acceleration
        self.air_max_speed = air_max_speed


test_char = Character(
    10, 20,
    15, 20,
    15, 20
)
