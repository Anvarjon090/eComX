from django.views.generic import TemplateView

from accounts.forms import UserCreationForm


class RegisterView(TemplateView):
    template_name = "auth/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "VooCommerce | Register"
        context["form"] = UserCreationForm()
        return context
