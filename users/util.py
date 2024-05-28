from datetime import datetime  # Importar funciones para cálculo del tiempo

from django.contrib.auth import logout


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            last_activity = request.session.get('last_activity', None)
            if last_activity:
                last_activity = datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
                if (datetime.now() - last_activity).seconds > 1600:  # 30 seconds = timeout duration
                    logout(request)
            request.session['last_activity'] = current_time
        response = self.get_response(request)
        return response
