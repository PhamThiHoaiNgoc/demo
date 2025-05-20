from .models import UserNotification

def get_unread_count(user, notification_type=None):
    qs = UserNotification.objects.filter(user=user, is_read=False)
    if notification_type:
        qs = qs.filter(notification__type=notification_type)
    return qs.count()

def unread_notification_counts(request):
    if request.user.is_authenticated:
        return {
            'personal_unread_count': get_unread_count(request.user, 'personal'),
            'company_unread_count': get_unread_count(request.user, 'company')
        }
    return {}
