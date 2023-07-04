from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from tours.data import tours


class MainPageView(View):
    def get(self, request):
        return render(request, 'index.html', {'tours': tours})


class DepartureView(View):
    def get(self, request, departure):
        out_tours = {}
        min_price = 100000
        max_price = 0
        nigths_min = 100000
        nigths_max = 0
        for tour_id, tour_info in tours.items():
            if tour_info['departure'] == departure:
                out_tours[tour_id] = tour_info
                if tour_info['price'] < min_price:
                    min_price = tour_info['price']
                if tour_info['price'] > max_price:
                    max_price = tour_info['price']
                if tour_info['nights'] < nigths_min:
                    nigths_min = tour_info['nights']
                if tour_info['nights'] > nigths_max:
                    nigths_max = tour_info['nights']
        return render(request, 'departure.html',
                      {'tours': out_tours, 'departure': departure,
                       'min_price': min_price, 'max_price': max_price,
                       'nights_min': nigths_min, 'nights_max': nigths_max})


class TourView(View):
    def get(self, request, tour_id):
        return render(request, 'tour.html', {'tour': tours[tour_id]})
