# locustfile.py
import base64

from locust import HttpUser, task, between
import json


def openJSONFile():
	with open("test.json", "r", encoding="utf-8") as f:
		byte = bytearray(f.read(), "utf-8")

		return str(base64.b64encode(byte), "utf-8")


class WebsiteTestUser(HttpUser):
	wait_time = between(1, 2.5)

	@task
	def my_task(self):
		data = {
			"textbook": "국어",
			"grade": "1",
			"semester": 1,
			"chapter_number": 1,
			"chapter": "문법",
			"file": openJSONFile(),
		}
		self.client.post("/api/review-note/", json=data)
