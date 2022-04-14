from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.index()

    @task
    def index(self):
        self.client.post(
            "/loginAthlete", json={
                                "email": "andersonsarah@example.net",
                                "password": "$1u^gGgE2e"
                            })
    @task
    def login(self):
        self.client.post(
            "/loginAdo", json={"email": "smithvincent@example.org", "password": "^@P4x9LjNO"}
        )

    # @task
    # def about(self):
    #     self.client.get("/about/")
