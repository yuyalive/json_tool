<?php
// ファイル読み込み
$json = file_get_contents("./sample.json");
$json = mb_convert_encoding($json, 'UTF8', 'ASCII,JIS,UTF-8,EUC-JP,SJIS-WIN');
$arr = json_decode($json, true);
$tcp_routing_org = json_decode($arr["TCP_ROUTING_ORG"], true);
print_r($tcp_routing_org);
?>
