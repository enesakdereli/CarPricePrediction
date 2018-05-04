from django.shortcuts import render, redirect
from .models import Brand, UserPreference, Series, Model,User
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserPreferenceForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


@login_required
def home(request):
    return render(request, 'home.html')
def cpp_home(request):
    return render(request, 'cpp/home.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    return render(request, 'base.html')


class UserPreferenceListView(ListView):
    model = UserPreference
    context_object_name = 'userpreferences'


class UserPreferenceCreateView(CreateView):
    model = UserPreference
    form_class = UserPreferenceForm
    success_url = reverse_lazy('cpp:userpreference_changelist')


class UserPreferenceUpdateView(UpdateView):
    model = UserPreference
    form_class = UserPreferenceForm
    success_url = reverse_lazy('cpp:userpreference_changelist')


def load_dropdown(request):
    brand_id = request.GET.get('brand')
    series_id = request.GET.get('series')
    #user_id = request.GET.get('user').index()
    #user_id = request.user.id
    series = Series.objects.filter(brand_id=brand_id).order_by('series_name')
    models = Model.objects.filter(series_id=series_id).order_by('model_name')
    #user = User.objects.filter(id=user_id)

    return render(request, 'cpp/dropdown_list_options.html', {'series': series, 'models':models})


class UserFormView(View):
    """
    form_class = UserForm
    template = 'cpp/registration_splash.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():#make sure that user filled all required areas.
            user = form.save(commit=False)#dont save in db
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password= password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cpp:index')
        return render(request, self.template, {'form': form})
        """