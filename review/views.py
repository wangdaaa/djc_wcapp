import datetime
import os
import traceback

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from review.app_serializer import ReviewGameFileDBSerializer,CreateReviewGameFileDBSerializer
from review.func_tools import create_new_name
from review.models import  ReviewGameFileDB
from review.my_page import GMPagination
from djc_wcapp.settings import MEDIA_ROOT


class ReviewGameFileDBView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        params=request.query_params
        query_dic={}
        if params:
            if "name" in params:
                query_dic['name']= params.get('name')
                params.get('name')
            if 'description' in params:
                if params.get('description'):
                    query_dic['description'] = params.get('description')
        res=ReviewGameFileDB.objects.filter(**query_dic)
        pp=GMPagination()
        pager_gms=pp.paginate_queryset(queryset=res,request=request,view=self)
        bs=ReviewGameFileDBSerializer(pager_gms,many=True)
        return pp.get_paginated_response(bs.data)

    def post(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        image = request.FILES.get("image")
        if image:
            new_name=create_new_name(image.name)
            if new_name:
                with open(os.path.join(MEDIA_ROOT,new_name),'wb+') as e:
                    for line in image:
                        e.write(line)
                request.data['image']=new_name
                post_data=CreateReviewGameFileDBSerializer(data=request.data,many=False)
                if post_data.is_valid():
                    res=post_data.save()
                    data['result']['data']=res.name
                    data['msg']='创建成功'
                else:
                    data['code']=-1
                    data['msg']=post_data.errors
            else:
                data['code'] = -1
                data['msg'] = '上传的图片格式有误'
        else:
            data['code'] = -1
            data['msg'] = '请上传图片'

        return Response(data)

class ForReviewGameFileDBView(APIView):

    def get(self, request, *args, **kwargs):
        data={
            "count": 2,
            "next": "",
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "image": "/static/5931b46470d0eff6d280f42096f72b73.png",
                    "name": "游戏一",
                    "description": "",
                    "available": False,
                    "create_data": "2020-07-08T12:48:19.608456Z",
                    "update_data": "2020-07-14T06:49:12.923006Z"
                },
                {
                    "id": 2,
                    "image": "/static/5931b46470d0eff6d280f42096f72b73.png",
                    "name": "女商人",
                    "description": "功能升级中，敬请期待",
                    "available": False,
                    "create_data": "2020-07-08T12:55:42.075637Z",
                    "update_data": "2020-07-14T06:50:16.053894Z"
            },]
            }
        return Response(data)

    def post(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        image = request.FILES.get("image")
        if image:
            new_name=create_new_name(image.name)
            if new_name:
                with open(os.path.join(MEDIA_ROOT,new_name),'wb+') as e:
                    for line in image:
                        e.write(line)
                request.data['image']=new_name
                post_data=CreateReviewGameFileDBSerializer(data=request.data,many=False)
                if post_data.is_valid():
                    res=post_data.save()
                    data['result']['data']=res.name
                    data['msg']='创建成功'
                else:
                    data['code']=-1
                    data['msg']=post_data.errors
            else:
                data['code'] = -1
                data['msg'] = '上传的图片格式有误'
        else:
            data['code'] = -1
            data['msg'] = '请上传图片'

        return Response(data)


class ReviewGameFileDBDeatailView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        gm_id=kwargs.get("gm_id")
        if gm_id and  gm_id.isdigit():
            res=ReviewGameFileDB.objects.filter(id=gm_id,)
            if res:
                res = ReviewGameFileDBSerializer(res.first(), many=False)
                res = res.data
                data['result']['data'] = res
            else:
                data['code']=-1
                data['msg']='查询的游戏数据不存在'
        else:
            data['code'] = -1
            data['msg'] = '请传入id'
          
        return Response(data)


    def put(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        gm_id=kwargs.get("gm_id")
        if gm_id and  gm_id.isdigit():
            pre_cs_obj=ReviewGameFileDB.objects.filter(id=gm_id)
            if pre_cs_obj:
                post_data = request.data
                post_data = ReviewGameFileDBSerializer(instance=pre_cs_obj.first(),data=post_data)
                if post_data.is_valid():
                    post_data.save()
                    data['msg'] = '更新成功'
                else:
                    data['code'] = -1
                    data['msg'] = post_data.errors
            else:
                data['code'] = -1
                data['msg'] = '无此游戏数据'
        else:
            data['code'] = -1
            data['msg'] = '无此游戏数据'

        return Response(data)

    def delete(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        gm_id=kwargs.get("gm_id")
        if gm_id and  gm_id.isdigit():
            pre_cs_obj=ReviewGameFileDB.objects.filter(id=gm_id)
            if pre_cs_obj:

                if pre_cs_obj.first().available==False:
                #todo: 判断是否是启用，启用状态不能删除
                    file_path = os.path.join(MEDIA_ROOT, pre_cs_obj.first().image)
                    del_res=pre_cs_obj.delete()
                    if del_res[0]==1:
                        try:
                            os.remove(file_path)
                        except Exception as e:
                            data['msg'] = e
                    data['msg'] = '删除成功'+data['msg']
                else:
                    data['msg'] = '删除失败，请先禁用'
            else:
                data['code'] = -1
                data['msg'] = '无此游戏数据'
        else:
            data['code'] = -1
            data['msg'] = '无此游戏数据'

        return Response(data)


class EnableReviewGameFileDBDeatailView(APIView):

    def put(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        gm_id = kwargs.get("gm_id")
        if gm_id and  gm_id.isdigit():
            pre_cs_obj = ReviewGameFileDB.objects.filter(id=gm_id)
            if pre_cs_obj:
                pre_cs_obj.update(available=True)
                data['msg'] = '更新成功'
            else:
                data['code'] = -1
                data['msg'] = '无此游戏数据'
        else:
            data['code'] = -1
            data['msg'] = '无此游戏数据'

        return Response(data)


class DisableReviewGameFileDBDeatailView(APIView):

    def put(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        gm_id = kwargs.get("gm_id")
        if gm_id and  gm_id.isdigit():
            pre_cs_obj = ReviewGameFileDB.objects.filter(id=gm_id)
            if pre_cs_obj:
                pre_cs_obj.update(available=False)
                data['msg'] = '更新成功'
            else:
                data['code'] = -1
                data['msg'] = '无此游戏数据'
        else:
            data['code'] = -1
            data['msg'] = '无此游戏数据'

        return Response(data)


class HelloView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        return Response(data)