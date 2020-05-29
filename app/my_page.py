from rest_framework.pagination import PageNumberPagination


class GMPagination(PageNumberPagination):
    page_size = 20  # 限定每页显示多少条数据
    page_query_param = 'page' # 这个配置决定在这儿输入“内容”=“页码”  跳转到相应的页面


    page_size_query_param = "size"

    max_page_size = 50  # 限制每页最多能显示多少条数据