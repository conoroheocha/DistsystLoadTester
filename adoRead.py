from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(0, 15)

    def on_start(self):
        self.getTimes()

    @task
    def getTimes(self):
        self.client.get(
            "/read",
            json={
                "ADO_email": "smithvincent@example.org",
                "Athlete_email": "andersonsarah@example.net",
            },
        )
