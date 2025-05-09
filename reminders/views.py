from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from .models import Reminder

@csrf_exempt
def create_reminder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse incoming JSON
            message = data.get('message')
            remind_at = data.get('remind_at')
            reminder_type = data.get('reminder_type')

            if not message or not remind_at or not reminder_type:
                return JsonResponse({'error': 'Missing data'}, status=400)

            # Store the reminder in the database (for now, just returning the data back)
            reminder=Reminder.objects.create(
                message=message,
                remind_at=remind_at,
                reminder_type=reminder_type,
            )
            
            return JsonResponse({'success': 'Reminder created', 'reminder': {'message': reminder.message, 'remind_at': reminder.remind_at, 'reminder_type': reminder.reminder_type}}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


def home(request):
    return HttpResponse("Welcome to the Remind Me Later API!")