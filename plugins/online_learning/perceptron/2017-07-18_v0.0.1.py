from hyperstream import Tool, StreamInstance
from random import choice
from numpy import array, dot, random

unit_step = lambda x: 0 if x < 0 else 1

training_data = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 1),
    (array([1,0,1]), 1),
    (array([1,1,1]), 1),
]

w = random.rand(3)
learning_rate = 0.2


def perceptron_update(x, w):
    x, expected = choice(training_data)
    result = dot(w,x)
    error = expected - unit_step(result)
    w = w + learning_rate * error * x
    y = unit_step(result)
    return w, y



class Perceptron(Tool):
    def __init__(self, weights, learning_rate):
        super(Perceptron, self).__init__(weights=weights, learning_rate=learning_rate)

    def _execute(self, sources, alignment_stream, interval):
        data = sources[0].window(interval, force_calculation=True)

        for timestamp, value in data:
            self.weights, y_est = perceptron_update(value, self.weights)
            yield StreamInstance(timestamp, y_est)
