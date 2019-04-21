from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@never_cache
def personal_management_dashboard_home(request):
    """
        Function for rendering the personal management dashboard
    """
    return render(request, 'personal_management_dashboard_home/personal_management_dashboard_home.html')


@csrf_exempt
def holiday_details(request):
    """
        Function returns JSON data containing holiday's details. Involves AJAX Call.
    """
    holiday_new_year = dict()
    holiday_martin_luther_king_jr = dict()
    holiday_Washington = dict()
    holiday_Memorial = dict()
    holiday_Independence = dict()
    holiday_Labor = dict()
    holiday_Veterans = dict()
    holiday_Thanksgiving = dict()
    holiday_Christmas = dict()
    holiday_new_year['holiday'] = "Tuesday, January 1"
    holiday_new_year['holiday_reason'] = "New Year’s Day"
    holiday_martin_luther_king_jr['holiday'] = "Monday, January 21"
    holiday_martin_luther_king_jr['holiday_reason'] = "Martin Luther King, Jr"
    holiday_Washington['holiday'] = "Monday, February 18"
    holiday_Washington['holiday_reason'] = "Washington’s Birthday"
    holiday_Memorial['holiday'] = "Monday, May 27"
    holiday_Memorial['holiday_reason'] = "Memorial Day"
    holiday_Independence['holiday'] = "Thursday, July 4"
    holiday_Independence['holiday_reason'] = "Independence Day"
    holiday_Labor['holiday'] = "Monday, September 21"
    holiday_Labor['holiday_reason'] = "Labor Day"
    holiday_Veterans['holiday'] = "Monday, November 11"
    holiday_Veterans['holiday_reason'] = "Veterans Day"
    holiday_Thanksgiving['holiday'] = "Thursday, November 28"
    holiday_Thanksgiving['holiday_reason'] = "Thanksgiving Day"
    holiday_Christmas['holiday'] = "Wednesday, December 25"
    holiday_Christmas['holiday_reason'] = "Christmas Day"
    response = [holiday_new_year, holiday_martin_luther_king_jr, holiday_Washington, holiday_Memorial,
                holiday_Independence, holiday_Labor, holiday_Veterans, holiday_Thanksgiving, holiday_Christmas]
    return HttpResponse(json.dumps(response), content_type="application/json")


def about_page(request):
    """
        Function for rendering about dashboard page.
    """
    return render(request, 'personal_management_dashboard_home/about_page.html')
