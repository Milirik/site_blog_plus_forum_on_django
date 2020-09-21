from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from django.views.generic import View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView

from django.shortcuts import get_object_or_404

from django.core.signing import BadSignature

from .models import *
from .forms import *
from .utilities import signer

from datetime import datetime


def check_for_constraint(request):
	if request.user.is_authenticated:
		s = request.user.discussion_set.filter(date_of_creation__date=datetime.now().date()).count()	
		d = request.user.subanswer_set.filter(date_of_creation__date=datetime.now().date()).count()
		b = request.user.answer_set.filter(date_of_creation__date=datetime.now().date()).count()
		return CaptchaForm() if d + s + b >= 5 else None
	else:
		return None

# Pages
def index(request):
	categories = Category.objects.all()
	return render(request, 'forum/index.html', 
		context={
		'categories':categories,
		})


# Discussions
def detail(request, pk): # Also for new answers
	discuss = get_object_or_404(Discussion, pk=pk)

	if request.method == "POST": 
		if check_for_constraint(request):
			captcha_form = CaptchaForm(request.POST)

			if captcha_form.is_valid():
				if request.POST.get("form_") == "subanswer":
					sub_answer_form = SubAnswerForm(request.POST)
					if sub_answer_form.is_valid():
						tmp = sub_answer_form.save()
						messages.add_message(request, messages.SUCCESS, 'Ответ создан')
				elif request.POST.get("form_") == "answer":
					form = AnswerForm(request.POST)
					if form.is_valid():
						tmp = form.save()
						messages.add_message(request, messages.SUCCESS, 'Комментарий создан')
						
			else:
				messages.add_message(request, messages.ERROR, 'Вы не правильно ввели код')
		else:
			if request.POST.get("form_") == "subanswer":
				sub_answer_form = SubAnswerForm(request.POST)
				if sub_answer_form.is_valid():
					tmp = sub_answer_form.save()
					messages.add_message(request, messages.SUCCESS, 'Ответ создан')
			elif request.POST.get("form_") == "answer":
				form = AnswerForm(request.POST)
				if form.is_valid():
					tmp = form.save()
					messages.add_message(request, messages.SUCCESS, 'Комментарий создан')

	captcha_form = check_for_constraint(request)
	form = AnswerForm(initial={'creator':request.user.pk, 'discussion': discuss.pk})
	sub_answer_form = SubAnswerForm(initial={'creator': request.user.pk})
	context = {
		'discuss': discuss,
		'form': form,
		'sub_answer_form': sub_answer_form,
		'captcha_form': captcha_form,
		}

	return render(request, 'forum/detail.html', context)
@login_required
def profile_add_discuss(request):
	captcha_form = check_for_constraint(request)

	if request.method=="POST":
		form = DiscussForm(request.POST)
		if form.is_valid():
			discuss = form.save()
			messages.add_message(request, messages.SUCCESS, 'Обсуждение успешно создано')
			return redirect('forum:index_name')
	else:
		form = DiscussForm(initial={'creator':request.user.pk})
	context = {
	'form': form,
	'captcha_form': captcha_form,
	}
	return render(request, 'forum/profile_discuss_add.html', context)


@login_required
def profile_delete_discuss(request, pk):
	discuss = get_object_or_404(Discussion, pk=pk)
	if request.method=="POST":
		discuss.delete()
		messages.add_message(request, messages.SUCCESS, 'Объявление удалено')
		return redirect('forum:profile_name')
	else:
		context = {'discuss': discuss}
		return render(request, 'forum/profile_delete_discuss.html', context)

# User
class ForumLoginView(LoginView):
	template_name = 'forum/login.html'


class ForumLogoutView(LoginRequiredMixin, LogoutView):
	template_name = 'forum/logout.html'


class RegisterUserView(CreateView):
	model = AdvUser
	template_name = 'forum/register_user.html'
	form_class = RegisterUserForm
	success_url = reverse_lazy('forum:register_done_name')


class RegisterUserDoneView(TemplateView):
	template_name = 'forum/register_done.html'


class ForumPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
	template_name = 'forum/password_change.html'
	success_url = reverse_lazy('forum:profile_name')
	success_message = 'Пароль пользователя изменен'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = AdvUser
	template_name = 'forum/change_user_info.html'
	form_class = ChangeUserInfoForm
	success_url = reverse_lazy('forum:profile_name')
	success_message = 'Личные данные пользователя изменены'

	def dispatch(self, request, *args, **kwargs):
		self.user_id = request.user.pk
		return super().dispatch(request, *args, **kwargs)

	def get_object(self, queryset=None):
		if not queryset:
			queryset = self.get_queryset()
		return get_object_or_404(queryset, pk=self.user_id)


class DeleteUserView(LoginRequiredMixin, DeleteView):
	model = AdvUser
	template_name = 'forum/delete_user.html'
	success_url = reverse_lazy('forum:index_name')

	def dispatch(self, request, *args, **kwargs):
		self.user_id = request.user.pk
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		logout(request)
		messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
		return super().post(request, *args, **kwargs)

	def get_object(self, queryset=None):
		if not queryset:
			queryset = self.get_queryset()
		return get_object_or_404(queryset, pk=self.user_id)


class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
	template_name = 'forum/reset_password.html'
	subject_template_name = 'email/reset_password_letter_subject.txt'
	email_template_name = 'email/reset_password_letter_body.txt'
	success_url = reverse_lazy('forum:password_reset_done_name')
	success_message = 'Письмо для восстановления пароля успешно отправлено на почту'


class UserPasswordResetDoneView(SuccessMessageMixin, PasswordResetDoneView):
	template_name = "forum/password_reset_done.html"


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
	template_name = 'forum/resetconfirm_password.html'
	# post_reset_login = True
	success_url = reverse_lazy('forum:index_name')
	success_message = 'Пароль успешно изменен'


def user_activate(request, sign):
	try:
		username = signer.unsign(sign)
	except BadSignature:
		return render(request, 'forum/bad_signature.html')
	user = get_object_or_404(AdvUser, username=username)
	if user.is_activated:
		template = 'forum/user_is_activated.html'
	else:
		template = 'forum/activation_done.html'
		user.is_active = True
		user.is_activated = True
		user.save()
	return render(request, template)

@login_required
def profile(request):
	return render(request, 'forum/profile.html')
	

# Likes
class AddLikeView(View):
	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('forum:login_name')

		discussion_id = int(request.POST.get('discussion_id'))
		user_id = int(request.POST.get('user_id'))

		user_inst = AdvUser.objects.get(pk=user_id)
		discussion_inst = Discussion.objects.get(pk=discussion_id)

		try:
			forum_likes_inst = ForumLikes.objects.get(discussion=discussion_inst, liked_by=user_inst)
		except Exception as e:
			forum_likes = ForumLikes(discussion=discussion_inst, liked_by=user_inst, like=True)
			forum_likes.save()
		return redirect('forum:index_name')

class RemoveLikeView(View):
	def post(self, request, *args, **kwargs):
		forum_likes_id = int(request.POST.get('forum_likes_id'))
		print('hey', forum_likes_id)
		forum_likes_inst = ForumLikes.objects.get(pk=forum_likes_id)
		forum_likes_inst.delete()
		return redirect('forum:index_name')