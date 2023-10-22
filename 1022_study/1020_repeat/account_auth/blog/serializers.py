from rest_framework import serializers
from .models import Post
from rest_framework.authtoken.models import Token # token모델, Token.objects.get() 방식으로 토큰확인
from rest_framework.validators import UniqueValidator # 중복검사
from django.contrib.auth.password_validation import validate_password # 비밀번호 유효성 검사
from django.contrib.auth.models import User # User모델, 기본 User모델 사용 시 사용자명, 비밀번호, 이메일 필드만 사용 가능 -> 상속 받아 커스터마이징 가능
from django.contrib.auth import authenticate


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    ''' 회원가입 serializer'''

    # 사용자명 중복검사
    username = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    # 이메일 중복검사
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    # 비밀번호 유효성 검사(너무 짧은 비밀 번호 등)
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    # 비밀번호 확인 필드
    password2 = serializers.CharField(
        write_only = True,
        required = True
    )

    class Meta:
        model = User
        fields = '__all__' # ['필드명', '필드명', ...] 이제 허락 x

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': '비밀번호가 일치하지 않습니다.'})
        
    def create(self, validated_date):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        # 비밀번호 암호화
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.created(user=user) # 토큰생성
        # token = Token.objects.created(user=user)
        # print(token)
        return user


class LoginSerializer(serializers.ModelSerializer):
    '''로그인 시리얼라이저'''

    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True) # write_only=True: password 필드는 읽기 전용으로 설정

    class Meta:
        model = User
        fields = ['username', 'password'] # 로그인시 아이디, 비밀번호 필요

    def validate(self, data):
        print(data)
        user = authenticate(**data)
        print(user)
        print(dir(user))
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError("유효하지 않은 로그인입니다.")