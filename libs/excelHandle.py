import datetime
import time
import datetime
import pytz

import os
import platform
import csv

def handle_report_data():
    platform_type = platform.platform()
    if platform_type.find('Windows') > -1:
        # 分隔符不要写死 -->待改进
        report_file = os.path.join(os.path.dirname(os.getcwd()), 'appreport\html\data\suites.csv')
        print(report_file)
    elif platform_type.find('Linux') > -1:
        report_file = os.path.join(os.path.dirname(os.getcwd()), 'appreport/html/data/suites.csv')
        print(report_file)

    parent_suite = []
    suite = []

    # #需要计算测试开始和结束时间
    # Start Time获取并转时间戳
    # start_time
    # end_time
    # duration = end_time - start_time
    data = {'tester': 'Selina', 'start_time': '2023-01-05 16:40:15', 'end_time': '2023-01-05 19:45:55', 'duration': '03:05:40', 'total_cases': 0,
            'total_passed': 0, 'total_failed': 0, 'total_errored': 0, 'passed_rate': 0,
            'module_data': {'test_cases.fwv.test_common.TestCommon': {'total': 0, 'passed': 0, 'failed': 0, 'errored': 0}}}

    module_data = {}

    with open(report_file, encoding="utf8") as f:
        csv_reader = csv.DictReader(f)
        # show the data
        for line in csv_reader:
            # print(f"{line['Parent Suite']}.{line['Suite']}.{line['Sub Suite']}  {line['Name']}  {line['Status']} {line['Duration in ms']}ms")
            module = f"{line['Parent Suite']}.{line['Suite']}.{line['Sub Suite']}"
            data['module_data'][module] = {'total': 0, 'passed': 0, 'failed': 0, 'errored': 0}
            # module_data[module] = {'total':0, 'passed': 0, 'failed': 0, 'errored': 0}
            if line['Status'] == 'passed':
                data['total_passed'] += 1
            elif line['Status'] == 'failed':
                data['total_failed'] += 1
            elif line['Status'] == 'error':
                data['total_errored'] += 1
            data['total_cases'] += 1

    data['passed_rate'] = '{:.2%}'.format(data['total_passed'] / data['total_cases'])

    with open(report_file, encoding="utf8") as f:
        csv_reader = csv.DictReader(f)
        for line in csv_reader:
            module = '{}.{}.{}'.format(line['Parent Suite'], line['Suite'], line['Sub Suite'])
            data['module_data'][module]['total'] += 1
            if line['Status'] == 'passed':
                data['module_data'][module]['passed'] += 1
            elif line['Status'] == 'failed':
                data['module_data'][module]['failed'] += 1
            elif line['Status'] == 'errored':
                data['module_data'][module]['errored'] += 1

    return data
