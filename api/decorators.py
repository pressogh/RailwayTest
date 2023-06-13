import traceback
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework import serializers
from api.errors import API_EXCEPTION_0001, VALIDATION_ERROR_0001
import logging


# 에러에 대한 알림을 받고 싶으면, 이 데코레이터 안에서 처리하세요.
def api_raise_exception(func):
	def decorated_func(*args, **kwargs):
		logger = logging.getLogger("django")
		try:
			with transaction.atomic():
				value = func(*args, **kwargs)
			return value
		except serializers.ValidationError as e:
			logger.error(traceback.format_exc())
			return VALIDATION_ERROR_0001.as_res(str(e))
		except ObjectDoesNotExist as e:
			print("ObjectDoesNotExist")
			logger.error(traceback.format_exc())
			traceback.print_exc()
			return VALIDATION_ERROR_0001.as_res(str(e))
		except Exception:
			logger.error(traceback.format_exc())
			traceback.print_exc()
			return API_EXCEPTION_0001.as_res()

	return decorated_func


def api_view_raise_exception(cls):
	mixin_actions = ["create", "retrieve", "list", "update", "partial_update", "destroy"]
	view_actions = ["get", "put", "post", "patch", "delete"]
	actions = mixin_actions + view_actions
	for action in actions:
		func = getattr(cls, action, None)
		if func is not None:
			wrapper_func = api_raise_exception(func)
			setattr(cls, action, wrapper_func)
	return cls


class RaiseException:
	def __init__(self, *args, **kwargs):
		if len(args) == 1:
			self._func = args[0]
		else:
			self._func = None

	def __call__(self, *args, **kwargs):
		def wrapped(*_args, **_kwargs):
			try:
				self._func(*_args, **kwargs)
			except Exception:
				traceback.print_exc()
				raise

		return wrapped(*args, **kwargs)

	def __enter__(self, *args, **kwargs):
		return self

	def __exit__(self, exctype, excinst, exctb):
		if exctype is not None:
			traceback.print_exc()
		return exctype is None


def raise_exception(func=None, *args, **kwargs):
	if callable(func):  # using as a decorator
		return RaiseException(func)
	else:  # using as a context manager
		return RaiseException()
