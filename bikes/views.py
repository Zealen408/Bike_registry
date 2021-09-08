from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView


from .forms import BikeForm
from .models import bike


@login_required()
def bike_create(request):
    if request.POST:
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Input saved')
            return redirect('bikes:list', username=request.user.email)
    form = BikeForm()
    return render(request, 'bikes/bike_create.html', {'form': form})


class BikeDelete(DeleteView):
    model = bike

    def get_success_url(self):
        email = self.object.owner.email
        return reverse_lazy('bikes:list', kwargs={'username': email})


@login_required()
def bike_list(request, username):
    my_bikes = bike.objects.filter(owner__email=username)
    context = {
        'bikes': my_bikes,
    }
    return render(request, 'bikes/bike_list.html', context)


@login_required()
def bike_detail(request, username, serial_number):
    instance = get_object_or_404(bike, owner__email=username, bike_serial_number=serial_number)
    if request.POST:
        form = BikeForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Input saved')
            return redirect('bikes:list', username=request.user.email)
    form = BikeForm(instance=instance)
    return render(request, 'bikes/bike_detail.html', {'form': form, 'bike': instance})

def lost_bikes(request):
    stolen_bikes = bike.objects.get().filter(bike_stolen=True)
    context = {'bikes': stolen_bikes}
    return render(request, 'bikes/bike_stolen.html', context)

# def bikeDetail1(request):
#
#     if request.method == 'POST':
#         form = bikeForm(request, request.POST)
#         form.data['owner'] = request.user.id
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Bike saved successfully.')
#             return redirect('bike:bike_list')
#
#         else:
#             messages.error(request, 'Invalid data, please retry.')
#
#     form = bikeForm()
#     return render(request, 'bikes/bike_detail.html', {'form': form})