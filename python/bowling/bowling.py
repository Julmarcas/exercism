class BowlingGame:
    def __init__(self):
        self.frames = []
        self.current_frame = []
        self.score = 0

    def roll(self, pins: int):
        if not self.current_frame:
            self.current_frame.append(pins)
        

    def score(self):
        double = False
        score = 0
        for roll in rolls:
            if double:
                score += 2 * roll
                double = False
            else:
                score += roll
                if score

        return score
