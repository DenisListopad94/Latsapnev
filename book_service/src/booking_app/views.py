from django.http import HttpResponse
from .models import Person
from django.shortcuts import render
from django.views import View


# function base view
def some_view(request, some_int, some_str):
    return HttpResponse(f"<h1>hello django app some int: {some_int} some str: {some_str}</h1>")


# def some_new_view(request, year):
#     return HttpResponse(f"<h1>regular expression view  some year {year} </h1>")

class MyView(View):
    def get(self, request, year):
        return HttpResponse(f"<h1>regular expression view  some year {year} </h1>")


# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def get_info_user(self):
#         return f"name :{self.name} age: {self.age}"


# def some_template_view(request):
#     # context = {
#     #     "some_arg": "hello world",
#     #     "some_list": [4, 2, 6, 1, 15, 16, 21],
#     #     "user": User("Jhon", 45)
#     # }
#
#     return render(
#         request=request,
#         template_name="base.html",
#         # context=context
#     )

def home_view(request):
    return render(
        request=request,
        template_name="home.html",
    )


comments = [
    {
        "number": 1,
        "user_id": 1,
        "name": "John",
        "comment": "some John comment"
    },
    {
        "number": 2,
        "user_id": 2,
        "name": "Ann",
        "comment": "some Ann comment"
    },
    {
        "number": 3,
        "user_id": 3,
        "name": "Peter",
        "comment": "some Peter comment"
    },
]


def user_comment_view(request):
    context = {
        "comments": comments
    }
    return render(
        request=request,
        template_name="user_comment.html",
        context=context
    )

def persons_view(request):
    context = {
        "persons" : Person.objects.all()
    }
    return render(
        request=request,
        template_name="persons.html",
        context=context
    )

from booking_app.models import Person

def print_all_users():
    all_users = Person.objects.all()
    for user in all_users:
        print(user)

print_all_users()

from booking_app.models import Hotel

def print_hotels_with_more_than_3_stars():
    hotels = Hotel.objects.filter(stars__gt=3)
    for hotel in hotels:
        print(hotel)

print_hotels_with_more_than_3_stars()

def print_users_over_40_with_name_starting_with_p():
    users = Person.objects.filter(age__gt=40, first_name__istartswith='P')
    for user in users:
        print(user)

print_users_over_40_with_name_starting_with_p()

def print_users_named_nick_or_suzan():
    users = Person.objects.filter(first_name__in=['Nick', 'Suzan'])
    for user in users:
        print(user)

print_users_named_nick_or_suzan()

def print_youngest_users():
    youngest_users = Person.objects.order_by('age')[:5]
    for user in youngest_users:
        print(user)

print_youngest_users()

def print_young_women():
    young_women = Person.objects.filter(sex='f', age__range=[18, 30])
    for woman in young_women:
        print(woman)

print_young_women()
