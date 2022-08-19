import numpy as np


class Sigmoid:
    def __init__(self):
        self.params, self.grads = [], []
        self.out = None

    def forward(self, x):
        out = 1/(1+np.exp(-x))
        self.out = out
        return out

    def backward(self, dout):
        dx = dout*(1.0-self.out)*self.out
        return dx


class Affine:
    def __init__(self, w, b):
        self.params = [w, b]
        self.grads = [np.zeros_like(w), np.zeros_like(b)]
        self.x = None

    def forward(self, x):
        w, b = self.params
        out = np.dot(x, w) + b
        self.x = x
        return out

    def backward(self, dout):
        w, b = self.params
        dx = np.dot(dout, w.T)
        dw = np.dot(self.x.T, dout)
        db = np.sum(dout, axis=0)
        self.grads[0][...] = dw
        self.grads[1][...] = db
        return dx


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size):
        I, H, O = input_size, hidden_size, output_size
        w1 = np.random.randn(I, H)
        b1 = np.random.randn(H)
        w2 = np.random.randn(H, O)
        b2 = np.random.randn(O)
        self.layers = [Affine(w1, b1), Sigmoid(), Affine(w2, b2)]
        self.params = []
        for layer in self.layers:
            self.params += layer.params

    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x


class MatMul:
    def __init__(self, w):
        self.params = [w]
        self.grads = [np.zeros_like(w)]
        self.x = None

    def forward(self, x):
        w, = self.params
        out = np.dot(x, w)
        self.x = x
        return out

    def backward(self, dout):
        w, = self.params
        dx = np.dot(dout, w.T)
        dw = np.dot(self.x.T, dout)
        self.grads[0][...] = dw
        return dx


class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        for i in range(len(params)):
            params[i] -= self.lr*grads[i]


x = np.random.randn(10, 2)
optimizer = SGD()
model = TwoLayerNet(2, 4, 3)
s = model.predict(x)
# print(s)
