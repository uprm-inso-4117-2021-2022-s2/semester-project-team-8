import time
from locust import HttpUser, between, task


class LocustTesting(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_users_test(self):
        self.client.get(url="/user")

    @task
    def get_field_test(self):
        self.client.get(url="/field")
