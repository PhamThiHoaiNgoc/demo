from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()


def search_employees_api(request):
    """
    API endpoint to search employees by name and department
    Returns JSON response for AJAX requests
    """
    query = request.GET.get('q', '')
    department_id = request.GET.get('department', '')

    users = User.objects.all()
    if query:
        users = users.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    # Filter by department
    if department_id:
        users = users.filter(department_id=department_id)

    # Prepare data for JSON response
    results = []
    for user in users:
        results.append({
            'id': user.id,
            'username': user.username,
            'full_name': f"{user.first_name} {user.last_name}",
            'department': user.department.name if user.department else None,
            'role': user.get_role_display(),
            'avatar_url': user.avatar_url,
        })

    return JsonResponse({
        'results': results,
        'count': len(results)
    })
