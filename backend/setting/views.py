

from django.http import HttpResponse


def math_operation(a: int, b: int) -> int:
    return a*a + b*b


def example(request):
    math_operation(3, 4)
    return HttpResponse('Hello, World!')
