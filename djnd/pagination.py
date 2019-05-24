from rest_framework import pagination


class VariableSizePageNumberPagination(pagination.PageNumberPagination):
  page_size = 10
  page_size_query_param = 'size'
  max_page_size = 1000
