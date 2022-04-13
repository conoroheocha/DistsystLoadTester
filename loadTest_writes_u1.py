from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.index()

    @task
    def index(self):
        # self.client.get("/")
        # self.client.get("/static/assets.js")
        # self.client.post(
        #     "/loginAthlete", json={"email": "qroach@example.com",
        #                            "password": "+E9v&+E9v&uGy6h"}
        # )

        self.client.post(
            "/writeAvailability", json={
                "email": "qroach@example.com",
                "availability": [
                    {
                        "datetime_start": 1650386248000,
                        "datetime_end": 1650397048000,
                        "lat": 53.3234,
                        "lng": 6.2653,
                    }
                ]
            }
        )

        # # fail with error 400 - invalid timestamp
        # self.client.post(
        #     "/writeAvailability", json={
        #         "email": "qroach@example.com",
        #         "availability": [
        #             {
        #                 "datetime_start": 1650386248000,
        #                 "datetime_end": 1650386248000,
        #                 "lat": 53.3234,
        #                 "lng": 6.2653,
        #             }
        #         ]
        #     }
        # )

        # # fail with error 400 - past cutoff
        # self.client.post(
        #     "/writeAvailability", json={
        #         "email": "qroach@example.com",
        #         "availability": [
        #             {
        #                 "datetime_start": 1649868595000,
        #                 "datetime_end": 1649875795000,
        #                 "lat": 53.3234,
        #                 "lng": 6.2653,
        #             }
        #         ]
        #     }
        # )

        # # fail with error 404 no such user
        # self.client.post(
        #     "/writeAvailability", json={
        #         "email": "qroach@com",
        #         "availability": [
        #             {
        #                 "datetime_start": 1649868595000,
        #                 "datetime_end": 1649875795000,
        #                 "lat": 53.3234,
        #                 "lng": 6.2653,
        #             }
        #         ]
        #     }
        # )

    # @task
    # def about(self):
    #     self.client.get("/about/")
