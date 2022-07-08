from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView


@method_decorator(login_required, "dispatch")
class ProfileDetailView(DetailView):
    """View that renders a member's profile."""

    def setup(self, request, *args, **kwargs) -> None:
        if "pk" not in kwargs and request.member:
            kwargs["pk"] = request.member.pk
        super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        return {}
