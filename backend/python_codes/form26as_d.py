# -*- coding: utf-8 -*-
"""Form26AS Digitization func1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xvspcvMcu17opGrdWUmcuE3VHQdhbw0r
"""

import pandas as pd
import numpy as np
import tabula
import glob
import re

########################################### Function for digitization. ###########################################################

def get_form26as_data(pdf_path):
  # files = glob.glob(fname)
  # print(files)
  file_name = pdf_path.split("\\")[-1][:-4]
  image_name = file_name + '.' + 'pdf'
  lid = file_name.split('_')[0]
  print('file= ',file_name)

# reading the pdf table
  tables = tabula.read_pdf(pdf_path, pages='all',stream=True)



  ################## Assessee Table ################################
  
  df1=tables[0]

  PAN=[]
  Financial_Year=[]
  Assessment_Year=[]
  Current_pan_status=[]
  Name_of_Assessee=[]
  Address_of_Assessee=[]

  # Finding the PAN Number from the columns

  df1.drop(columns='Unnamed: 0',inplace=True)

  for i in df1.columns.tolist():

  # If any Unnamed column is present then delete it
     

  # Using re function to find the 10 digit PAN number from the columns of df1 and storing them in list.
    temp=re.findall("([a-zA-Z0-9]{10,})", i)
    temp=list(temp)


  # Function to find whether list temp contain any number for it to be a PAN
    def num(s):
      return any(j.isdigit() for j in s)


  # Finding and appending the PAN value in list PAN
    for k in temp:
      if num(k)==True:
        PAN.append(k) 

  columns=list(df1.columns)

  # Getting the Financial and Assessment Year and status of PAN

  for i in df1.columns.tolist():
    if "Financial" in i:
      Financial_Year.append(columns[columns.index(i)+1])  
  
    if "Assessment" in i:
      Assessment_Year.append(columns[columns.index(i)+1])

    if "Status" in i:
      Current_pan_status.append(columns[columns.index(i)+1]) # There's a problem here when using different pdf's

  # Getting the Name of Assessee
  for j in range(len(df1)) :
    for k in range(len(df1.columns)) :
      if "Name" in str(df1.iloc[j,k]) :
        Name_of_Assessee.append(df1.iloc[j,k+1])

  # Getting the Address of Assessee
  for j in range(len(df1)) :
    for k in range(len(df1.columns)) :
      if "Address" in str(df1.iloc[j,k]) :
        add=(df1.iloc[j,k+1])
        if df1.iloc[j+1,k+1] is None:
          pass
        else:
          add=add+str(df1.iloc[j+1,k+1])
          Address_of_Assessee.append(add)

  # Generating the table

  assessee_table=pd.DataFrame({"PAN":PAN,
                    "Financial_Year":Financial_Year,
                    "Assessment_Year":Assessment_Year,
                    "Current_pan_status":Current_pan_status,
                    "Name_of_Assessee":Name_of_Assessee,
                    "Address_of_Assessee":Address_of_Assessee,
                    "Image_name":image_name,
                    "lid":lid})
  #assessee_table.to_csv(r'Assessee.csv')


  ############################## Part A ################################################

  df2=tables[1]
  cols=list(df2.columns)
  df3=tables[2]

# Getting the details of each deductor in part A(table 1)

  Name_of_Deductor=[]
  TAN_of_Deductor=[]
  Total_Amount_Paid_Credited=[]
  Total_Tax_Deducted=[]
  Total_TDS_Deposited=[]


# Function to get the details of the deductor 
  def extractd(x):
    for j in range(len(x)) :
      for k in range(len(x.columns)) :
        if "Section" in str(x.iloc[j,k]) :
        
          l1=list(x.iloc[j-1,:]) # Contains the details of each deductor in this table
          #print(l1)
          l1=l1[1:]
      
          l2=[]
          for p in l1:
            if "nan" not in str(p):
              l2.append(p)
        
          if len(l2)>1:
            Name_of_Deductor.append(l2[0])
            TAN_of_Deductor.append(l2[1])
            Total_Amount_Paid_Credited.append(l2[2])
            Total_Tax_Deducted.append(float(l2[3]))
            Total_TDS_Deposited.append(l2[4])

    deduct=pd.DataFrame({"Name_of_Deductor":Name_of_Deductor,
      "TAN_of_Deductor":TAN_of_Deductor,
      "Total_Amount_Paid_Credited":Total_Amount_Paid_Credited,
      "Total_Tax_Deducted":Total_Tax_Deducted,
      "Total_TDS_Deposited":Total_TDS_Deposited})

    return deduct


  d=pd.DataFrame()

# Checking each table for the keywords "Name of deductor"/"TAN of deductor"/"Total TDS" and generating a dataframe
# with the details of the deductors in those tables.
  for tab in tables:
    for j in range(len(tab)) :
      for k in range(len(tab.columns)):
        if "194A" or "194H" in str(tab.iloc[j,k]) :
          d=pd.concat([d,extractd(tab)], axis=0)

# Remove any Duplicates made due to the execution of 3 for loops 
  d=d.drop_duplicates().reset_index()



# Getting the transactions of each deductor

# The Function below will extract the relevent data from the parameters
  def extractt(x):

    for j in list(x.columns):
      if x[j].isna().sum()==(list(x.shape))[0]:
        del x[j]

       #df2=df2.iloc[1:]

    for j in range(len(x)) :
      for k in range(len(x.columns)):
        try:
          if "Sr. No." in str(x.iloc[j,k]):
            x.drop(x.index[[j,j+1]],axis=0,inplace=True)
        except:
          pass


    for i in x.columns:
      if "TAN" in i:
        x["Remarks"]=x[i]
            
    for i in list(x.columns):
      if "TAN" in i:
        k=list(x.columns).index(i)
    for j in range(len(x)):
      if len(str(x.iloc[j,k]))<10:
        x.iloc[j,k]=x.iloc[j-1,k]


    for j in range(len(x)) :
      for k in range(len(x.columns)) :            
        try:
          if "nan" in str(x.iloc[j,1]):
            x.drop(x.index[[j]],axis=0,inplace=True)
          if "nan" in str(x.iloc[j,2]):
            x.drop(x.index[[j]],axis=0,inplace=True)
        except:
          pass

    x=x.reset_index()

    for i in list(x.columns):
      if "Name" in i:
        list1=x[i].str.split(" ")
        if len(list1[0])==3:
          x[['Transaction_Date', 'Status_of_Booking', 'Date_of_Booking']] = pd.DataFrame([ x.split(' ') for x in x[i].tolist() ])
        else:
          x[['Transaction_Date', 'Status_of_Booking']] = pd.DataFrame([ x.split(' ') for x in x[i].tolist() ])
          x['Date_of_Booking']=x.iloc[:,(list(x.columns)).index("Name of Deductor")+1]
          del x["Unnamed: 1"]

    for i in x.columns:
      if "index" in i:
        del x[i]  
      if "Name" in i:
        del x[i]
    return x


  # If the table contains any type of Section value(192,194A etc) then finding and converting that table into parta format

  if '194A' or '192' or '194H' in str(df3.columns):
    if 'Unnamed: 0' in df3.columns:
      df3.drop(columns='Unnamed: 0',inplace=True)
    df3=df3.columns.to_frame().T.append(df3,ignore_index=True)
    df3.columns=range(len(df3.columns))
    df3[2]=df3[2]+' '+df3[3]
    df3.drop(columns=3,inplace=True)
    df3.columns=cols

    part_a=pd.DataFrame(extractt(df3))
    part_a1=pd.DataFrame(extractt(df2))


    table_part_a=pd.concat([part_a1,part_a],axis=0)

  else:
    table_part_a=pd.DataFrame(extractt(df2))


  table_part_a['TAN of Deductor']=[i.strip() if pd.notna(i) else i for i in table_part_a['TAN of Deductor']]
  table_part_a.replace(to_replace ='-',value = np.nan,inplace=True)
  table_part_a['TAN of Deductor'].fillna( method ='ffill', inplace = True)
  table_part_a.reset_index(drop=True,inplace=True)



# Renaming the columns of the Part A table
  cols=['Sr_No.',
'Section_1',
'TAN_of_Deductor',
'Amount_Paid_Credited',
'Tax_Deducted',
'TDS_Deposited',
'Remarks', 
'Transaction_Date',
'Status_of_Booking',
'Date_of_Booking']

  table_part_a.columns=cols

# Setting the position of name of deductor column
  table_part_a=pd.merge(table_part_a,d,on=["TAN_of_Deductor"])
  name=table_part_a.pop('Name_of_Deductor')
  table_part_a.insert(2,'Name_of_Deductor',name)

  table_part_a["PAN"]=PAN[0]
  table_part_a["Name_of_Assessee"]=Name_of_Assessee[0]
  table_part_a["Assessment_Year"]=Assessment_Year[0]

  #table_part_a.to_csv(r'PART A.csv')


  ############################## Part B ################################################

# We apply the same method as we've used for part a extraction

# first we need to extract the data of the collectors in part b table 

  Name_of_Collector=[]
  TAN_of_Collector=[]
  Total_Amount_Paid_Debited=[]
  Total_Tax_Collected=[]
  Total_TCS_Deposited=[]


  for tab in tables :
    cols=list(tab.columns)
    for i in cols:
      if "Collected" in i:
        data=tab
      
        for j in range(len(data)) :
          for k in range(len(data.columns)) :
          
            if "Section" in str(data.iloc[j,k]) :
            
              l1=list(data.iloc[j-1,:])
              l1=l1[1:]
              l2=[]
            
              for p in l1:
                if "nan" not in str(p):
                  l2.append(p)
            
              if len(l2)>1:
                Name_of_Collector.append(l2[0])
                TAN_of_Collector.append(l2[1])
                Total_Amount_Paid_Debited.append(l2[2])
                Total_Tax_Collected.append(l2[3])
                Total_TCS_Deposited.append(l2[4])
                            
  part_b_collec=pd.DataFrame({'Name_of_Collector':Name_of_Collector,
            'TAN_of_Collector':TAN_of_Collector,
            'Total_Amount_Paid_Debited':Total_Amount_Paid_Debited,
            'Total_Tax_Collected':Total_Amount_Paid_Debited,
            'Total_TCS_Deposited':Total_Amount_Paid_Debited})


# Extracting all the transactions of collectors

  def extractct(x):

    for j in list(x.columns):
      if x[j].isna().sum()==(list(x.shape))[0]:
        del x[j]

       #df2=df2.iloc[1:]

    for j in range(len(x)) :
      for k in range(len(x.columns)):
        try:
          if "Sr. No." in str(x.iloc[j,k]):
            x.drop(x.index[[j,j+1]],axis=0,inplace=True)
        except:
          pass


    for i in x.columns:
      if "TAN" in i:
        x["Remarks"]=x[i]
            
    for i in list(x.columns):
      if "TAN" in i:
        k=list(x.columns).index(i)
    for j in range(len(x)):
      if len(str(x.iloc[j,k]))<10:
        x.iloc[j,k]=x.iloc[j-1,k]


    for j in range(len(x)) :
      for k in range(len(x.columns)) :            
        try:
          if "nan" in str(x.iloc[j,1]):
            x.drop(x.index[[j]],axis=0,inplace=True)
          if "nan" in str(x.iloc[j,2]):
            x.drop(x.index[[j]],axis=0,inplace=True)
        except:
          pass

    x=x.reset_index()

    for i in list(x.columns):
      if "Name" in i:
        list1=x[i].str.split(" ")
        if len(list1[0])==3:
          x[['Transaction_Date', 'Status_of_Booking', 'Date_of_Booking']] = pd.DataFrame([ x.split(' ') for x in x[i].tolist() ])
        else:
          x[['Transaction_Date', 'Status_of_Booking']] = pd.DataFrame([ x.split(' ') for x in x[i].tolist() ])
          x['Date_of_Booking']=x.iloc[:,(list(x.columns)).index(i)+1]
          del x["Unnamed: 1"]

    for i in x.columns:
      if "index" in i:
        del x[i]  
      if "Name" in i:
        del x[i]
    return x

  if len(part_b_collec) is 0:
    dict = {'Sr_No.':[],"Section_1":[],"TAN_of_Collector":[],"Amount_Paid_Debited":[],"Tax_Collected":[],
                    "TCS_Deposited":[],"Remarks":[],"Transaction_Date":[],"Status_of_Booking":[],"Date_of_Booking":[],
                    "Name_of_Collector":[],"Total_Amount_Paid_Debited":[],"Total_Tax_Collected":[]
                    ,"Total_TCS_Deposited":[],"PAN":[],"Name_of_Assessee":[],"Assessment_Year":[]}
    table_part_b=pd.DataFrame(dict)
  else:
    part_b_trans=pd.DataFrame(extractct(data))

  # Renaming the columns for the desired output
    cols=['Sr_No.',
  'Section_1',
  'TAN_of_Collector',
  'Amount_Paid_Debited',
  'Tax_Collected',
  'TCS_Deposited',
  'Remarks', 
  'Transaction_Date',
  'Status_of_Booking',
  'Date_of_Booking']

    part_b_trans.columns=cols

  # Merging the two dataframes
    table_part_b=pd.merge(part_b_trans,part_b_collec,on=["TAN_of_Collector"],how="left")



    table_part_b["PAN"]=PAN[0]
    table_part_b["Name_of_Assessee"]=Name_of_Assessee[0]
    table_part_b["Assessment_Year"]=Assessment_Year[0]


  #table_part_b.to_csv(r'PART B.csv')


  ############################## Part C ################################################


# Checking the tables for the columns containing the keyword 'Major' for extracting partc data
  for tab in tables:
    col=list(tab.columns)
    for i in col:
      if "Major" in i:
        data=tab
        partc=data.iloc[1:,:] # Remove the first row of the table containg partc data


# Deleting the unwanted columns
  del partc['3']    
  del partc['2']

  table_part_c=partc


  table_part_c["PAN"]=PAN[0]
  table_part_c["Name_of_Assessee"]=Name_of_Assessee[0]
  table_part_c["Assessment_Year"]=Assessment_Year[0]


  #table_part_c.to_csv(r'PART C.csv')



  ############################## Part D ################################################


# Checking the tables for the columns containing the keyword 'Refund' for extracting partd data
  partd=pd.DataFrame()

  for tab in tables:
    col=list(tab.columns)
    for i in col:
      if ("Nature of Refund" in i) or ('Amount of Refund' in i):
        data=tab
        partd=data.iloc[1:,:] # Remove the first row of the table containg partc data

    for j in list(partd.columns):
      if "Unnamed" in j:
        partd["Interest"]=partd[j]
        del partd[j]


  table_part_d=partd


  table_part_d["PAN"]=PAN[0]
  table_part_d["Name_of_Assessee"]=Name_of_Assessee[0]
  table_part_d["Assessment_Year"]=Assessment_Year[0]


  #table_part_d.to_csv(r'PART D.csv')

 ############################## Part G ################################################

# Checking the tables for the columns containing the keyword 'Refund' for extracting partd data

  for tab in tables:
    col=list(tab.columns)
    for i in col:
      if ("Short Payment" in i) or ('Short Deduction' in i):
        data=tab
        partg=data.iloc[1:,:] # Remove the first row of the table containg partc data

# Extracting data from the above dataframe
  Financial_Year=[]
  Short_Payment=[]
  Short_Deduction=[]
  Interest_on_TDS=[]
  Interest_on_TDS_1=[]
  Late_Filing_Fee_us=[]
  Interest_us_220=[]
  Total_Default=[]
  TAN=[]

  for j in range(len(partg)) :
    for k in range(len(partg.columns)) :
      if "Short Payment" in str(partg.iloc[j,k]) :

      # Getting the TAN if transactions are present
        if "TANs" in str(partg.iloc[j,k]):
          TAN=str(partg.iloc[j+2,k])
        else:
          TAN='-'
        print(TAN)


        l1=list(partg.iloc[j-1,:]) # Contains the details of each deductor in this table

        l1=l1[1:]
        l2=[]
        for p in l1:
          if "nan" not in str(p):
            l2.append(p)

# Same as what we did for assessee table
        if len(l2)>1:
          Financial_Year.append(l2[0])
          Short_Payment.append(l2[1])
          Short_Deduction.append(l2[2])
          Interest_on_TDS.append(float(l2[3]))
          Interest_on_TDS_1.append(l2[4])
          Late_Filing_Fee_us.append(l2[5])
          Interest_us_220.append(l2[6])
          Total_Default.append(l2[7])
      else:
        pass

  table_part_g=pd.DataFrame({'Financial Year':Financial_Year, 'Short Payment':Short_Payment, 'Short Deduction':Short_Deduction,
       'Interest on  TDS':Interest_on_TDS, 'Interest on  TDS.1':Interest_on_TDS_1, 'Late Filing Fee u/s 234E':Late_Filing_Fee_us,
       'Interest u/s 220(2)':Interest_us_220, 'Total Default':Total_Default,'TAN':TAN}) 



  table_part_g["PAN"]=PAN[0]
  table_part_g["Name_of_Assessee"]=Name_of_Assessee[0]
  table_part_g["Assessment_Year"]=Assessment_Year[0]

  #table_part_g.to_csv(r'PART G.csv')  


  x = file_name.split('_')[0]
  y = file_name.split('_')[1:]

  
  z = x + '_form26as_asseseedetails_' + '_'.join(y)
  z1 = x + '_form26as_parta_' + '_'.join(y)
  z2 = x + '_form26as_partb_' + '_'.join(y)
  z3 = x + '_form26as_partc_' + '_'.join(y)
  z4 = x + '_form26as_partd_' + '_'.join(y)
  z5 = x + '_form26as_partg_' + '_'.join(y)


  assessee_table['lid'] = lid
  table_part_a['lid'] = lid
  table_part_b['lid'] = lid
  table_part_c['lid'] = lid
  table_part_d['lid'] = lid
  table_part_g['lid'] = lid
  
  assessee_table.to_csv(r'D:\digitizedfiles\{}_i.csv'.format(z), index=False)
  table_part_a.to_csv(r'D:\digitizedfiles\{}_i.csv'.format(z1), index=False)
  table_part_b.to_csv(r'D:\digitizedfiles\{}_i.csv'.format(z2), index=False)
  table_part_c.to_csv(r'D:\digitizedfiles\{}_i.csv'.format(z3), index=False)
  table_part_d.to_csv(r'D:\digitizedfiles\{}_i.csv'.format(z4), index=False)
  table_part_g.to_csv(r'D:\digitizedfiles\{}_i.csv'.format(z5), index=False)

  data_list = []

  data_list.append(r'D:\digitizedfiles\{}_i.csv'.format(z))
  data_list.append(r'D:\digitizedfiles\{}_i.csv'.format(z1))
  data_list.append(r'D:\digitizedfiles\{}_i.csv'.format(z2))
  data_list.append(r'D:\digitizedfiles\{}_i.csv'.format(z3))
  data_list.append(r'D:\digitizedfiles\{}_i.csv'.format(z4))
  data_list.append(r'D:\digitizedfiles\{}_i.csv'.format(z5))
    
  return data_list

# Calling the function
# digitize('765598_7_26_AS_HWT_AY19-20.pdf')
