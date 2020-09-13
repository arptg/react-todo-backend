import jwt
from django.conf import settings


def AddUserToRequest(get_response):

    def middleware(request):

        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            token = authorization_header.split(' ')[1]
            decoded_token = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user_id = decoded_token['user_id']
        except:
            request.user_id = None
        response = get_response(request)
        return response

    return middleware
