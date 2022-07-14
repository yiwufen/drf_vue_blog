# article/views.py

from django.http import Http404

from article.models import Article
from article.models import Category
from article.models import Tag
# from article.serializers import ArticleListSerializer
# from article.serializers import ArticleDetailSerializer

#------------视图集----------------------------
from rest_framework import viewsets
from article.serializers import ArticleSerializer
from article.serializers import CategorySerializer, CategoryDetailSerializer
from article.serializers import TagSerializer
from article.serializers import ArticleDetailSerializer
#-----------------------------------------------

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#对数据的增删改查是几乎每个项目的通用操作的库
from rest_framework import mixins
from rest_framework import generics

#       权限控制类
# from rest_framework.permissions import IsAdminUser
from article.permissions import IsAdminUserOrReadOnly

#---------过滤文章-----------------------
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# --------------------------------------------------------

#----------------头像------------------------
from article.models import Avatar
# 这个 AvatarSerializer 最后来写
from article.serializers import AvatarSerializer
#----------------------------------------------

# class ArticleDetail(APIView):
#     """文章详情视图"""

#     def get_object(self, pk):
#         """获取单个文章对象"""
#         try:
#             # pk 即主键，默认状态下就是 id
#             return Article.objects.get(pk=pk)
#         except:
#             raise Http404

#     def get(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleDetailSerializer(article)
#         # 返回 Json 数据
#         return Response(serializer.data)

#     def put(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleDetailSerializer(article, data=request.data)
#         # 验证提交的数据是否合法
#         # 不合法则返回400
#         if serializer.is_valid():
#             # 序列化器将持有的数据反序列化后，
#             # 保存到数据库中
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         article = self.get_object(pk)
#         article.delete()
#         # 删除成功后返回204
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """文章详情视图"""
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#------------------视图集前----------------------------
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#     #详情视图的权限
#     permission_classes = [IsAdminUserOrReadOnly]
#--------------------------------------------------

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------------------视图集前---------------------------
# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer

#     #   发布文章权限
#     permission_classes = [IsAdminUserOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

#------------------------------------------------------

class ArticleViewSet(viewsets.ModelViewSet):
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['author__username', 'title']

    #对文章标题的模糊搜索
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    #-------------------------------------------------
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    #--------------------------------------------------

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer
    
    
    # def get_queryset(self):
    #     queryset = self.queryset
    #     username = self.request.query_params.get('username', None)

    #     if username is not None:
    #         queryset = queryset.filter(author__username=username)

    #     return queryset
#------------------------分类模块---------------------
class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None

#---------------头像----------------------
class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]
#---------------------------------------------