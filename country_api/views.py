from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Country
from .serializers import CountrySerializer, CountryListSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name_common', 'name_official']

    def get_serializer_class(self):
        if self.action == 'list':
            return CountryListSerializer
        return CountrySerializer

    @action(detail=True, methods=['get'])
    def same_region(self, request, pk=None):
        """List countries in the same region as the specified country"""
        country = self.get_object()
        same_region_countries = Country.objects.filter(
            region=country.region
        ).exclude(id=country.id)

        serializer = CountryListSerializer(same_region_countries, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_language(self, request):
        """List countries that speak a given language"""
        language = request.query_params.get('language', None)
        if not language:
            return Response(
                {"error": "Language parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        countries_with_language = []
        for country in Country.objects.all():
            if country.languages and any(
                    lang.lower() == language.lower()
                    for lang in country.languages.values()
            ):
                countries_with_language.append(country)

        serializer = CountryListSerializer(countries_with_language, many=True)
        return Response(serializer.data)


class CountryListView(LoginRequiredMixin, ListView):
    model = Country
    template_name = 'country_list.html'
    context_object_name = 'countries'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')

        if search_query:
            return Country.objects.filter(
                Q(name_common__icontains=search_query) |
                Q(name_official__icontains=search_query)
            )
        return Country.objects.all()


class CountryDetailView(LoginRequiredMixin, DetailView):
    model = Country
    template_name = 'country_detail.html'
    context_object_name = 'country'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add countries in the same region
        context['same_region_countries'] = Country.objects.filter(
            region=self.object.region
        )
        return context