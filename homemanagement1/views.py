from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Home list screen.")


def new_home(request):
    return HttpResponse("You're adding a new home")


def home_detail(request, home_id):
    response = "You are looking at the home detail for the home %s."
    return HttpResponse(response % home_id)


def new_record(request, home_id):
    response = "Add a record to the home %s"
    return HttpResponse(response % home_id)


def record_detail(request, home_id, record_id):
    response = "Record detail for home %s, and record: %s"
    return HttpResponse(response % (home_id, record_id))
