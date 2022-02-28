from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    email = models.EmailField(unique = True)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"

class Form(models.Model):
    creator = models.ForeignKey(User, verbose_name=_("سازنده"),on_delete=models.CASCADE)
    title = models.CharField(_("عنوان فرم"), max_length=50)
    description = models.CharField(max_length=10000, blank = True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    questions = models.ManyToManyField("Question", verbose_name=_("سوالات"),related_name='questions',blank=True)
    def __str__(self):
        return str(self.pk)

class Question(models.Model):
    QTYPE ={
            (0, 'کوتاه'),
            (1, 'پاراگراف'),
            (2,'انتخابی'),
            (3, 'چندگزینه ای'),
    }
    title = models.TextField(_("عنوان سوال"))
    q_type = models.IntegerField(_("نوع سوال"),choices=QTYPE, default=0)
    required = models.BooleanField(_("ضرورت پاسخ"),default= False)
    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey("Question", verbose_name=_("سوال مربوطه"), on_delete=models.CASCADE ,default='')
    text = models.CharField(max_length=5000)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Answer(models.Model):
    answer = models.CharField(_("متن جواب"), max_length=5000)
    answer_to = models.ForeignKey("Question", verbose_name=_("جواب به"), on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

class Response(models.Model):
    responder = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "responder")
    response_to = models.ForeignKey(Form, on_delete = models.CASCADE, related_name = "response_to")
    response = models.ManyToManyField(Answer, related_name = "response")