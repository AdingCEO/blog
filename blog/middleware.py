from django.urls import reverse
from django.shortcuts import redirect

class ProfileSetupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        
    def __call__(self, request):
        if (
            request.user.is_authenticated and
            request.path_info != reverse('set_profile')
        ):
            try:
                request.user.profile.address
            except:
                return redirect('set_profile')
        
        
        response = self.get_response(request)
        return response