# coding:utf-8

import sys
import json

# jsonファイル読み込み
f = open(sys.argv[1], 'r')
# 文字列からdict型へ変換
json_dict = json.load(f)
print('json_dict:{}'.format(type(json_dict)))

# 追加する情報を入力
# 注意:python2:raw_input python3: input 
print('cluster名を入力してください。')
cluster = raw_input('>> ')

print('org名を入力してください。')
org = raw_input('>> ')

port_number = 20

print('以下で登録します。よろしいですか？')
print('---')
print('cluster:' + cluster)
print('org:' + org)
print('port_number(固定):' + str(port_number))
print('---')
if raw_input('(y/n) ') != 'y':
    sys.exit()

# TCP_ROUTING_ORG 追加
tcp_routing_org_dict = json.loads(json_dict["TCP_ROUTING_ORG"])
print(str(tcp_routing_org_dict))
tcp_routing_org_dict.append({
    u"cluster":unicode(cluster),
    u"org":unicode(org),
    u"port_number":unicode(20)
    })
print(tcp_routing_org_dict)

# 値更新
json_dict["TCP_ROUTING_ORG"] = json.dumps(tcp_routing_org_dict)

# ファイル更新
f = open(sys.argv[1], 'w')
json.dump(json_dict, f)