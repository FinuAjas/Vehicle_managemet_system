from django.shortcuts import redirect
from . models import Vehicle
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . forms import VehicleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages


# Home view accessible to all users
class Home(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicles'] = Vehicle.objects.all()
        return context


# Add new vehicle details view accessible to only superadmin
class AddVehicle(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vehicle
    template_name = 'addvehicle.html'
    form_class = VehicleForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            messages.success(self.request, 'New Vehicle details added!')
            return redirect('home')

    def test_func(self):
        return self.request.user.is_superadmin

    def handle_no_permission(self):
        messages.error(
            self.request, 'You are not authorized to do this operation!')
        return redirect('home')


# Edit or Update vehicle details view accessible to superadmin and admin
class UpdateVehicle(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vehicle
    template_name = 'updatevehicle.html'
    form_class = VehicleForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Vehicle details updated!')
            return redirect('home')

    def test_func(self):
        return self.request.user.is_admin

    def handle_no_permission(self):
        messages.error(
            self.request, 'You are not authorized to do this operation!')
        return redirect('home')


# Delete vehicle details view accessible to only superadmin
class DeleteVehicle(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vehicle
    success_url = '/'
    template_name = 'vehicle_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Vehicle details deleted successfully.')
        return response

    def test_func(self):
        return self.request.user.is_superadmin

    def handle_no_permission(self):
        messages.error(
            self.request, 'You are not authorized to do this operation!')
        return redirect('home')
