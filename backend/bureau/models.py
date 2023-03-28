from django.db import models


# Create your models here.

class bureau(models.Model):
    index = models.CharField(max_length=20, null=True, default=" ")
    Loan_Selection = models.CharField(max_length=10)
    Loan_Selection_edited = models.CharField(max_length=5)
    Loan_Selection_user_edited = models.BinaryField()
    Customer_Id = models.CharField(max_length=10)
    Date_reported = models.DateField()
    Loan_type = models.CharField(max_length=50)
    Loan_status = models.CharField(max_length=10)
    Disbursed_amount = models.CharField(max_length=20)
    Disbursed_amount_edited = models.CharField(max_length=10, null=True)
    Disbursed_amount_user_edited = models.CharField(max_length=10)
    Disbursal_date = models.DateField()
    Tenure = models.CharField(max_length=20, null=True)
    Tenure_new = models.CharField(max_length=20, null=True)
    Tenure_edited = models.CharField(max_length=20, null=True)
    Tenure_user_edited = models.BinaryField()
    ROI = models.CharField(max_length=10, null=True)
    ROI_new = models.CharField(max_length=50, null=True)
    ROI_edited = models.CharField(max_length=50, null=True)
    ROI_user_edited = models.BinaryField()
    EMI = models.CharField(max_length=50, null=True, blank=True)
    EMI_new = models.CharField(max_length=50, null=True, blank=True)
    EMI_edited = models.CharField(max_length=50, null=True, blank=True)
    EMI_user_edited = models.BinaryField()
    Current_Balance = models.CharField(max_length=50, blank=True)
    DPD = models.CharField(max_length=20, null=True, blank=True)
    DPD_month_new = models.CharField(max_length=50, blank=True, null=True)
    Overdueamount = models.CharField(max_length=20, blank=True)
    Source = models.CharField(max_length=20)
    lead_id = models.CharField(max_length=20, null=True, blank=True)
    final_selected = models.BinaryField()
    valuetype = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)

    def __str__(self):
        return (self.Customer_Id)
