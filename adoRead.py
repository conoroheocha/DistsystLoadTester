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
                "ADO_email": "charles92@example.net",
                "Athlete_email": "qroach@example.com",
            },
        )
