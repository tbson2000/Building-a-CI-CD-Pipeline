import json
from locust import HttpUser, task, between


class LocustStressTest(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def test1(self):
        self.client.get("http://localhost:80")

    @task(2)
    def test2(self):
        data = json.loads(
            """{
  "CHAS": {
    "0": 0
  },
  "RM": {
    "0": 6.575
  },
  "TAX": {
    "0": 296.0
  },
  "PTRATIO": {
    "0": 15.3
  },
  "B": {
    "0": 396.9
  },
  "LSTAT": {
    "0": 4.98
  }
}"""
        )
        self.client.post("http://localhost:80/predict", json=data)