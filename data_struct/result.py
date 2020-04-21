import json


class Result:

    def __init__(self):
        self.title = "no title"
        self.popultion = 0
        self.subpopulation = 0
        self.number_of_rect = 0
        self.scores = list()
        self.iters = list()
        self.finalScore = 0
        self.finalIter = 0

    def save(self, folder_name):
        file_name = folder_name + "/result_" + self.title + ".json"
        with open(file_name, "w") as file:
            json.dump(self.__dict__, file)

    def add_point(self, score, iter):
        if len(self.scores) > 0 and len(self.iters) > 0:
            last_scores = self.scores[-1]
            if last_scores == score:
                return
            self.scores.append(last_scores)
            self.iters.append(iter-1)

        self.iters.append(iter)
        self.scores.append(score)
