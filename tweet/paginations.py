from rest_framework.pagination import PageNumberPagination

class SubtweetPagination(PageNumberPagination):
    page_size = 3