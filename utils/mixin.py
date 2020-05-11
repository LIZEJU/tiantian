# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/5/11 12:37 PM
# Project: dailyfresh

from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        # 调用父类的as_view
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
