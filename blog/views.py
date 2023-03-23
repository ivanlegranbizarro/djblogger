from django.views import generic

from .models import Post


class HomeView(generic.ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return ["blog/components/post-list-elements.html"]
        return ["blog/home.html"]


class DetailPostView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    lookup_field = "slug"
    context_object_name = "post"
