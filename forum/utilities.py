from datetime import datetime
from os.path import splitext
from django.template.loader import render_to_string
from django.core.signing import Signer
from blog.settings import ALLOWED_HOSTS

signer = Signer()


def get_timestamp_path(instance, filename):
	return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])

def send_activation_notification(user):
	host = 'http://' + ALLOWED_HOSTS[0] if ALLOWED_HOSTS else 'http://localhost:8000'
	context = {
	'user': user, 
	'host': host, 
	'sign': signer.sign(user.username),
	}
	subject = render_to_string('email/activation_letter_subject.txt', context)
	body_text = render_to_string('email/activation_letter_body.txt', context)
	user.email_user(subject, body_text)
# def get_random_cats_photo():
# 	pass

