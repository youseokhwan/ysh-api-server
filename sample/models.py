from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Avatar of {self.user.name}"


# [ Fields ]
# BooleanField: 논리값 | IntegerField: 정수 | CharField: 문자열
# DateTimeField: 날짜+시간 | DateField: 날짜 | TimeField: 시간
# DecimalField: 소수점 | TextField: 긴 문자열 | FileField: 파일
# ForeignKey: 1:N

# [ Parameters ]
# 공통: unique, blank, default
# CharField에서 max_length 필수
# DateField에서 auto_now는 객체 저장될 때마다 현재 시각 적용, auto_now_add는 생성될 때만 현재 시각 적용

