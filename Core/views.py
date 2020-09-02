from django.shortcuts import render
# Create your views here.
from django.views.generic import DetailView, ListView

from Core.forms import ContactForm
from Core.models import Article, ContactMessage, Slider


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"


class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    template_name = "articles/list.html"


def homepage(request):
    context = {
        "articles":  Article.objects.order_by("publish")[:5],
        "sliders": Slider.objects.all()
    }
    return render(request, template_name="index.html", context=context)


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            model = ContactMessage()
            model.subject = subject
            model.email = from_email
            model.message = message
            model.save()
            return render(request, "pages/contact.html", {'form': ContactForm(), "success": True})
    return render(request, "pages/contact.html", {'form': form})
