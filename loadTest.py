from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.index()

    @task
    def index(self):
        self.client.post(
            "/loginAthlete", json={
                                "email": "qroach@example.com",
                                "password": "+E9v&uGy6h"
                            })

    # @task
    # def about(self):
    #     self.client.get("/about/")
