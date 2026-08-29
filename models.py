from django.db import models

class WebhookPayload(models.Model):
    endpoint_name = models.CharField(max_length=100)
    source_ip = models.GenericIPAddressField()
    headers_json = models.JSONField(default=dict)
    body_data = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.endpoint_name} from {self.source_ip}"
