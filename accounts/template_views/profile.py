from django.views.generic import TemplateView

from accounts.forms import UserChangeForm


class ProfileView(TemplateView):
    template_name = "auth/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "VooCommerce | Profile"
        context["current_user"] = self.request.user
        context["form"] = UserChangeForm()
        return context
