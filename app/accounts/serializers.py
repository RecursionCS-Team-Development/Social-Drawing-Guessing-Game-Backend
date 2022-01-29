from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'profile', 'icon', 'is_staff')


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):

        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        # if(self.user is None or not self.user.is_active):
        #     raise EmailNotRegistered

        # if not api_settings.USER_AUTHENTICATION_RULE(self.user):
        #     raise PasswordNotCorrect

        refresh = self.get_token(self.user)
        data = {
            'refresh': str(refresh),
            'access_token':  str(refresh.access_token),
            'email': self.user.email,
            'username': self.user.username,
            'profile': self.user.profile,
        }

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class TokenRefreshSerializer(serializers.Serializer):

    def validate(self, attrs):
        refresh = self.request.COOKIES.get('refresh')
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

        return data