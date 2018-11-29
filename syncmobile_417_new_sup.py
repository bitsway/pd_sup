from random import randint
import urllib2
import calendar
import urllib
import time


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)
def deduct_months(sourcedate, months):
    month = sourcedate.month - 1 - months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)



#============================= Image Upload
def fileUploaderPrescription():
    import shutil
    filename = request.vars.upload.filename
    file = request.vars.upload.file
#    shutil.copyfileobj(file,open('C:/workspace/Dropbox/sabbir_acer/web2py/applications/welcome/uploads/'+filename,'wb'))
#     shutil.copyfileobj(file, open('/home/www-data/web2py/applications/mrepacme/static/prescription_pic/' + filename, 'wb'))
    shutil.copyfileobj(file, open('/home/www-data/web2py/applications/demo/static/prescription_pic/' + filename, 'wb'))
    return 'success'

def fileUploader_docVisit():
    import shutil
    filename = request.vars.upload.filename
    file = request.vars.upload.file
#    shutil.copyfileobj(file,open('C:/workspace/Dropbox/sabbir_acer/web2py/applications/welcome/uploads/'+filename,'wb'))
    shutil.copyfileobj(file, open('/home/www-data/web2py/applications/demo/static/docVisit_pic/' + filename, 'wb'))
    return 'success'


def fileUploaderProfile():
    import shutil
    filename = request.vars.upload.filename
    file = request.vars.upload.file

    #    Remove file start============
    import os
    myfile = "/home/www-data/web2py/applications/lscrmap/static/client_pic/" + filename

    # # if file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)

#    Remove file end============

#    shutil.copyfileobj(file,open('C:/workspace/Dropbox/sabbir_acer/web2py/applications/welcome/uploads/'+filename,'wb'))
    shutil.copyfileobj(file, open('/home/www-data/web2py/applications/lscrmap/static/client_pic/' + filename, 'wb'))
    return 'success'




#=============New Check User==============================

#================Shima Start===========


def check_user_pharma():
   
    randNumber = randint(1001, 9999)

    retStatus = ''

    cid = str(request.vars.cid).strip().upper()
    rep_id = str(request.vars.rep_id).strip().upper()

    password = str(request.vars.rep_pass).strip()
    synccode = str(request.vars.synccode).strip()

    compRow = db((db.sm_company_settings.cid == cid) & (db.sm_company_settings.status == 'ACTIVE')).select(db.sm_company_settings.cid, limitby=(0, 1))
   
    if not compRow:
        return 'FAILED<SYNCDATA>Invalid Company'
    else:
        
        repRow = db((db.sm_rep.cid == cid) & (db.sm_rep.rep_id == rep_id) & (db.sm_rep.password == password) & (db.sm_rep.status == 'ACTIVE')).select(db.sm_rep.id,db.sm_rep.rep_id, db.sm_rep.name, db.sm_rep.sync_count, db.sm_rep.first_sync_date, db.sm_rep.last_sync_date, db.sm_rep.user_type, db.sm_rep.depot_id, db.sm_rep.level_id, db.sm_rep.field2,db.sm_rep.sync_code, limitby=(0, 1))
#         return repRow
        if not repRow:
           retStatus = 'FAILED<SYNCDATA>Invalid Authorization 2'
           return retStatus
        else:

            rep_name = repRow[0].name
#             return rep_name
            lastSyncTIme=str(repRow[0].last_sync_date)
            

            sync_code = str(randNumber)
            sync_count = int(repRow[0].sync_count) + 1
            first_sync_date = repRow[0].first_sync_date
            user_type = repRow[0].user_type

            last_sync_date = str(repRow[0].last_sync_date)
            
            if len(str(lastSyncTIme))< 10 :
                last_sync_date = date_fixed
            if first_sync_date == None:
                first_sync_date = date_fixed
                
            else:
                datetimeFormat = '%Y-%m-%d %H:%M:%S' 

                timedelta = datetime.datetime.strptime(datetime_fixed, datetimeFormat) - datetime.datetime.strptime(last_sync_date,datetimeFormat)

                if (str(timedelta).find('day')!=-1):
                    pass
                else:
                    try:
                        timeDiff=str(timedelta).split(':')[0]
                        timeDiffMinute=str(timedelta).split(':')[1]
                        if int(timeDiff) > 0:
                            pass
                        elif ((int(timeDiff) == 0) & (int(timeDiffMinute) > 15)) :
                            pass
                        elif ((int(timeDiff) > 0) & (int(timeDiffMinute) > 15)) :
                            pass
                        else:
                            pass

                    except:
                        pass
            last_sync_date = date_fixed
            if first_sync_date == None:
                first_sync_date = date_fixed
                
            rep_update = repRow[0].update_record(sync_code=sync_code, first_sync_date=first_sync_date, last_sync_date=last_sync_date, sync_count=sync_count)

            if (user_type == 'sup'):
                
                companyStr=''
                comRow=db((db.sm_company.cid==cid)).select(db.sm_company.ALL, orderby=db.sm_company.id)
                    
                
                for rows in comRow:
                    companyName=str(rows.company_name).strip()
                    companyId=str(rows.company_id).strip()
                    
                    companyStr+=str(companyName)+'<fdfd>'+str(companyId)+'<rdrd>'
                       
                
                productStr=''
                productRow=db((db.sm_company_settings.cid==cid)).select(db.sm_company_settings.item_list_mobile, limitby=(0,1))
                
                
                for rows in productRow:
                    productName=str(rows.item_list_mobile).strip()
                    productStr+=str(productName)+'<fd>'
                       
                
                
                brandtStr=''
                brandRow=db((db.company_brand.cid==cid)).select(db.company_brand.brand_name,db.company_brand.company_name, orderby=db.company_brand.brand_name)
#                 return brandRow
                pastCompany=''
                sFlag=0
                for rows in brandRow:
                    brandName=str(rows.brand_name).strip()
                    company_name=str(rows.company_name).strip().upper()
                    if pastCompany!=company_name :
                        if sFlag==0 and pastCompany=='':
                            brandtStr=brandtStr+'<'+company_name+'>'
                        sFlag=1
                        if sFlag==1 and pastCompany!='':
                            brandtStr=brandtStr+'<rd>'+'<'+company_name+'>'
                    pastCompany=company_name
                    
                    brandtStr=brandtStr+str(brandName)+'<fd>'
#                 return brandtStr
                
                
                #=================shima2511 start===============
                
                
                repStr=''
                repareaList=[]
                repRows=db((db.sup_rep.cid==cid)  and (db.sup_rep.sup_id==rep_id)).select(db.sup_rep.rep_id,db.sup_rep.rep_name, orderby=db.sup_rep.rep_id)
#                 return repRows
                for repRow in repRows:
                    reps_id = repRow.rep_id
                    
                    reps_name = repRow.rep_name
                    repareaList.append(rep_id)
                    #repStr=''
#                     repStr+=str(reps_name)+'|'+str(reps_id)+'<rdrd>'
                    if repStr == '':
                        repStr = str(reps_name) + '|' + str(reps_id)
#                         repStr+=str(reps_name)+'|'+str(reps_id)
                    else:
                        repStr += '<rd>' + str(reps_name) + '|' + str(reps_id)
#                         repStr+=str(reps_name)+'|'+str(reps_id)+'<rdrd>'
                
                reqStr=''
                suprepStr=''
                reqareaList=[]
                sup_repId=db((db.sup_rep.cid==cid)  and (db.sup_rep.sup_id==rep_id)).select(db.sup_rep.rep_id,db.sup_rep.rep_name, orderby=db.sup_rep.rep_id)
#                 return sup_repId
                
                
#                 sup_repId=db((db.sup_rep.cid==cid)  and (db.sup_rep.sup_id==rep_id)).select(db.sup_rep.rep_id, orderby=db.sup_rep.id)
#                 return repRows
                for sup_rep in sup_repId:
                    sup_repId = sup_rep.rep_id   
                    sup_rep_name = sup_rep.rep_name 
                    suprepStr+=str(sup_rep_name)+'|'+str(sup_repId)+'<rdrd>'
#                     return suprepStr
#                     past_sl=''
#                     
#                     past_sl = 0
#                     reqRows=db((db.sm_requisition_new.cid==cid)  and (db.sm_requisition_new.req_by_id==sup_repId)).select(db.sm_requisition_new.ALL, orderby=db.sm_requisition_new.sl)
#                     
#                     if reqRows:
#                         past_sl = int(reqRows[0].sl)
#                         
#                     past_sl=past_sl + 1
# #                     return past_sl
#                     for reqRow in reqRows:
# #                         rep_sl=reqRow.sl
# #                         return rep_sl
#                         item_id = reqRow.item_id
#                         item_name = reqRow.item_name
#                         item_price = reqRow.item_price
#                         item_piece = reqRow.item_piece
#                         item_carton = reqRow.item_carton
#                         carton_info = reqRow.carton_info
# #                         reqareaList.append(item_id)
#                         #repStr=''
#                         reqStr+=str(item_name)+'<fdfd>'+str(item_id)+'<fdfd>'+str(item_price)+'<fdfd>'+str(item_price)+'<fdfd>'+str(item_piece)+'<fdfd>'+str(item_carton)+'<fdfd>'+str(carton_info)+'<rdrd>'+str(past_sl)+'<reqrepsl>'
                        
#                         return reqStr
#                         if reqStr == '':
#                             #repStr = str(reps_id) + '|' + str(reps_name)
#                             reqStr+=str(item_name)+'|'+str(item_id)
#                         else:
#                             #repStr += '<rd>' + str(reps_id) + '|' + str(reps_name)
#                             reqStr+='<rd>'+str(item_name)+'|'+str(item_id)
                #===========sup
                supStr=''
                supareaList=[]
                supRows=db((db.sup_rep.cid==cid)  and (db.sup_rep.sup_id==rep_id)).select(db.sup_rep.sup_id,db.sup_rep.sup_name, orderby=db.sup_rep.id)
#                 return supRows
                for supRow in supRows:
                    sup_id = supRow.sup_id
                    sup_name = supRow.sup_name
                    supareaList.append(rep_id)
                    if supStr == '':
                        supStr = str(sup_id) + '|' + str(sup_name)
                        
                    else:
                        supStr += '<rd>' + str(sup_id) + '|' + str(sup_name)
                        
#                 return repStr
#                 return brandtStr
#=================Shima start 17/10/20108===========
                marketStr = ''
                repareaList=[]
                marketRows = db((db.sm_rep_area.cid == cid) & (db.sm_rep_area.rep_id == rep_id)).select(db.sm_rep_area.area_id, db.sm_rep_area.area_name, orderby=db.sm_rep_area.area_name, groupby=db.sm_rep_area.area_id)
                
                for marketRow in marketRows:
                    area_id = marketRow.area_id
                    area_name = marketRow.area_name
                    repareaList.append(area_id)
                    if marketStr == '':
                        marketStr = str(area_id) + '<fd>' + str(area_name)
                        
                    else:
                        marketStr += '<rd>' + str(area_id) + '<fd>' + str(area_name)
                        
                        
                
                clienttCatStr = ''
                cliendepot_name=''


#                 ---------------------------------------------------------------------------------------
#                 ------------------------------Market Client List Start-----------------------------------------
                area_id=''
                clientStr = ''
                start_flag = 0
                client_depot=''
                for marketRow_1 in marketRows:
                    area_id = marketRow_1.area_id
                   

                    clientStr = clientStr + '<' + area_id + '>'
#                   
                    clientRows = db((db.sm_client.cid == cid) & (db.sm_client.area_id == area_id) & (db.sm_client.status == 'ACTIVE')).select(db.sm_client.ALL, orderby=~db.sm_client.id)

#                     return clientRows
                    if not clientRows:
                        clientStr = clientStr + 'Retailer not available' + '</' + area_id + '>'
#                         return retStatus
                    else:
                        client_depot=''
                        cliendepot_name=''
                        for clientRow in clientRows:
                            client_id = clientRow.client_id
                            name = clientRow.name
                            market_ad = clientRow.market_ad
                            union_ad = clientRow.union_ad
                            upazila = clientRow.upazila
                            district = clientRow.district
                            owner_name = clientRow.owner_name
                            contact_no1 = clientRow.contact_no1
                            category_id = clientRow.category_id
                            category_name = clientRow.category_name
                            market_id = clientRow.market_id
                            photo = clientRow.photo

                            if start_flag == 0:
                                
                                clientStr = clientStr + str(client_id) +'<fd>'+ str(name)+'<fd>'+str(market_ad)+'<fd>'+str(union_ad)+'<fd>' + str(upazila) + '<fd>' + str(district) + '<fd>' + str(owner_name)+ '<fd>' + str(contact_no1)+ '<fd>' + str(category_id)+ '<fd>' + str(category_name)+ '<fd>' + str(market_id)+ '<fd>' + str(photo).strip().upper()
                                start_flag = 1
                            else:
                                clientStr = clientStr + '<rd>' + str(client_id) +'<fd>'+ str(name)+'<fd>'+str(market_ad)+'<fd>'+str(union_ad)+'<fd>' + str(upazila) + '<fd>' + str(district) + '<fd>' + str(owner_name)+ '<fd>' + str(contact_no1)+ '<fd>' + str(category_id)+ '<fd>' + str(category_name)+ '<fd>' + str(market_id)+ '<fd>' + str(photo).strip().upper()
                
                    clientStr = clientStr + '</' + area_id + '>'
#                     return clientStr
                clientCatStr = ''
                clientCatRows = db((db.sm_category_type.cid == cid) & (db.sm_category_type.type_name == 'CLIENT_CATEGORY')).select(db.sm_category_type.cat_type_id,db.sm_category_type.cat_type_name, orderby=db.sm_category_type.cat_type_id)
                for clientCat in clientCatRows:
                    cat_type_id = clientCat.cat_type_id
                    cat_type_name=clientCat.cat_type_name
                    if clientCatStr == '':
                        clientCatStr = cat_type_id + '<fd>' + cat_type_name
                    else:
                        clientCatStr += '<rd>' + cat_type_id+'<fd>' + cat_type_name
                
                clientSubCatStr = ''
                clientSubCatRows = db((db.sm_category_type.cid == cid) & (db.sm_category_type.type_name == 'CLIENT_SUB_CATEGORY')).select(db.sm_category_type.cat_type_id,db.sm_category_type.cat_type_name, orderby=db.sm_category_type.cat_type_id)
#                 return clientSubCatRows
                for clientSubCat in clientSubCatRows:
                    sub_cat_type_id = clientSubCat.cat_type_id
                    sub_cat_type_name = clientSubCat.cat_type_name
                    if clientSubCatStr == '':
                        clientSubCatStr = sub_cat_type_id + '<fd>' + sub_cat_type_name
                    else:
                        clientSubCatStr += '<rd>' + sub_cat_type_id+'<fd>' + sub_cat_type_name
                
                companyStr=companyStr.replace("'","")
                productStr=productStr.replace("'","")
                marketStr=marketStr.replace("'","")
                clientStr =clientStr.replace("'","")
                clientCatStr =clientCatStr.replace("'","")
                clientSubCatStr =clientSubCatStr.replace("'","")
                brandtStr =brandtStr.replace("'","")
                repStr =repStr.replace("'","")
                supStr=supStr.replace("'","")
                reqStr=reqStr.replace("'","")
                suprepStr=suprepStr.replace("'","")
                reqStr=''
                return 'SUCCESS<SYNCDATA>' + str(sync_code) + '<SYNCDATA>'+ user_type +'<SYNCDATA>'+companyStr+'<SYNCDATA>'+productStr+'<SYNCDATA>'+rep_name +'<SYNCDATA>'+marketStr +'<SYNCDATA>'+clientStr+'<SYNCDATA>'+clientCatStr+'<SYNCDATA>'+clientSubCatStr+'<SYNCDATA>'+brandtStr+'<SYNCDATA>'+repStr+'<SYNCDATA>'+supStr+'<SYNCDATA>'+reqStr+'<SYNCDATA>'+suprepStr
            
            else:
                return 'FAILED<SYNCDATA>Invalid Authorization'
# =================ReqList
def reqList():
    cid = str(request.vars.cid).strip().upper()
    rep_id = str(request.vars.rep_id).strip().upper()#sup id
    synccode = str(request.vars.synccode).strip()
    password=  str(request.vars.rep_pass).strip()
    sup_repId= str(request.vars.repId).strip().split('|')[1]
   
#     sup_repd = sup_rep.rep_id 
#     return sup_repId
    repRow = db((db.sm_rep.cid == cid) & (db.sm_rep.rep_id == rep_id) & (db.sm_rep.password == password) & (db.sm_rep.status == 'ACTIVE')).select(db.sm_rep.id,db.sm_rep.rep_id, db.sm_rep.name, db.sm_rep.sync_count, db.sm_rep.first_sync_date, db.sm_rep.last_sync_date, db.sm_rep.user_type, db.sm_rep.depot_id, db.sm_rep.level_id, db.sm_rep.field2,db.sm_rep.sync_code, limitby=(0, 1))
    reqStr=''
    if not repRow:
       retStatus = 'FAILED<SYNCDATA>Invalid Authorization 2'
       return retStatus
    else:
        past_sl=''
         
        
        reqRows=db((db.sm_requisition_new.cid==cid)  and (db.sm_requisition_new.req_by_id==sup_repId)).select(db.sm_requisition_new.ALL, orderby=db.sm_requisition_new.sl)
#         return past_sl
        for reqRow in reqRows:
            sl=reqRow.sl
            item_id = reqRow.item_id
            item_name = reqRow.item_name
            item_price = reqRow.item_price
            item_piece = reqRow.item_piece
            item_carton = reqRow.item_carton
            carton_info = reqRow.carton_info
            status = reqRow.field1
#             return past_sl
            if past_sl!=sl:
                reqStr=reqStr+'<recSep>'
                
            reqStr=reqStr+str(sl)+'<fdfd>'+str(item_name)+'<fdfd>'+str(item_id)+'<fdfd>'+str(item_price)+'<fdfd>'+str(item_piece)+'<fdfd>'+str(item_carton)+'<fdfd>'+str(carton_info)+'<fdfd>'+str(status)+'<rdrd>'
            past_sl= sl




        return 'SUCCESS<SYNCDATA>' + str(reqStr) 
        
#         else:
#             return 'FAILED<SYNCDATA>Invalid Authorization'




def approvReq():
    cid = str(request.vars.cid).strip().upper()
    rep_id = str(request.vars.rep_id).strip().upper()#sup id
    synccode = str(request.vars.synccode).strip()
    password=  str(request.vars.rep_pass).strip()
    reqsl= str(request.vars.reqsl).strip()
    
    settings_update=db((db.sm_requisition_new.cid == cid) & (db.sm_requisition_new.sl == reqsl)).update(field1='APPROVED')
    
    settings_update=db((db. sm_requisition_head_new.cid == cid) & (db. sm_requisition_head_new.sl == reqsl)).update(field1='APPROVED')
    
    return 'SUCCESS<SYNCDATA>Approved Successfully'
            

def cancelReq():
    cid = str(request.vars.cid).strip().upper()
    rep_id = str(request.vars.rep_id).strip().upper()#sup id
    synccode = str(request.vars.synccode).strip()
    password=  str(request.vars.rep_pass).strip()
    reqsl= str(request.vars.reqsl).strip()
     
    settings_update=db((db.sm_requisition_new.cid == cid) & (db.sm_requisition_new.sl == reqsl)).update(field1='CANCELLED')
     
    settings_update=db((db. sm_requisition_head_new.cid == cid) & (db. sm_requisition_head_new.sl == reqsl)).update(field1='CANCELLED')
     
    return 'SUCCESS<SYNCDATA>Cancelled Successfully'
             

#=================Shima end 17/10/20108===========
def dataSubmit():
    
    cid = str(request.vars.cid).strip().upper()
    rep_id = str(request.vars.rep_id).strip().upper()#sup id
    synccode = str(request.vars.synccode).strip()
    password=  str(request.vars.password).strip()
    prouct_string=str(request.vars.prouct_string)
    comp_Id=str(request.vars.comp_Id).strip()
    comp_name=str(request.vars.comp_name).strip().upper()
    rep_name=str(request.vars.rep_name).strip().upper()#sup name
    reps_id=str(request.vars.rep_list).strip()
#     return reps_id
    reps_id=str(request.vars.rep_list).split('|')[0].strip()#combo rep id
    reps_name=str(request.vars.rep_list).split('|')[1].strip()#combo rep name
    
    latitude=str(request.vars.latitude).strip()
    longitude=str(request.vars.longitude).strip()
    date=str(request.vars.date).strip()
    
    
    import time
    compRow = db((db.sm_company_settings.cid == cid) & (db.sm_company_settings.status == 'ACTIVE')).select(db.sm_company_settings.cid, limitby=(0, 1))
    
    if not compRow:
        return 'FAILED<SYNCDATA>Invalid Company'
    else:
        repRow = db((db.sm_rep.cid == cid) & (db.sm_rep.rep_id == rep_id) & (db.sm_rep.password == password) & (db.sm_rep.status == 'ACTIVE')).select(db.sm_rep.ALL, limitby=(0, 1))
#         return repRow
        if not repRow:
           retStatus = 'FAILED<SYNCDATA>Invalid Authorization'
           return retStatus
        else:
            order_sl = 0
            req_head_sl=db((db.sm_received_head_new.cid==cid)).select(db.sm_received_head_new.sl, orderby=~db.sm_received_head_new.sl, limitby=(0,1))
            if req_head_sl:
                order_sl = int(req_head_sl[0].sl)
                
            ordSl=order_sl + 1
            DataInsert=db.sm_received_head_new.insert(cid=cid,sl=ordSl,rep_by_id=reps_id,rep_by_name=reps_name,req_to_id=comp_Id,req_to_name=comp_name,received_by_id=rep_id,received_by_name=rep_name,received_date=date,latitude=latitude,longitude=longitude)
        
            prouct_stringList = prouct_string.split('<rd>');
         
            com_name=''
            pr_id=''
            pr_name=''
            pQty=''
            cQty=''
            cQty=''
            insFlag=0
            for i in range(len(prouct_stringList)-1):
                pr_list=prouct_stringList[i].split("<fd>")
                pr_id=pr_list[0]
                pQty=pr_list[1]
                cQty=pr_list[2]
                
                carton_info=pr_list[3]  
                price=pr_list[4]  
                d_price=pr_list[5]  
                
                DataInsert=db.sm_received_new.insert(cid=cid,sl=ordSl,rep_by_id=reps_id,rep_by_name=reps_name,req_to_id=comp_Id,req_to_name=comp_name,item_id=pr_id,item_price=price,item_piece=pQty,item_carton=cQty,carton_info=carton_info,d_price=d_price,received_by_id=rep_id,received_by_name=rep_name,received_date=date)
                insFlag=1
            if insFlag==1:
                return 'Success'
        
#     return DataInsert



#===================Check User End==========================

#=================Shima start 17/10/20108===========
def chemist_submit():
    cid = str(request.vars.cid).strip().upper()
    rep_id = str(request.vars.rep_id).strip().upper()
    password = str(request.vars.rep_pass).strip()
    synccode = str(request.vars.synccode).strip()
    market_id = str(request.vars.market_id).strip()
    
    latitude = str(request.vars.latitude).strip()
    longitude = str(request.vars.longitude).strip()
  
    ChemistName = str(request.vars.ChemistName).strip().decode("ascii", "ignore")
    #=================Shima start 22/10/20108===========
    market = str(request.vars.market).strip().decode("ascii", "ignore")
    union = str(request.vars.union).strip().decode("ascii", "ignore")
    
    upazila = str(request.vars.upazila).strip().decode("ascii", "ignore")
    district = str(request.vars.district).strip().decode("ascii", "ignore")
    
    category_id = str(request.vars.Category).split('|')[0].strip().decode("ascii", "ignore")
    category_name = str(request.vars.Category).split('|')[1].strip().decode("ascii", "ignore")
    
#=================Shima end 22/10/20108===========
    
#     Address_Line_1 = str(request.vars.Address_Line_1).strip().decode("ascii", "ignore")
    Category = str(request.vars.Category).strip().decode("ascii", "ignore")
    subCategory = str(request.vars.subCategory).strip().decode("ascii", "ignore")
    RegistrationNo = str(request.vars.RegistrationNo).strip().decode("ascii", "ignore")
    Contact_Name=str(request.vars.Contact_Name).strip().decode("ascii", "ignore")
    Contact_phone = str(request.vars.Contact_phone).strip().decode("ascii", "ignore")
    nid = str(request.vars.nid).strip().decode("ascii", "ignore")
    Credit_Limit = str(request.vars.Credit_Limit).strip().decode("ascii", "ignore")
    Cash_Credit = str(request.vars.Cash_Credit).strip().decode("ascii", "ignore")
    dob = str(request.vars.dob).strip().decode("ascii", "ignore")
    imageName = str(request.vars.imageName).strip().decode("ascii", "ignore")
    
    
    import time
    compRow = db((db.sm_company_settings.cid == cid) & (db.sm_company_settings.status == 'ACTIVE')).select(db.sm_company_settings.cid, limitby=(0, 1))
    
    if not compRow:
        return 'FAILED<SYNCDATA>Invalid Company'
    else:
        repRow = db((db.sm_rep.cid == cid) & (db.sm_rep.rep_id == rep_id) & (db.sm_rep.password == password) & (db.sm_rep.status == 'ACTIVE')).select(db.sm_rep.ALL, limitby=(0, 1))

        if not repRow:
           retStatus = 'FAILED<SYNCDATA>Invalid Authorization'
           return retStatus
        else:
            slRow= db((db.sm_settings_pharma.cid == cid) & (db.sm_settings_pharma.s_key == 'CHEMSL')).select(db.sm_settings_pharma.s_value,orderby=~db.sm_settings_pharma.s_value, limitby=(0, 1))

            clientId=0
            if slRow:
                clientId= int(slRow[0].s_value)
            maxClient_id=clientId+1
#             client_insert=db.sm_client.insert(cid=cid,client_id=maxClient_id,name=ChemistName,area_id=market_id,market_id=str(market_id),contact_no1= Contact_phone ,vat_registration_no=RegistrationNo , created_by= rep_id,  dob=dob,photo=imageName,address=Address_Line_1,nid=nid,owner_name=Contact_Name,category_name=Category,sub_category_name=subCategory,credit_limit=Credit_Limit,paytype=Cash_Credit,status='ACTIVE',latitude=latitude,longitude=longitude,district=district,upazila=upazila,union_ad=union,market_ad=market)
            client_insert=db.sm_client.insert(cid=cid,client_id=maxClient_id,name=ChemistName,area_id=market_id,market_id=str(market_id),contact_no1= Contact_phone ,vat_registration_no=RegistrationNo , created_by= rep_id,  dob=dob,photo=imageName,nid=nid,owner_name=Contact_Name,category_id=category_id,category_name=category_name,sub_category_name=subCategory,credit_limit=Credit_Limit,paytype=Cash_Credit,status='ACTIVE',latitude=latitude,longitude=longitude,district=district,upazila=upazila,union_ad=union,market_ad=market)            

            settings_update=db((db.sm_settings_pharma.cid == cid) & (db.sm_settings_pharma.s_key == 'CHEMSL')).update(s_value=str(maxClient_id))
            retStatus = 'SUCCESS<SYNCDATA>Submitted Successfully'
            
            
            return retStatus


#=================Shima start 17/10/20108===========


 
#=================Shima end 17/10/20108===========
 
#============================= Test dynamic path
def dmpath():
    
#     return '<start>http://127.0.0.1:8000/pd_sup/syncmobile_417_new/<fd>http://127.0.0.1:8000/pd/static/<fd>http://i001.yeapps.com/image_hub/skfahd_image/skfahd_image/<fd>http://127.0.0.1:8000/pd_sup/syncmobile_417_new/<end>'
    return '<start>http://w02.yeapps.com/pd/syncmobile_417_new_sup/<fd>http://w02.yeapps.com/pd/static/<fd>http://i001.yeapps.com/image_hub/skfahd_image/skfahd_image/<fd>http://w02.yeapps.com/pd/syncmobile_417_new_sup/<end>'
#     return '<start>http://127.0.0.1:8000/skfah/syncmobile_417_new/<fd>http://127.0.0.1:8000/skfah/static/<fd>http://i001.yeapps.com/image_hub/skfahd_image/skfahd_image/<fd>http://127.0.0.1:8000/skfah/syncmobile_417_new/<end>'
#     return '<start>http://w02.yeapps.com/ipi/syncmobile_417_new_ibn/<fd>http://e2.businesssolutionapps.com/mrepbiopharma/static/<fd>http://104.155.225.205/gpl_image/syncmobile_prescription/<fd>http://w02.yeapps.com/ipi/syncmobile_417_new_ibn/<end>'
# #     return '<start>http://a007.yeapps.com/acme/syncmobile_417_new/<fd>http://a007.yeapps.com/acme/static/<fd>http://a007.yeapps.com/acme/syncmobile_417_new/<fd>http://a007.yeapps.com/acme/syncmobile_417_new/<end>'
# #     return '<start>http://a007.yeapps.com/ipi/syncmobile_417_new/<fd>http://a007.yeapps.com/ipi/static/<fd>http://a007.yeapps.com/ipi/syncmobile_417_new/<fd>http://a007.yeapps.com/ipi/syncmobile_417_new/<end>'
#     return '<start>http://127.0.0.1:8000/demo/syncmobile_417_new_ibn/<fd>http://e2.businesssolutionapps.com/mrepbiopharma/static/<fd>http://104.155.225.205/gpl_image/syncmobile_prescription/<fd>http://127.0.0.1:8000/demo/syncmobile_417_new_ibn/<end>'
# #     return '<start>http://c003.cloudapp.net/demo/syncmobile_417_new/<fd>http://c003.cloudapp.net/demo/static/<fd>http://c003.cloudapp.net/demo/syncmobile_417_new/<fd>http://c003.cloudapp.net/demo/syncmobile_417_new/<end>'


