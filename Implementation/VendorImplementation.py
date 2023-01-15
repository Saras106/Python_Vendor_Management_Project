from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        # Add you code here after verifying the vendor data exists in the dictionary
        if self.vendor_model.is_correct_vendor(username,password):
            self.vendor_session.login

         

    def logout(self, username):
        # Add your code here to log out the current vendor
        if self.vendor_session.check_login(username):
            self.vendor_session.logout(username)
        
