from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(0, 15)

    def on_start(self):
        self.login()
        self.getTimes()

    @task
    def login(self):
        self.client.post(
            "/loginAdo", json={"email": "qroach@example.com", "password": "+E9v&uGy6h"}
        )

    @task
    def getTimes(self):
        self.client.get(
            "/read",
            json={
                "ADO_email": "charles92@example.net",
                "Athlete_email": "qroach@example.com",
            },
        )
