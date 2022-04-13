from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.client.post(
            "/loginAthlete", {"email": "qroach@example.com", "password": "+E9v&ussGy6h"}
        )

    # @task
    # def index(self):
    #     self.client.get("/")
    #     self.client.get("/static/assets.js")

    # @task
    # def about(self):
    #     self.client.get("/about/")
