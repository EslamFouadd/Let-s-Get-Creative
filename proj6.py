#Evaluating a Polynomial at Multiple Points

def factorize(self, points  = None):
    if points is None:
        points = self.points
    else:
        self.points = points
    if len(self.points) == 0:
        raise ValueError("No points to factorize")
    if len(self.points) == 1:
        return self.points[0]
    factors = []
    for i in range(len(self.points)):
        for j in range(i+1, len(self.points)):
            if self.points[i] % self.points[j] == 0:
                factors.append(self.points[i] // self.points[j])
                self.points.remove(self.points[j])
                break
    if len(self.points) == 1:
        return self.points[0]
    else:
        return factors