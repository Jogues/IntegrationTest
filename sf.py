from simple_salesforce import Salesforce

sfusername = 'isaac@labster.com.partial'
sfpassword = ''
sfsecurity = 'FnNhu4ABOzDIU4ugY0Sjx5S38'
sforg = ''

sf = Salesforce(password=sfpassword, username=sfusername,
    organizationId=sforg, sandbox=True)

Simulation = sf.Simulation__c.create({
'Name':'Test Simulation',
'Active__c': True,

})

license = sf.License__c.create({
'Valid_from__c':'2018-04-21T00:00:00.000Z',
'Valid_to__c':'2018-04-28T00:00:00.000Z',
'Login_Email__c':'isaac+0011@labster.com',
'Password__c':'Lab2ster',
'Course_Name__c':'AT 060418',
'Active__c':True,
'Related_Opportunity__c':'0064E000004m5tfQAA',
'Type__c':'Internal',
'ConsumerKey__c':'a0u4E000004A01rQAC',
'Contact_at_University__c':'0034E00000WfffrQAB',})

licensedict = dict(license)
licenseId = licensedict["id"]
print(licenseId)

sf.LS_Relationship__c.create({'License_ID__c':licenseId, 'Simulation__c':'a0Kw000000TpSF9EAN', 'Quantity__c':33})



#sf.ConsumerKey__c.describe('0014E00000a2721QAA')
