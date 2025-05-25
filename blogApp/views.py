from django.shortcuts import get_object_or_404, render
from . models import *
from . serializers import *
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
# Create your views here.

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def list(self, request, *args, **kwargs):
        '''Custom list method to modify response.'''
        cache_key = 'blogpost_list'
        cached_data = cache.get(cache_key)
        
        if cached_data:
            print("⚡ Data served from Redis cache")
            # return Response(cached_data)
            return Response({
                "source": "redis",
                "data": cached_data
            })
        
        print("🔄 Data served from Postgres DB")
        queryset = self.get_queryset() # Retrieve all blog posts
        serializer = self.get_serializer(queryset, many = True) # Serializes all blog posts (data)
        
        cache.set(cache_key, serializer.data, timeout = 60*3) #cache for 3 minutes
        # return Response(serializer.data)
        return Response({       # source Flag
            "source": "db",
            "data": serializer.data
        })
    
    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        cache.delete('blogpost_list') # Clear cache after new post creation
        return response


class BlogDetailView(APIView):
    def get(self,request, id):
        cache_key = f'blogpost_{id}'
        cached_data = cache.get(cache_key)
        
        if cached_data:
            print("⚡ Data served from Redis cache")
            return Response({
                'source': 'redis',
                'data': cached_data
            })
        print("🔄 Data served from Postgres DB")    
        blog = get_object_or_404(BlogPost,id=id)
        serializer = BlogPostSerializer(blog)
        cache.set(cache_key, serializer.data, timeout= 60*3)
        return Response({
            'source': 'db',
            'data': serializer.data
        })
        
    def patch(self, request, id):
        blog = get_object_or_404(BlogPost,id=id)
        serializer = BlogPostSerializer(blog,data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f'blogpost_{id}') # Invalidate cache
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id):
        blog = get_object_or_404(BlogPost,id=id)
        blog.delete()
        cache.delete(f'blogpost_{id}')
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# 🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴-----🔴  
    
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page

# @method_decorator(cache_page(60 * 3), name='dispatch') 
# class BlogListCreateView(generics.ListCreateAPIView):
#     queryset= BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
    
#     # remove manual Redis logic in list()
    
#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         cache.delete_pattern('*blogpost_list*')
#         return response
    
    
# class BlogDetailView(APIView):
    
#     @method_decorator(cache_page(60 * 3))
#     def get(self,request,id):
#         blog = get_object_or_404(BlogPost, id=id)
#         serializer = BlogPostSerializer(blog)
#         return Response({
#             'source': 'db',
#             'data': serializer.data
#         })
    
#     def patch(self, request, id):
#         blog = get_object_or_404(BlogPost, id=id)
#         serializer = BlogPostSerializer(blog, data = request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             cache.delete_pattern(f'*blogpost_{id}*')
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         blog = get_object_or_404(BlogPost, id=id)
#         blog.delete()
#         cache.delete_pattern(f'*blogpost_{id}*')
#         return Response(status=status.HTTP_204_NO_CONTENT)
        