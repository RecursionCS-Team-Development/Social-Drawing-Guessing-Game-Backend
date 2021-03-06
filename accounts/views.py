from django.contrib.auth import get_user_model
from rest_framework import viewsets
# from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.settings import api_settings
from accounts.serializers import UserSerializer, LoginSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.filter(is_active=True)
    serializer_class = UserSerializer

class UserProfileCreateView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated]

    def get(self, request, format=None):
        icon = request.user.icon.url if request.user.icon else 'No IMAGE'

        return Response(data= {
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
            'icon': icon,
            'profile': request.user.profile
        },
        status=status.HTTP_200_OK)


class LoginAPIView(TokenObtainPairView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        response.set_cookie(
            "refresh",
            serializer.validated_data["refresh"],
            max_age=60 * 60 * 24 * 30,
            httponly=True,
        )
        return response


class LogoutAPIView(APIView):

    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie("refresh")
        return response


class RefreshAPIView(APIView):

    def post(self, request, format=None):
        refresh = self.request.COOKIES.get('refresh')
        if refresh is not None:
            refresh = RefreshToken(refresh)

            data = {'access': str(refresh.access_token)}
            if api_settings.ROTATE_REFRESH_TOKENS:
                if api_settings.BLACKLIST_AFTER_ROTATION:
                    try:
                        # Attempt to blacklist the given refresh token
                        refresh.blacklist()
                    except AttributeError:
                        # If blacklist app not installed, `blacklist` method will
                        # not be present
                        pass

            refresh.set_jti()
            refresh.set_exp()
            # refresh.set_iat()

            data['refresh'] = str(refresh)

            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)