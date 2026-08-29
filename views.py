from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WebhookPayload
import json

def dashboard(request):
    logs = WebhookPayload.objects.order_by('-received_at')[:20]
    return render(request, 'relay/dashboard.html', {'logs': logs})

@csrf_exempt
def ingest_webhook(request, endpoint):
    if request.method == 'POST':
        ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
        headers = {k: v for k, v in request.META.items() if k.startswith('HTTP_')}
        body = request.body.decode('utf-8', errors='ignore')
        
        WebhookPayload.objects.create(
            endpoint_name=endpoint,
            source_ip=ip,
            headers_json=headers,
            body_data=body
        )
        return JsonResponse({"status": "received", "endpoint": endpoint})
    return JsonResponse({"error": "POST method required"}, status=405)
