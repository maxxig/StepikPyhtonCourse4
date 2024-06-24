from abc import ABC, abstractmethod
class Middle(ABC):
    @abstractmethod
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes                   # пользовательские оценки
        self.expert_votes = expert_votes               # оценки критиков
    @abstractmethod
    def get_correct_user_votes(self):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.user_votes if 10 < vote < 90]
    @abstractmethod
    def get_correct_expert_votes(self):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.expert_votes if 5 < vote < 95]
    @abstractmethod
    def get_average(self, users=True):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        pass
class Average(Middle):
    def __init__(self, user_votes, expert_votes):
        super().__init__(user_votes, expert_votes)               # оценки критиков
    def get_correct_user_votes(self):
        return super().get_correct_user_votes()
    def get_correct_expert_votes(self):
        return super().get_correct_expert_votes()

    def get_average(self, users=True):
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()

        return sum(votes) / len(votes)

class Median(Middle):
    def __init__(self, user_votes, expert_votes):
        super().__init__(user_votes, expert_votes)               # оценки критиков
    def get_correct_user_votes(self):
        return super().get_correct_user_votes()
    def get_correct_expert_votes(self):
        return super().get_correct_expert_votes()

    def get_average(self, users=True):
        """Возвращает медиану пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = sorted(self.get_correct_user_votes())
        else:
            votes = sorted(self.get_correct_expert_votes())

        return votes[len(votes) // 2]

class Harmonic(Middle):
    def __init__(self, user_votes, expert_votes):
        super().__init__(user_votes, expert_votes)               # оценки критиков
    def get_correct_user_votes(self):
        return super().get_correct_user_votes()
    def get_correct_expert_votes(self):
        return super().get_correct_expert_votes()

    def get_average(self, users=True):
        """Возвращает среднее гармоническое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()

        return len(votes) / sum(map(lambda vote: 1 / vote, votes))