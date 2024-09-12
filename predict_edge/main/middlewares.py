from django.middleware.csrf import get_token

#This middleware creates a sessionID and csrftoken for any user that is not logged in
class AnonymousSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.session.session_key:
            request.session.save()

        return self.get_response(request)
