from get_canshu import get_address,get_money

def format(x):  #转换为对应状态
    if x=='集团' or x=='房屋补贴' or x=='现金' or x=='渠道' or x=='本省' or x=='销售佣金':
        return '1'
    elif x=='公众' or x=='装修费补贴' or x=='实物' or x=='发展人' or x=='沃商店基地' or x=='清欠佣金':
        return '2'
    elif x=='设施补贴' or x=='阅读基地' or x=='服务佣金':
        return '3'
    elif x=='宣传补贴' or x=='音乐基地' or x=='奖罚佣金':
        return '4'
    else:
        return '5'
def xml1(data):    #补录数据
    add=get_address(data[0],data[2])
    mon=get_money(data[0],data[6],data[2])
    xm1="<RootInfo><RowSet Name='TfChlSubsidy' FullName='com_ailk_uchannel_commmgr_web_set_TfChlSubsidy'  Sts='U'>" \
        "<Row Sts='N'><Col Name='CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>" \
        "<Col Name='CHNL_NAME' Sts= 'N'  ID ='"+add[0]+"' ></Col>" \
        "<Col Name='PAY_CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='PAY_CHNL_NAME' Sts= 'N'  ID ='"+add[1]+"' ></Col>"\
        "<Col Name='CUSTOMER_CODE' Sts= 'N'  ID ='0"+format(data[3])+"' >"+data[3]+"</Col>"\
        "<Col Name='USAGE_TYPE' Sts= 'N'  ID ='"+format(data[4])+"' >"+data[4]+"</Col>"\
        "<Col Name='SUBSIDY_TYPE' Sts= 'N'  ID ='"+format(data[5])+"' ></Col>"\
        "<Col Name='TOTAL_AMOUNT' Sts= 'N'  ID ='"+str(data[6])+"' ></Col>"\
        "<Col Name='AMOUNT' Sts= 'N'  ID ='"+mon[1]+"' ></Col>"\
        "<Col Name='VAT_TAX' Sts= 'N'  ID ='"+mon[0]+"' ></Col>"\
        "<Col Name='MEMO' Sts= 'N'  ID ='"+str(data[7])+"' ></Col></Row></RowSet></RootInfo>"
    return xm1

def xml2(data):   #补录数据
    add = get_address(data[0])
    xm2="<RootInfo><RowSet Name='TfChlManualFee' FullName='com_ailk_uchannel_commmgr_web_set_TfChlManualFee'  Sts='U'>"\
        "<Row Sts='N'>"\
        "<Col Name='CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='CHNL_NAME' Sts= 'N'  ID ='"+add[0]+"' ></Col>"\
        "<Col Name='SETT_CYCLE' Sts= 'N'  ID ='"+str(data[2])+"' ></Col>"\
        "<Col Name='PAY_OBJECT_NAME' Sts= 'N'  ID ='"+add[1]+"' ></Col>"\
        "<Col Name='PAY_OBJECT_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='AMOUNT' Sts= 'N'  ID ='0.00' ></Col>"\
        "<Col Name='VAT_TAX' Sts= 'N'  ID ='0.00' ></Col></Row></RowSet></RootInfo>"
    return xm2

def xml1_rg(data):  #rg人工录入数据
    xm1rg="<RootInfo><RowSet Name='TfChlSubsidy' FullName='com_ailk_uchannel_commmgr_web_set_TfChlSubsidy'  Sts='U'>"\
        "<Row Sts='N'>"\
        "<Col Name='CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='CHNL_NAME' Sts= 'N'  ID ='"+data[1]+"' ></Col>"\
        "<Col Name='PAY_CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='PAY_CHNL_NAME' Sts= 'N'  ID ='"+data[1]+"' ></Col>"\
        "<Col Name='SUBSIDY_TYPE' Sts= 'N'  ID ='2' ></Col><Col Name='TOTAL_AMOUNT' Sts= 'N'  ID ='0.00' ></Col>"\
        "</Row></RowSet></RootInfo>"
    return xm1rg
def xml2_rg(data):  #rg人工录入数据
    addr = get_address(data[0],data[2])
    money = get_money(data[0], data[7], data[2])
    xm2rg="<RootInfo><RowSet Name='TfChlManualFee' FullName='com_ailk_uchannel_commmgr_web_set_TfChlManualFee'  Sts='U'>"\
        "<Row Sts='N'>"\
        "<Col Name='CHNL_ID' Sts= 'N'  ID ='"+data[0]+"' ></Col>"\
        "<Col Name='CHNL_NAME' Sts= 'N'  ID ='"+addr[0]+"' ></Col>"\
        "<Col Name='SETT_CYCLE' Sts= 'N'  ID ='"+str(data[2])+"' ></Col>"\
        "<Col Name='CUSTOMER_CODE' Sts= 'N'  ID ='0"+format(data[3])+"' >"+data[3]+"</Col>"\
        "<Col Name='PAY_OBJECT_TYPE' Sts= 'N'  ID ='0"+format(data[4])+"' ></Col>"\
        "<Col Name='COST_ATTR' Sts= 'N'  ID ='99999999' >"+data[5]+"</Col>"\
        "<Col Name='PAY_OBJECT_NAME' Sts= 'N'  ID ='"+addr[1]+"' ></Col>"\
        "<Col Name='PAY_OBJECT_ID' Sts= 'N'  ID ='"+str(data[0])+"' ></Col>"\
        "<Col Name='COMM_TYPE' Sts= 'N'  ID ='0"+format(data[6])+"' >"+data[6]+"</Col>"\
        "<Col Name='TOTAL_AMOUNT' Sts= 'N'  ID ='"+str(data[7])+"' ></Col>"\
        "<Col Name='AMOUNT' Sts= 'N'  ID ='"+money[1]+"' ></Col>"\
        "<Col Name='VAT_TAX' Sts= 'N'  ID ='"+money[0]+"' ></Col>"\
        "<Col Name='MEMO' Sts= 'N'  ID ='"+str(data[8])+"' ></Col>"\
        "</Row></RowSet></RootInfo>"
    return xm2rg