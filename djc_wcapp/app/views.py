import datetime
import os
import traceback

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from app.app_serializer import GameFileDBSerializer, CreateGameFileDBSerializer
from app.func_tools import create_new_name
from app.models import  GameFileDB
from app.my_page import GMPagination
from djc_wcapp.settings import MEDIA_ROOT


class GameFileDBView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }

        res=GameFileDB.objects.filter(available=True)

        pp=GMPagination()
        pager_gms=pp.paginate_queryset(queryset=res,request=request,view=self)
        bs=GameFileDBSerializer(pager_gms,many=True)
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
                post_data=CreateGameFileDBSerializer(data=request.data,many=False)
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


class GameFileDBDeatailView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        gm_id=kwargs.get("gm_id")
        print('sssss')
        if gm_id:
            res=GameFileDB.objects.filter(id=gm_id,available=True)
            if res:
                res = GameFileDBSerializer(res, many=True)
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
        if gm_id:
            pre_cs_obj=GameFileDB.objects.filter(id=gm_id)
            if pre_cs_obj:
                post_data = request.data
                post_data = GameFileDBSerializer(instance=pre_cs_obj.first(),data=post_data)
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
        if gm_id:
            pre_cs_obj=GameFileDB.objects.filter(id=gm_id)
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


class EnableGameFileDBDeatailView(APIView):

    def put(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        gm_id = kwargs.get("gm_id")
        if gm_id:
            pre_cs_obj = GameFileDB.objects.filter(id=gm_id)
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


class DisableGameFileDBDeatailView(APIView):

    def put(self, request, *args, **kwargs):
        data = {
            "code": 0,
            "msg": "",
            "result": {"data": {}}
        }
        gm_id = kwargs.get("gm_id")
        if gm_id:
            pre_cs_obj = GameFileDB.objects.filter(id=gm_id)
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

#
# from rest_framework_jwt.views import JSONWebTokenAPIView
# from rest_framework_jwt.utils import jwt_response_payload_handler
# from rest_framework_jwt.serializers import JSONWebTokenSerializer
#
# class XD_JSONWebTokenAPIView(JSONWebTokenAPIView):
#     """
#     Base API View that various JWT interactions inherit from.
#    """
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#
#         if serializer.is_valid():
#             user = serializer.object.get('user') or request.user
#             token = serializer.object.get('token')
#             response_data = jwt_response_payload_handler(token, user, request)
#             response_data['is_first']=user.is_default_pwd
#             response = Response(response_data)
#             print(response,'这是response===',response_data,user,type(user))
#             if api_settings.JWT_AUTH_COOKIE:
#                 print('是否进来了')
#                 expiration = (datetime.datetime.utcnow() +
#                               api_settings.JWT_EXPIRATION_DELTA)
#                 response.set_cookie(api_settings.JWT_AUTH_COOKIE,
#                                     token,
#                                     expires=expiration,
#                                     httponly=True)
#             return response
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ObtainJSONWebToken(XD_JSONWebTokenAPIView):
#     """
#     API View that receives a POST with a user's username and password.
#
#     Returns a JSON Web Token that can be used for authenticated requests.
#     """
#     serializer_class = JSONWebTokenSerializer
#
#
# xd_obtain_jwt_token = ObtainJSONWebToken.as_view()