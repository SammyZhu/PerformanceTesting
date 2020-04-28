from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

    def login(self):
        self.client.post("/appLogin.mvc",
                         {'code': 'eb70412cffa99093eb8d6b07000eb4e3', 'userName': "sammy.zhu", 'password': '1'})

    @task(2)
    def enquiry_lot(self):
        self.client.get("/qi-service/inspectionLot/8ad68aeb6f12bf06016f12ff8e5e165f")

    # @task(1)
    # def create_lot(self):
    #     self.client.post()


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
