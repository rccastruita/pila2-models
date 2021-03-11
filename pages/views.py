from django.views.generic import ListView
from .models import Personaje

# Create your views here.
class HomePageView(ListView):
    model = Personaje
    template_name = 'home.html'
    context_object_name = 'personaje_objects'