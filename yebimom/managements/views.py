from django.views.generic import View, TemplateView
# from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from centers.models.center import Center
from centers.models.center_landing import CenterLanding


class ManagementBaseView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ManagementBaseView, self).dispatch(*args, **kwargs)


class ManagementDashboard(ManagementBaseView, TemplateView):
    template_name = "managements/home.html"


class ManagementCenterLanding(ManagementBaseView, CreateView):
    template_name = "managements/landing.html"
    model = CenterLanding

    def get_context_data(self, **kwargs):
        context = super(ManagementCenterLanding, self).get_context_data(**kwargs)
        center = Center.objects.get(hash_id=self.kwargs['hash_id'])
        context['center'] = center
        context['center_landings'] = center.centerlanding_set.all()

        return context
