from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from seminar_3_app.models import Author, Post, Comment

from .forms import GamesForm, AddAuthorForm, AddPostForm, AddComment


# Create your views here.
def game_view(request):
    results = []
    if request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['change_game']
            game = globals()[game_type]()
            count = form.cleaned_data['count']
            for i in range(count):
                game.play()
                results.append(str(game))
    else:
        form = GamesForm()
    return render(request, 'seminar_4_app/game.html', {'form': form, 'results': results})


class AddAuthor(CreateView):
    model = Author
    template_name = 'seminar_4_app/add_author.html'
    form_class = AddAuthorForm


class AuthorPage(DetailView):
    model = Author
    template_name = 'seminar_4_app/author_page.html'


class AddPost(CreateView):
    model = Post
    template_name = 'seminar_4_app/add_post.html'
    form_class = AddPostForm


class PostViews(CreateView):
    model = Post
    template_name = 'seminar_4_app/post.html'
    context_object_name = 'post'
    form_class = AddComment

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs['pk'])
        comments = Comment.objects.filter(post=post).all().order_by('-publish_date')
        context['post'] = post
        context['comments'] = comments
        return context
