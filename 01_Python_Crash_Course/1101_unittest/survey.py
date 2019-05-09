class AnonymousSurvey():
    """收集匿名問卷"""
    def __init__(self, question):
        """儲存一個問題，並準備答案"""
        self.question = question
        self.respones = []

    def show_question(self):
        """顯示問卷的問題"""
        print(self.question)

    def store_respones(self, new_respones):
        self.respones.append(new_respones)

    def show_result(self):
        print("Survey result:")
        for respone in self.respones:
            print('-' + respone)

