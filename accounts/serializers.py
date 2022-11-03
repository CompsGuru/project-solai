from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.tasks import LongTasks
from clock import scheduler


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'usage', 'role']
        extra_kwargs = {'password': {'write_only': True},
                        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        usage = validated_data['usage']
        role = validated_data['role']
        user = User(email=email, username=username, usage=usage, role=role)
        user.set_password(password)
        # user.save()
        mail_subject = "Solai Account Activation"
        template = 'accounts/account_activation_email.html'
        scheduler.add_job(LongTasks.send_email, args=[
                          self.context["request"], user, mail_subject, template])
        return user
