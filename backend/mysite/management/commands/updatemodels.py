from django.core.management.base import BaseCommand
import  pandas as pd
from mysite.models import *
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('bureau.csv')
        for index, Loan_Selection, Loan_Selection_edited, Loan_Selection_user_edited, Customer_Id, Date_reported, Loan_type, Loan_status, Disbursed_amount, Disbursed_amount_edited, Disbursed_amount_user_edited, Disbursal_date, Tenure, Tenure_new, Tenure_edited, Tenure_user_edited, ROI, ROI_new, ROI_edited, ROI_user_edited, EMI, EMI_new, EMI_edited, EMI_user_edited, Current_Balance, DPD, DPD_month_new, Overdueamount, Source, lead_id, final_selected, valuetype, salary in zip(df.index, df.Loan_Selection, df.Loan_Selection_edited, df.Loan_Selection_user_edited, df.Customer_Id, df.Date_reported, df.Loan_type, df.Loan_status, df.Disbursed_amount, df.Disbursed_amount_edited, df.Disbursed_amount_user_edited, df.Disbursal_date, df.Tenure, df.Tenure_new, df.Tenure_edited, df.Tenure_user_edited, df.ROI, df.ROI_new, df.ROI_edited, df.ROI_user_edited, df.EMI, df.EMI_new, df.EMI_edited, df.EMI_user_edited, df.Current_Balance, df.DPD, df.DPD_month_new, df.Overdueamount, df.Source, df.lead_id, df.final_selected, df.valuetype, df.salary):
            models = bureau(index = index, Loan_Selection = Loan_Selection, Loan_Selection_edited = Loan_Selection_edited, Loan_Selection_user_edited = Loan_Selection_user_edited, Customer_Id = Customer_Id, Date_reported = Date_reported, Loan_type = Loan_type, Loan_status = Loan_status, Disbursed_amount = Disbursed_amount, Disbursed_amount_edited = Disbursed_amount_edited, Disbursed_amount_user_edited = Disbursed_amount_user_edited, Disbursal_date = Disbursal_date, Tenure = Tenure, Tenure_new = Tenure_new, Tenure_edited = Tenure_edited, Tenure_user_edited = Tenure_user_edited, ROI = ROI, ROI_new = ROI_new, ROI_edited = ROI_edited, ROI_user_edited = ROI_user_edited, EMI = EMI, EMI_new = EMI_new, EMI_edited = EMI_edited, EMI_user_edited = EMI_user_edited , Current_Balance = Current_Balance, DPD = DPD, DPD_month_new = DPD_month_new, Overdueamount = Overdueamount, Source = Source, lead_id = lead_id, final_selected = final_selected, valuetype = valuetype, salary = salary)
            models.save()
        # print(df)
        # for lead_id, file_name, date in zip(df.lead_id, df.file_name, df.date):
        #     models = downloaded_file_details(lead_id=lead_id,file_name=file_name,date=date)
        #     models.save()


        # can we try manually adding the data and then doing operations