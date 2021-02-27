from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse

from Management.forms import RouteModelForm
from Management.forms.station import StationFormSet
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

class RouteCreateView(generic.CreateView):
    model = Route
    template_name = 'Management/route/create.html'
    success_url = reverse_lazy('route_list')
    form_class = RouteModelForm

    def post(self, request, *args, **kwargs):
        station_formset = StationFormSet(request.POST)
        route_form = RouteModelForm(data=request.POST)
        if station_formset.is_valid() and route_form.is_valid():
            return self.form_valid(station_formset, route_form)

    def form_valid(self, station_formset, route_form):
        route = route_form.save()
        stations = station_formset.save(commit=False)
        for deleted_station in station_formset.deleted_objects:
            deleted_station.delete()
        for station in stations:
            station.route = route
            station.save()

        return HttpResponseRedirect(self.success_url)


    def get_context_data(self, **kwargs):
        context = super(RouteCreateView, self).get_context_data(**kwargs)
        context['station_formset'] = StationFormSet(queryset=Station.objects.none())
        context['route_form'] = RouteModelForm()
        return context

class RouteUpdateView(generic.UpdateView):
    model = Route
    template_name = 'Management/route/update.html'
    success_url = reverse_lazy('route_list')
    form_class = RouteModelForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        station_formset = StationFormSet(request.POST, instance=self.object)
        route_form = RouteModelForm(data=request.POST, instance=self.object)
        if station_formset.is_valid() and route_form.is_valid():
            return self.form_valid(station_formset, route_form)
        else:
            return self.form_invalid(station_formset = station_formset, route_form =route_form)

    def form_valid(self, station_formset, route_form):
        route = route_form.save()
        stations = station_formset.save(commit=False)
        for deleted_station in station_formset.deleted_objects:
            deleted_station.delete()
        for station in stations:
            station.route = route
            station.save()

        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, station_formset, route_form, **kwargs):
        """If the form is invalid, render the invalid form."""
        context = self.get_context_data(**kwargs)
        context['station_formset'] = station_formset
        context['route_form'] = route_form
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(RouteUpdateView, self).get_context_data(**kwargs)
        context['station_formset'] = StationFormSet(instance=self.object)
        context['route_form'] = RouteModelForm(instance=self.object)
        return context

class RouteDeleteView(generic.DeleteView):
    model = Route
    template_name = 'Management/route/delete.html'
    success_url = reverse_lazy('route_list')



