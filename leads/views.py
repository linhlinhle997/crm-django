from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Lead, Agent
from .forms import CustomUserCreationForm, LeadForm, LeadModelForm

# CRUD+L - Create, Retrieve, Update and Delete + List

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    # defaul call in html is {% for lead in object_list  %}
    # change with context_object_name = "leads" html will change {% for lead in leads  %}
    context_object_name = "leads"

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject = "A lead has been created", 
            message = "Go to the site to the new lead",
            from_email = "test@test.com",
            recipient_list = ["test@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


# =======> Old version of LandingPageView, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView <=======
# def landing_page(request):
#     return render(request, "landing.html")
# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads' : leads
#     }
#     return render(request, "leads/lead_list.html", context)

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead': lead
#     }
#     return render(request, "leads/lead_detail.html", context)

# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('leads:list')
#     context = {
#         "form": form
#     }
#     return render(request, 'leads/lead_create.html', context)
# =======> Old version of LandingPageView, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView <=======

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead) #instance=lead is get data of lead and show on form for update
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             lead.save()
#             return redirect('leads:detail')

#     context = {
#         'lead' : lead,
#         "form": form
#     }
#     return render(request, "leads/lead_update.html", context)

# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('leads:list')
# =======> Old version of lead_update <=======


# =======> Old version of lead_update <=======
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']

#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()

#             return redirect('list')

#     context = {
#         'lead' : lead,
#         "form": form
#     }
#     return render(request, "leads/lead_update.html", context)
# =======> Old version of lead_update <=======


# =======> Old version of lead_create <=======
# def lead_create(request):
#     form = LeadForm()
#     if request.method == 'POST':
#         print('Receiving a post request')
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             # ======> Start form.save() <======
#             # Get data input from form 
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first() #becacse agent is ForeignKey
#             # create new lead
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             # ======> End form.save() <======
#             # return leads list page after created lead success
#             return redirect('list')

#     context = {
#         "form": form
#     }
#     return render(request, 'leads/lead_create.html', context)
# =======> Old version of lead_update <=======