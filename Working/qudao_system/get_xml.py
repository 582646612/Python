from get_canshu import get_address,get_money
'''             
AMOUNT			调整应付净额
CHNL_ID			渠道编码
CHNL_NAME		发展渠道
COMM_TYPE		佣金类型
COST_ATTR		成本所属中心
CUSTOMER_CODE	客户类别
MEMO			调整依据
SETT_CYCLE		账期
SUBSIDY_TYPE   	补贴方式
TOTAL_AMOUNT	补贴参考总额
VAT_TAX			调整参考税额

'''#各字段对应名
def format(tr):  #转换为对应状态
    if tr == '房屋补贴' or tr == '房***' or tr == '集团' or  tr == '现金' or tr == '渠道' or tr == '销售佣金' or tr == '集客' :
        return '1'
    elif tr == '装修费补贴' or tr == '公众' or tr == '实物' or tr == '发展人' or tr == '清欠佣金':
        return '2'
    elif tr == '设施补贴' or tr == '服务佣金':
        return '3'
    elif tr == '宣传补贴' or tr == '奖罚佣金':
        return '4'
    elif tr == '其它一次性补贴' or tr == '维系佣金':
        return '5'
    elif tr == "本省":
        return '99999999'
    elif tr == '沃商店基地':
        return '0904325'
    elif tr == '阅读基地':
        return '0904324'
    elif tr == '音乐基地':
        return '0904323'

def xml1(data,addr,cooks):    #补录数据
    mon = get_money(data[0],data[8],data[4],cooks)
    xm1 = "<RootInfo><RowSet Name='TfChlSubsidy' FullName='com_ailk_uchannel_commmgr_web_set_TfChlSubsidy'  Sts='U'>" \
        "<Row Sts='N'><Col Name='CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>" \
        "<Col Name='CHNL_NAME' Sts= 'N'  ID ='"+addr[0]+"' ></Col>" \
        "<Col Name='PAY_CHNL_ID' Sts= 'N'  ID ='"+addr[2]+"' ></Col>"\
        "<Col Name='PAY_CHNL_NAME' Sts= 'N'  ID ='"+addr[1]+"' ></Col>"\
        "<Col Name='CUSTOMER_CODE' Sts= 'N'  ID ='0"+format(data[5])+"' >"+data[5]+"</Col>"\
        "<Col Name='USAGE_TYPE' Sts= 'N'  ID ='"+format(data[6])+"' >"+data[6]+"</Col>"\
        "<Col Name='SUBSIDY_TYPE' Sts= 'N'  ID ='"+format(data[7])+"' ></Col>"\
        "<Col Name='TOTAL_AMOUNT' Sts= 'N'  ID ='"+str(data[8])+"' ></Col>"\
        "<Col Name='AMOUNT' Sts= 'N'  ID ='"+mon[1]+"' ></Col>"\
        "<Col Name='VAT_TAX' Sts= 'N'  ID ='"+mon[0]+"' ></Col>"\
        "<Col Name='MEMO' Sts= 'N'  ID ='"+data[9]+"' ></Col></Row></RowSet></RootInfo>"
    return xm1

def xml2(data,addr):   #补录数据
    xm2 = "<RootInfo><RowSet Name='TfChlManualFee' FullName='com_ailk_uchannel_commmgr_web_set_TfChlManualFee'  Sts='U'>"\
        "<Row Sts='N'>"\
        "<Col Name='CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='CHNL_NAME' Sts= 'N'  ID ='"+addr[0]+"' ></Col>"\
        "<Col Name='SETT_CYCLE' Sts= 'N'  ID ='"+data[4]+"' ></Col>"\
        "<Col Name='PAY_OBJECT_NAME' Sts= 'N'  ID ='"+addr[1]+"' ></Col>"\
        "<Col Name='PAY_OBJECT_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='AMOUNT' Sts= 'N'  ID ='0.00' ></Col>"\
        "<Col Name='VAT_TAX' Sts= 'N'  ID ='0.00' ></Col></Row></RowSet></RootInfo>"
    return xm2

def xml1_rg(data,addr):  #rg人工录入数据r
    xm1rg = "<RootInfo><RowSet Name='TfChlSubsidy' FullName='com_ailk_uchannel_commmgr_web_set_TfChlSubsidy'  Sts='U'>"\
        "<Row Sts='N'>"\
        "<Col Name='CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='CHNL_NAME' Sts= 'N'  ID ='"+addr[0]+"' ></Col>"\
        "<Col Name='PAY_CHNL_ID' Sts= 'N'  ID ='"+addr[2]+"' ></Col>"\
        "<Col Name='PAY_CHNL_NAME' Sts= 'N'  ID ='"+addr[1]+"' ></Col>"\
        "<Col Name='SUBSIDY_TYPE' Sts= 'N'  ID ='2' ></Col>" \
        "<Col Name='TOTAL_AMOUNT' Sts= 'N'  ID ='0.00' ></Col>"\
        "</Row></RowSet></RootInfo>"
    return xm1rg
def xml2_rg(data,addr,cooks):  #rg人工录入数据
    money = get_money(data[0], data[7], data[2],cooks)
    xm2rg = "<RootInfo><RowSet Name='TfChlManualFee' FullName='com_ailk_uchannel_commmgr_web_set_TfChlManualFee'  Sts='U'>"\
        "<Row Sts='N'>"\
        "<Col Name='CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='CHNL_NAME' Sts= 'N'  ID ='"+addr[0]+"' ></Col>"\
        "<Col Name='SETT_CYCLE' Sts= 'N'  ID ='"+data[2]+"' ></Col>"\
        "<Col Name='CUSTOMER_CODE' Sts= 'N'  ID ='0"+format(data[3])+"' >"+data[3]+"</Col>"\
        "<Col Name='PAY_OBJECT_TYPE' Sts= 'N'  ID ='0"+format(data[4])+"' ></Col>"\
        "<Col Name='COST_ATTR' Sts= 'N'  ID ='"+format(data[5])+"' >"+data[5]+"</Col>"\
        "<Col Name='PAY_OBJECT_NAME' Sts= 'N'  ID ='"+addr[1]+"' ></Col>"\
        "<Col Name='PAY_OBJECT_ID' Sts= 'N'  ID ='"+addr[2]+"' ></Col>"\
        "<Col Name='COMM_TYPE' Sts= 'N'  ID ='0"+format(data[6])+"' >"+data[6]+"</Col>"\
        "<Col Name='TOTAL_AMOUNT' Sts= 'N'  ID ='"+str(data[7])+"' ></Col>"\
        "<Col Name='AMOUNT' Sts= 'N'  ID ='"+money[1]+"' ></Col>"\
        "<Col Name='VAT_TAX' Sts= 'N'  ID ='"+money[0]+"' ></Col>"\
        "<Col Name='MEMO' Sts= 'N'  ID ='"+data[8]+"' ></Col>"\
        "</Row></RowSet></RootInfo>"
    return xm2rg