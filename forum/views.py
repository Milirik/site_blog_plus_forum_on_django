from django.shortcuts import render

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404

from django.core.signing import BadSignature

from .models import Discussion, Category, AdvUser
from .forms import ChangeUserInfoForm, RegisterUserForm, AnswerForm
from .utilities import signer

# Pages
def index(request):
	categories = Category.objects.all()
	return render(request, 'forum/index.html', 
		context={
		'categories':categories,
		})


# Discussions
def detail(request, pk):
	if request.method=="POST":
		pass
	else:
		discuss = get_object_or_404(Discussion, pk=pk)
		answer_form = AnswerForm()
		return render(
			request, 
			'forum/detail.html', 
			context = {
			'discuss': discuss,
			'answer_form':answer_form,
			},)


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
	

