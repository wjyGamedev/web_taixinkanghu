# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.core.serializers import json
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest
from django.template import Context
from django.template.loader import get_template

# log
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
        'head_title': u'Django Bookmarks',
        'page_title': u'Welcome to Django Bookmarks',
        'page_body': u'Where you can store and share bookmarks!'
    })
    output = template.render(variables)
    return HttpResponse(output)


# register
import requests

class MobSMS:
    def __init__(self, appkey):
        self.appkey = appkey
        self.verify_url = 'https://api.sms.mob.com/sms/verify'

    def verify_sms_code(self, zone, phone, code, debug=False):
        if debug:
            return 200

        data = {'appkey': self.appkey, 'phone': phone, 'zone': zone, 'code': code}
        req = requests.post(self.verify_url, data=data, verify=False)
        if req.status_code == 200:
            j = req.json()
            return j.get('status', 500)

        return 500


@csrf_exempt
def handle_register(request):
    import json
    # request.get_full_path()
    if request.method == 'POST':
        try:
            body_data = json.loads(request.body.decode('utf-8'))
        except Exception as e:
            logger.debug('body_data json.loads error')
            # return HttpResponseBadRequest(json.dumps({'error': 'Invalid request: {0}'.format(str(e))}), content_type="application/json")

        logger.debug('Raw Data: "%s"' % request.body)
        logger.debug('body_data: "%s"', body_data)

        logger.debug('zone: "%s"', body_data['zone'])
        logger.debug('phone: "%s"', body_data['phone'])
        logger.debug('code: "%s"', body_data['code'])
        #
        # for ele in bodyArray:
        #     logger.debug('ele %s%',ele)
        #
        # bodydic = {}
        # for ele in bodyArray:
        #     bodyArrayEle = ele.split(':')
        #     bodydic[bodyArrayEle[0]] = bodyArrayEle[1]
        #
        # for key in bodydic:
        #     logger.debug('map key%s:=s%', key, bodydic[key])
    return HttpResponse(request.body)
    # return  mobsms.verify_sms_code(86, 13900000000, '1234')












def hospital_list(request):
    import json

    request.get_full_path()
    response_data = {"type":"hospital_list","hospital_list":[{"id":1,"name":"北京朝阳医院"},{"id":2,"name":"北京天坛医院"},{"id":3,"name":"医科院肿瘤医院"}], "Version":1}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def nurse_basics_list(request):
    import json

    request.get_full_path()
    response_data = {"type":"nurse_basics_list","nurse_basics_list":[{"id":1 ,"hospital_id":1,"name":"孔展诚","star_level":3,"age":"28","hometown":"河南","nursing_exp":2,"nursing_level":0,"service_charge_per_day":120,"nurse_service_status":0},{"id":2 ,"hospital_id":2,"name":"连梁良","star_level":5,"age":"31","hometown":"河北","nursing_exp":3,"nursing_level":1,"service_charge_per_day":150,"nurse_service_status":1},{"id":3 ,"hospital_id":3,"name":"危萌立","star_level":4,"age":"45","hometown":"甘肃","nursing_exp":4,"nursing_level":2,"service_charge_per_day":180,"nurse_service_status":0},{"id":4 ,"hospital_id":1,"name":"邢乐亮","star_level":3,"age":"35","hometown":"辽宁","nursing_exp":5,"nursing_level":3,"service_charge_per_day":200,"nurse_service_status":1},{"id":5 ,"hospital_id":2,"name":"古秩仆","star_level":5,"age":"59","hometown":"吉林","nursing_exp":6,"nursing_level":0,"service_charge_per_day":120,"nurse_service_status":0},{"id":6 ,"hospital_id":3,"name":"田觉保","star_level":4,"age":"34","hometown":"河南","nursing_exp":7,"nursing_level":1,"service_charge_per_day":150,"nurse_service_status":1},{"id":7 ,"hospital_id":1,"name":"程亚锐","star_level":3,"age":"36","hometown":"湖南","nursing_exp":8,"nursing_level":2,"service_charge_per_day":180,"nurse_service_status":0},{"id":8 ,"hospital_id":2,"name":"梁胜望","star_level":5,"age":"45","hometown":"湖北","nursing_exp":2,"nursing_level":3,"service_charge_per_day":200,"nurse_service_status":1},{"id":9 ,"hospital_id":3,"name":"成泰寒","star_level":4,"age":"41","hometown":"贵州","nursing_exp":3,"nursing_level":0,"service_charge_per_day":120,"nurse_service_status":0},{"id":10,"hospital_id":1,"name":"唐昆秀","star_level":3,"age":"31","hometown":"云南","nursing_exp":4,"nursing_level":1,"service_charge_per_day":150,"nurse_service_status":1},{"id":11,"hospital_id":2,"name":"戚菊汐","star_level":5,"age":"49","hometown":"宁夏","nursing_exp":5,"nursing_level":2,"service_charge_per_day":180,"nurse_service_status":0},{"id":12,"hospital_id":3,"name":"苏勤峰","star_level":4,"age":"38","hometown":"山西","nursing_exp":6,"nursing_level":3,"service_charge_per_day":200,"nurse_service_status":1},{"id":13,"hospital_id":1,"name":"史盼泽","star_level":3,"age":"37","hometown":"山西","nursing_exp":7,"nursing_level":0,"service_charge_per_day":120,"nurse_service_status":0},{"id":14,"hospital_id":2,"name":"周甜修","star_level":4,"age":"48","hometown":"陕西","nursing_exp":8,"nursing_level":1,"service_charge_per_day":150,"nurse_service_status":1},{"id":15,"hospital_id":3,"name":"岳毅弥","star_level":3,"age":"42","hometown":"山东","nursing_exp":2,"nursing_level":2,"service_charge_per_day":180,"nurse_service_status":0},{"id":16,"hospital_id":1,"name":"费磊行","star_level":5,"age":"40","hometown":"安徽","nursing_exp":3,"nursing_level":3,"service_charge_per_day":200,"nurse_service_status":1},{"id":17,"hospital_id":2,"name":"陶俩鸿","star_level":4,"age":"30","hometown":"浙江","nursing_exp":4,"nursing_level":0,"service_charge_per_day":120,"nurse_service_status":0},{"id":18,"hospital_id":3,"name":"邱映皆","star_level":3,"age":"36","hometown":"上海","nursing_exp":5,"nursing_level":1,"service_charge_per_day":150,"nurse_service_status":1},{"id":19,"hospital_id":1,"name":"孟家凡","star_level":5,"age":"45","hometown":"天津","nursing_exp":6,"nursing_level":2,"service_charge_per_day":180,"nurse_service_status":0},{"id":20,"hospital_id":2,"name":"金奎付","star_level":4,"age":"46","hometown":"北京","nursing_exp":7,"nursing_level":3,"service_charge_per_day":200,"nurse_service_status":1},{"id":21,"hospital_id":3,"name":"张冬皓","star_level":3,"age":"35","hometown":"广东","nursing_exp":8,"nursing_level":0,"service_charge_per_day":120,"nurse_service_status":0},{"id":22,"hospital_id":1,"name":"萧襄保","star_level":5,"age":"37","hometown":"广西","nursing_exp":2,"nursing_level":1,"service_charge_per_day":150,"nurse_service_status":1},{"id":23,"hospital_id":2,"name":"欧希曦","star_level":4,"age":"39","hometown":"海南","nursing_exp":3,"nursing_level":2,"service_charge_per_day":180,"nurse_service_status":0},{"id":24,"hospital_id":3,"name":"周宪旺","star_level":3,"age":"48","hometown":"台湾","nursing_exp":4,"nursing_level":3,"service_charge_per_day":200,"nurse_service_status":1},{"id":25,"hospital_id":1,"name":"陶淳庆","star_level":4,"age":"47","hometown":"香港","nursing_exp":5,"nursing_level":0,"service_charge_per_day":120,"nurse_service_status":0},{"id":26,"hospital_id":2,"name":"夏岩鸿","star_level":3,"age":"25","hometown":"福建","nursing_exp":6,"nursing_level":1,"service_charge_per_day":150,"nurse_service_status":1},{"id":27,"hospital_id":3,"name":"陈言心","star_level":5,"age":"36","hometown":"西藏","nursing_exp":7,"nursing_level":2,"service_charge_per_day":180,"nurse_service_status":0},{"id":28,"hospital_id":1,"name":"褚研春","star_level":4,"age":"34","hometown":"新疆","nursing_exp":8,"nursing_level":3,"service_charge_per_day":200,"nurse_service_status":1},{"id":29,"hospital_id":2,"name":"洪瑶希","star_level":3,"age":"39","hometown":"四川","nursing_exp":2,"nursing_level":0,"service_charge_per_day":120,"nurse_service_status":0},{"id":30,"hospital_id":3,"name":"庄龙启","star_level":5,"age":"27","hometown":"重庆","nursing_exp":3,"nursing_level":1,"service_charge_per_day":150,"nurse_service_status":1}], "Version":1}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def nurse_senior_list(request):
    import json

    request.get_full_path()
    response_data = {"type":"nurse_senior_list","nurse_senior_list":[{"id":1,"job_num":5112,"language_level":"普通话良好","education":"初中及以下","nation":"回族","intro":"本人性格温和和责任心强，善于跟老人沟通，擅长护理呼吸不畅疾病患者。能够使用普通话进行交流","departments":"呼吸科","certificate":"健康证","service_content":"负责患者日常生活护理，保持患者身体及床单位卫生清洁,帮助患者打饭及陪患者散步等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6,7_11,12,13,14,15,16,17_25,26,27,28,29,30"},{"month":"8"},{"days":"1,2,3_9,10,11,12,13_26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12_29,30"}]}},{"id":2,"job_num":5113,"language_level":"普通话一般","education":"初中及以下","nation":"回族","intro":"本人性格热情开朗，待人友好为人诚实谦虚。工作勤奋认真负责能是苦耐劳，尽职尽责有耐心。","departments":"神内科","certificate":"健康证","service_content":"包括初级护理的所有服务内容，及帮助患者翻身，扣背，防止患者身体长褥疮，观察患者病情变化等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5_17,18,19,20,21,22,23,24,25_29,30"},{"month":"8"},{"days":"1,2,3_16,17,18,19,20,21,22,23,24_30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9"}]}},{"id":3,"job_num":5114,"language_level":"普通话熟练","education":"初中及以下","nation":"回族","intro":"为人善良，能吃苦。","departments":"骨外科","certificate":"健康证","service_content":"包括中级护理的所有服务内容，懂得ICU及危重、特殊病人的看护；协助患者进行简单康复锻炼等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5_19,20,21,22,23,24,25,26_29,30"},{"month":"8"},{"days":"1,2,3,4,5,6_28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8"}]}},{"id":4,"job_num":5115,"language_level":"普通话良好","education":"初中及以下","nation":"回族","intro":"为人老实能吃苦工作细心。会使用普通话进行交流。","departments":"神外科","certificate":"健康证","service_content":"包括高级护理的所有服务内容，安抚病人情绪、为病人做心理辅导等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"12,13,14,15,16,17,18_28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7_18,19,20,21,22,23,24_30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16"}]}},{"id":5,"job_num":5116,"language_level":"普通话一般","education":"初中及以下","nation":"回族","intro":"本人做事细心，为人随和态度认真，开朗活泼吃苦耐劳，会使用普通话进行交流。","departments":"呼吸科","certificate":"健康证","service_content":"负责患者日常生活护理，保持患者身体及床单位卫生清洁,帮助患者打饭及陪患者散步等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2_21,22,23,24_28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8,9,10,11_25,26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10_26,27,28,29,30"}]}},{"id":6,"job_num":5117,"language_level":"普通话熟练","education":"初中及以下","nation":"汉族","intro":"本人有爱心、细心、责任心，对工作认真负责，积极进取，照顾病人细心认真。","departments":"神内科","certificate":"健康证","service_content":"包括初级护理的所有服务内容，及帮助患者翻身，扣背，防止患者身体长褥疮，观察患者病情变化等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6"},{"month":"8"},{"days":"16,17,18,19,20,21,22,23,24,25"}]}},{"id":7,"job_num":5118,"language_level":"普通话良好","education":"初中及以下","nation":"汉族","intro":"我是东北辽宁人，擅长与人交流，工作认真心细。","departments":"骨外科","certificate":"健康证","service_content":"包括中级护理的所有服务内容，懂得ICU及危重、特殊病人的看护；协助患者进行简单康复锻炼等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"18,19,20,21,22,23,24,25,26,27,28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8_28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9_27,28,29,30"}]}},{"id":8,"job_num":5119,"language_level":"普通话一般","education":"初中及以下","nation":"汉族","intro":"本人性格温和和责任心强，善于跟老人沟通，擅长护理呼吸不畅疾病患者。能够使用普通话进行交流","departments":"神外科","certificate":"健康证","service_content":"包括高级护理的所有服务内容，安抚病人情绪、为病人做心理辅导等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8,9_25,26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11_23,24,25,26,27,28,29,30"}]}},{"id":9,"job_num":5120,"language_level":"普通话熟练","education":"初中及以下","nation":"汉族","intro":"本人性格热情开朗，待人友好为人诚实谦虚。工作勤奋认真负责能是苦耐劳，尽职尽责有耐心。","departments":"呼吸科","certificate":"健康证","service_content":"负责患者日常生活护理，保持患者身体及床单位卫生清洁,帮助患者打饭及陪患者散步等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6,7_25,26,27,28,29,30"},{"month":"8"},{"days":"18,19,20,21,22,23,24,25"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,_28,29,30"}]}},{"id":10,"job_num":5121,"language_level":"普通话良好","education":"初中及以下","nation":"汉族","intro":"为人善良，能吃苦。","departments":"神内科","certificate":"健康证","service_content":"包括初级护理的所有服务内容，及帮助患者翻身，扣背，防止患者身体长褥疮，观察患者病情变化等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6_22,23,24,25,26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9_28,29,30"}]}},{"id":11,"job_num":5122,"language_level":"普通话一般","education":"初中及以下","nation":"汉族","intro":"为人老实能吃苦工作细心。会使用普通话进行交流。","departments":"骨外科","certificate":"健康证","service_content":"包括中级护理的所有服务内容，懂得ICU及危重、特殊病人的看护；协助患者进行简单康复锻炼等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3_29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8,9_16,17,18,19,20,21,22,23,24,25,26,27,28,29,30"},{"month":"9"},{"days":"1,2_14,15,16,17_28,29,30"}]}},{"id":12,"job_num":5123,"language_level":"普通话熟练","education":"初中及以下","nation":"汉族","intro":"本人做事细心，为人随和态度认真，开朗活泼吃苦耐劳，会使用普通话进行交流。","departments":"神外科","certificate":"健康证","service_content":"包括高级护理的所有服务内容，安抚病人情绪、为病人做心理辅导等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4_12,13,14,15,16,17,18,19,20,21,22,_30"},{"month":"8"},{"days":"1,2,3,4,5,6,7_17,18,19,20,21,22_29,30"},{"month":"9"},{"days":"1,2,3,4_16,17,18,19,20,21,22_29,30"}]}},{"id":13,"job_num":5124,"language_level":"普通话良好","education":"初中及以下","nation":"汉族","intro":"本人有爱心、细心、责任心，对工作认真负责，积极进取，照顾病人细心认真。","departments":"呼吸科","certificate":"健康证","service_content":"负责患者日常生活护理，保持患者身体及床单位卫生清洁,帮助患者打饭及陪患者散步等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"6,7,8,9,10_22,23,24,25,26,27,28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8,9,10_20,21,22,23_30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12,13"}]}},{"id":14,"job_num":5125,"language_level":"普通话一般","education":"初中及以下","nation":"汉族","intro":"我是东北辽宁人，擅长与人交流，工作认真心细。","departments":"神内科","certificate":"健康证","service_content":"包括初级护理的所有服务内容，及帮助患者翻身，扣背，防止患者身体长褥疮，观察患者病情变化等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2_22,23,24,25,26,27,28,29,30"},{"month":"8"},{"days":"20,21,22,23,24,25,26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11"}]}},{"id":15,"job_num":5126,"language_level":"普通话熟练","education":"初中及以下","nation":"汉族","intro":"本人性格温和和责任心强，善于跟老人沟通，擅长护理呼吸不畅疾病患者。能够使用普通话进行交流","departments":"骨外科","certificate":"健康证","service_content":"包括中级护理的所有服务内容，懂得ICU及危重、特殊病人的看护；协助患者进行简单康复锻炼等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30"}]}},{"id":16,"job_num":5127,"language_level":"普通话良好","education":"初中及以下","nation":"汉族","intro":"本人性格热情开朗，待人友好为人诚实谦虚。工作勤奋认真负责能是苦耐劳，尽职尽责有耐心。","departments":"神外科","certificate":"健康证","service_content":"包括高级护理的所有服务内容，安抚病人情绪、为病人做心理辅导等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6,7_11,12,13,14,15,16,17_25,26,27,28,29,30"},{"month":"8"},{"days":"1,2,3_9,10,11,12,13_26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12_29,30"}]}},{"id":17,"job_num":5128,"language_level":"普通话一般","education":"初中及以下","nation":"满族","intro":"为人善良，能吃苦。","departments":"呼吸科","certificate":"健康证","service_content":"负责患者日常生活护理，保持患者身体及床单位卫生清洁,帮助患者打饭及陪患者散步等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5_17,18,19,20,21,22,23,24,25_29,30"},{"month":"8"},{"days":"1,2,3_16,17,18,19,20,21,22,23,24_30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9"}]}},{"id":18,"job_num":5129,"language_level":"普通话熟练","education":"初中及以下","nation":"满族","intro":"为人老实能吃苦工作细心。会使用普通话进行交流。","departments":"神内科","certificate":"健康证","service_content":"包括初级护理的所有服务内容，及帮助患者翻身，扣背，防止患者身体长褥疮，观察患者病情变化等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5_19,20,21,22,23,24,25,26_29,30"},{"month":"8"},{"days":"1,2,3,4,5,6_28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8"}]}},{"id":19,"job_num":5130,"language_level":"普通话良好","education":"初中及以下","nation":"满族","intro":"本人做事细心，为人随和态度认真，开朗活泼吃苦耐劳，会使用普通话进行交流。","departments":"骨外科","certificate":"健康证","service_content":"包括中级护理的所有服务内容，懂得ICU及危重、特殊病人的看护；协助患者进行简单康复锻炼等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"12,13,14,15,16,17,18_28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7_18,19,20,21,22,23,24_30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16"}]}},{"id":20,"job_num":5131,"language_level":"普通话一般","education":"初中及以下","nation":"汉族","intro":"本人有爱心、细心、责任心，对工作认真负责，积极进取，照顾病人细心认真。","departments":"神外科","certificate":"健康证","service_content":"包括高级护理的所有服务内容，安抚病人情绪、为病人做心理辅导等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2_21,22,23,24_28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8,9,10,11_25,26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10_26,27,28,29,30"}]}},{"id":21,"job_num":5132,"language_level":"普通话熟练","education":"初中及以下","nation":"汉族","intro":"我是东北辽宁人，擅长与人交流，工作认真心细。","departments":"呼吸科","certificate":"健康证","service_content":"负责患者日常生活护理，保持患者身体及床单位卫生清洁,帮助患者打饭及陪患者散步等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6"},{"month":"8"},{"days":"16,17,18,19,20,21,22,23,24,25"}]}},{"id":22,"job_num":5133,"language_level":"普通话良好","education":"高中","nation":"汉族","intro":"本人性格温和和责任心强，善于跟老人沟通，擅长护理呼吸不畅疾病患者。能够使用普通话进行交流","departments":"神内科","certificate":"健康证","service_content":"包括初级护理的所有服务内容，及帮助患者翻身，扣背，防止患者身体长褥疮，观察患者病情变化等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"18,19,20,21,22,23,24,25,26,27,28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8_28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9_27,28,29,30"}]}},{"id":23,"job_num":5134,"language_level":"普通话一般","education":"高中","nation":"汉族","intro":"本人性格热情开朗，待人友好为人诚实谦虚。工作勤奋认真负责能是苦耐劳，尽职尽责有耐心。","departments":"骨外科","certificate":"健康证","service_content":"包括中级护理的所有服务内容，懂得ICU及危重、特殊病人的看护；协助患者进行简单康复锻炼等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8,9_25,26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11_23,24,25,26,27,28,29,30"}]}},{"id":24,"job_num":5135,"language_level":"普通话熟练","education":"高中","nation":"汉族","intro":"为人善良，能吃苦。","departments":"神外科","certificate":"健康证","service_content":"包括高级护理的所有服务内容，安抚病人情绪、为病人做心理辅导等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6,7_25,26,27,28,29,30"},{"month":"8"},{"days":"18,19,20,21,22,23,24,25"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,_28,29,30"}]}},{"id":25,"job_num":5136,"language_level":"普通话良好","education":"高中","nation":"汉族","intro":"为人老实能吃苦工作细心。会使用普通话进行交流。","departments":"呼吸科","certificate":"健康证","service_content":"负责患者日常生活护理，保持患者身体及床单位卫生清洁,帮助患者打饭及陪患者散步等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6_22,23,24,25,26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9_28,29,30"}]}},{"id":26,"job_num":5137,"language_level":"普通话一般","education":"高中","nation":"汉族","intro":"本人做事细心，为人随和态度认真，开朗活泼吃苦耐劳，会使用普通话进行交流。","departments":"神内科","certificate":"健康证","service_content":"包括初级护理的所有服务内容，及帮助患者翻身，扣背，防止患者身体长褥疮，观察患者病情变化等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3_29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8,9_16,17,18,19,20,21,22,23,24,25,26,27,28,29,30"},{"month":"9"},{"days":"1,2_14,15,16,17_28,29,30"}]}},{"id":27,"job_num":5138,"language_level":"普通话熟练","education":"高中","nation":"汉族","intro":"本人有爱心、细心、责任心，对工作认真负责，积极进取，照顾病人细心认真。","departments":"骨外科","certificate":"健康证","service_content":"包括中级护理的所有服务内容，懂得ICU及危重、特殊病人的看护；协助患者进行简单康复锻炼等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4_12,13,14,15,16,17,18,19,20,21,22,_30"},{"month":"8"},{"days":"1,2,3,4,5,6,7_17,18,19,20,21,22_29,30"},{"month":"9"},{"days":"1,2,3,4_16,17,18,19,20,21,22_29,30"}]}},{"id":28,"job_num":5139,"language_level":"普通话良好","education":"高中","nation":"汉族","intro":"我是东北辽宁人，擅长与人交流，工作认真心细。","departments":"神外科","certificate":"健康证","service_content":"包括高级护理的所有服务内容，安抚病人情绪、为病人做心理辅导等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"6,7,8,9,10_22,23,24,25,26,27,28,29,30"},{"month":"8"},{"days":"1,2,3,4,5,6,7,8,9,10_20,21,22,23_30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12,13"}]}},{"id":29,"job_num":5140,"language_level":"普通话一般","education":"高中","nation":"汉族","intro":"本人性格温和和责任心强，善于跟老人沟通，擅长护理呼吸不畅疾病患者。能够使用普通话进行交流","departments":"呼吸科","certificate":"健康证","service_content":"负责患者日常生活护理，保持患者身体及床单位卫生清洁,帮助患者打饭及陪患者散步等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2_22,23,24,25,26,27,28,29,30"},{"month":"8"},{"days":"20,21,22,23,24,25,26,27,28,29,30"},{"month":"9"},{"days":"1,2,3,4,5,6,7,8,9,10,11"}]}},{"id":30,"job_num":5141,"language_level":"普通话熟练","education":"高中","nation":"汉族","intro":"本人性格热情开朗，待人友好为人诚实谦虚。工作勤奋认真负责能是苦耐劳，尽职尽责有耐心。","departments":"神内科","certificate":"健康证","service_content":"包括初级护理的所有服务内容，及帮助患者翻身，扣背，防止患者身体长褥疮，观察患者病情变化等","nurse_shedule_list":{"nurse_shedule_list":[{"month":"7"},{"days":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30"}]}}], "Version":1}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def goods_basics_list(request):
    import json

    request.get_full_path()
    response_data = {"type":"goods_basics_list","goods_basics_list":[{"id":1,"name":"包邮家用康复器材脑瘫滚筒棍桶滚桶中风偏瘫康复训练康复用品","price":22,"praise_rate":"28","evaluation_times":123},{"id":2,"name":"雅德正品残疾人铝合金助行器 折叠老人四脚助步器用品康复器械","price":40,"praise_rate":"31","evaluation_times":456},{"id":3,"name":"楔形垫 三角垫 康复器材脑瘫用品平衡疗法康复训练体位垫","price":93,"praise_rate":"45","evaluation_times":789},{"id":4,"name":"包邮偏瘫脑瘫儿童医疗康复用品家用训练器材手指锻炼木塑料分指板","price":20,"praise_rate":"35","evaluation_times":963},{"id":5,"name":"中风偏瘫康复器材防褥疮气垫坐垫医用气垫瘫痪病人褥疮垫护理用品","price":17,"praise_rate":"59","evaluation_times":852},{"id":6,"name":"老人铁球健身手球 钢球实心保健球玉石中老年康复铁蛋子健身用品","price":49,"praise_rate":"34","evaluation_times":741},{"id":7,"name":"楔形垫 三角垫 脑瘫儿童康复器材 脑瘫用品 平衡疗法 康复训练体","price":168,"praise_rate":"36","evaluation_times":752},{"id":8,"name":"oper 手指矫形器 分指板 分指器 中风偏瘫手指康复训练器材 用品","price":93,"praise_rate":"45","evaluation_times":78},{"id":9,"name":"雅德正品老人铝合金助行器折叠残疾人四脚拐杖助步器用品康复器械","price":105,"praise_rate":"41","evaluation_times":21},{"id":10,"name":"15度30度45度楔形垫三角垫脑瘫用品 平衡疗法 康复用品训练体位垫","price":85,"praise_rate":"31","evaluation_times":854},{"id":11,"name":"可拆洗拉链式三角型防褥疮康复垫老人护理医用褥疮垫医疗器具用品","price":18,"praise_rate":"49","evaluation_times":132},{"id":12,"name":"雅德带坐垫残疾人铝合金助行器 折叠老人四脚助步器用品康复器械","price":138,"praise_rate":"38","evaluation_times":847},{"id":13,"name":"康复器材15度 楔形垫 三角垫脑瘫用 平衡疗法 康复用品训练体位垫","price":160,"praise_rate":"37","evaluation_times":312},{"id":14,"name":"褥疮垫手圈脚圈护理垫脚垫翻身垫踝骨垫卧床瘫痪病人康复护理用品","price":45,"praise_rate":"48","evaluation_times":112},{"id":15,"name":"老人拐杖用品残疾偏瘫康复专用拐杖手杖助行器拄拐棍可调节伸缩","price":12,"praise_rate":"42","evaluation_times":132},{"id":16,"name":"木质平衡板防滑 康复及训练平衡性平衡力感统训练高难度私教用品","price":43,"praise_rate":"40","evaluation_times":45},{"id":17,"name":"上下肢康复训练器材健身快车腿部锻炼脚踏车 青中老年人保健用品","price":13,"praise_rate":"30","evaluation_times":431},{"id":18,"name":"包邮 康复器材 脑瘫滚筒 棍桶 滚桶 中风偏瘫康复训练 康复用品","price":98,"praise_rate":"36","evaluation_times":312},{"id":19,"name":"老年人用品残疾偏瘫康复专用四角拐杖手杖助行器拄拐棍可调节伸缩","price":95,"praise_rate":"45","evaluation_times":102},{"id":20,"name":"医用踝关节支具脚踝矫正鞋矫形鞋足托足下垂矫形器矫正器康复用品","price":45,"praise_rate":"46","evaluation_times":20},{"id":21,"name":"包邮医用康复器材脑瘫滚筒棍桶滚桶中风偏瘫康复训练康复用品","price":28,"praise_rate":"35","evaluation_times":451},{"id":22,"name":"医用上肢垫/体位垫/护理垫/前臂垫/翻身垫/防褥疮垫康复用品","price":68,"praise_rate":"37","evaluation_times":46},{"id":23,"name":"雅德正品残疾人铝合金助行器 折叠老人四脚助步器用品康复器械","price":40,"praise_rate":"39","evaluation_times":485},{"id":24,"name":"包邮医用康复滚筒 偏瘫中风康复训练 脑瘫滚筒 康复用品训练器材","price":15,"praise_rate":"48","evaluation_times":312},{"id":25,"name":"15度30度45度楔形垫三角垫脑瘫用品 平衡疗法 康复用品训练体位垫","price":88,"praise_rate":"47","evaluation_times":12},{"id":26,"name":"雅德带坐垫残疾人铝合金助行器 折叠老人四脚助步器用品康复器械","price":65,"praise_rate":"25","evaluation_times":77},{"id":27,"name":"老年人用品助行器带轮可折叠调档残疾偏瘫辅助行走康复学步安全车","price":85,"praise_rate":"36","evaluation_times":54},{"id":28,"name":"正品医用卷式夹板 急救夹板 骨折固定板 可塑固定夹板 康复用品","price":75,"praise_rate":"34","evaluation_times":799},{"id":29,"name":"儿童脑瘫康复器材 手眼协调 手指精细活动早教用品益智拧螺丝包邮","price":29,"praise_rate":"39","evaluation_times":12},{"id":30,"name":"上下肢康复训练器材健身快车腿部锻炼脚踏车 青中老年人保健用品","price":33,"praise_rate":"27","evaluation_times":45}], "Version":1}
    return HttpResponse(json.dumps(response_data), content_type="application/json")