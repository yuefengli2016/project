from hyperstream import Tool, StreamInstance


def perceptron_update(x, w):
    y = 0
    return w, y



class Perceptron(Tool):
    def __init__(self, weights, learning_rate):
        super(Perceptron, self).__init__(weights=weights, learning_rate=learning_rate)

    def _execute(self, sources, alignment_stream, interval):
        data = sources[0].window(interval, force_calculation=True)

        for timestamp, value in data:
            self.weights, y_est = perceptron_update(value, self.weights)
            yield StreamInstance(timestamp, y_est)
