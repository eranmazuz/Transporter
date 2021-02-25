from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse

from Management.form import RouteModelForm
from Management.form import StationFormset
from Management.models import Route, Station
from django.shortcuts import get_object_or_404


class RouteListView(generic.ListView):
    model = Route
    template_name = 'Management/route/list.html'
    context_object_name = 'routes'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(RouteListView, self).get_context_data(**kwargs)
        routes = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(routes, self.paginate_by)
        try:
            routes = paginator.page(page)
        except PageNotAnInteger:
            routes = paginator.page(1)
        except EmptyPage:
            routes = paginator.page(paginator.num_pages)
        context['routes'] = routes
        return context

class RouteUpdateView(generic.UpdateView):
    model = Route
    template_name = 'Management/route/update.html'
    context_object_name = 'route'
    fields = ('name',)
    success_url = reverse_lazy('route_list')

class RouteDeleteView(generic.DeleteView):
    model = Route
    template_name = 'Management/route/delete.html'
    success_url = reverse_lazy('route_list')

class RouteCreateView(generic.CreateView):
    model = Route
    template_name = 'Management/route/create.html'
    fields = ('name',)
    success_url = reverse_lazy('route_list')

def create_route_view(request):
    if request.method == 'GET':
        route_form = RouteModelForm()
        stations_formset = StationFormset(queryset=Station.objects.none())
        return render(request, 'Management/route/create.html', {
            'routeform' : route_form,
            'formset' : stations_formset,
        })
    route_form = RouteModelForm(request.POST)
    stations_formset = StationFormset(request.POST)

    if not route_form.is_valid() or not stations_formset.is_valid():
        return HttpResponse(content= render(request, 'Management/route/create.html', {
            'routeform': route_form,
            'formset': stations_formset,
        }), status= 400)


    route = route_form.save()

    for station_formset in stations_formset:
        station = station_formset.save(commit=False)
        station.route = route
        station.save()

    return redirect('route_list')

def edit_route_view(request, pk):
    route = get_object_or_404(Route, pk=pk)

    if request.method == 'GET':

        route_form = RouteModelForm(instance=route)
        stations_formset = StationFormset(instance=route)
        return render(request, 'Management/route/create.html', {
            'routeform' : route_form,
            'formset' : stations_formset,
        })
    route_form = RouteModelForm(request.POST, instance= route)
    stations_formset = StationFormset(request.POST, instance= route)

    if not route_form.is_valid() or not stations_formset.is_valid():
        return HttpResponse(content= render(request, 'Management/route/create.html', {
            'routeform': route_form,
            'formset': stations_formset,
        }), status= 400)


    route = route_form.save()

    for station_formset in stations_formset:
        station = station_formset.save(commit=False)
        station.route = route
        station.save()

    return redirect('route_list')



