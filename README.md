# KingDee-filereading-exp
Unauthorized attackers can exploit this vulnerability to access arbitrary files on the server.

金蝶云星空是一款云端企业资源管理（ERP）软件，为企业提供财务管理、供应链管理以及业务流程管理等一体化解决方案。金蝶云·星空聚焦多组织，
多利润中心的大中型企业，以 “开放、标准、社交”三大特性为数字经济时代的企业提供开放的 ERP 云平台。服务涵盖：财务、供应链、智能制造、阿米巴管理、全渠道营销、电商、HR、企业互联网服务，帮助企业实现数字化营销新生态及管理重构等，提升企业数字化能力

由于金蝶云星空CommonFileServer接口处权限设置不当，未经身份认证的攻击者可以利用此漏洞访问服务器上的任意文件，包括数据库凭据、API密钥、配置文件等，从而获取系统权限和敏感信息。

python3 Kingdee.py -u url 

python3 Kingdee.py -f urls
![image](https://github.com/Despacito01/KingDee-filereading-exp/blob/main/START.png?raw=true)
