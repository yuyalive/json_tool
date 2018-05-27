# coding:utf-8

import sys
import platform
import json

# python2/3互換用input関数
def user_input(val):
    if platform.python_version_tuple()[0] == '2':
        return raw_input(val)
    else:
        return input(val)

# jsonファイル読み込み
f = open(sys.argv[1], 'r')
# jsonデコード
json_dict = json.load(f)

# 追加する情報を設定 
cluster = user_input('cluster名を入力してください >> ')
org = user_input('org名を入力してください >> ')
port_number = 20

print('以下で登録します。よろしいですか？')
print('---')
print('cluster:' + cluster)
print('org:' + org)
print('port_number(固定):' + str(port_number))
print('---')
if user_input('y/n >> ') != 'y':
    sys.exit()

# TCP_ROUTING_ORG 追加
tcp_routing_org = json.loads(json_dict["TCP_ROUTING_ORG"])
tcp_routing_org.append({"cluster":cluster,"org":org,"port_number":20})
json_dict["TCP_ROUTING_ORG"] = json.dumps(tcp_routing_org)

# ファイル更新
f = open(sys.argv[1], 'w')
json.dump(json_dict, f)