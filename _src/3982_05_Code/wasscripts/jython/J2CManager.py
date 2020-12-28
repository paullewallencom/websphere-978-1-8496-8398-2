import sys
import java.util as util
import java.io as javaio

class JDBCUtil:
   def __init__(self,fullPropsPath):
      self.fullPropsPath=fullPropsPath

#-------------------------------------------------------------
# Create / Modify J2C Java Authentication and Authorization Service (JAAS)
#-------------------------------------------------------------
   def J2CAuthentication(self,props1): 
      appName = props1.get("AppName")
      updJAAS = props1.get("updJAAS")
      JAASAlias = props1.get("JAASAlias")
      JDBCName=props1.get("JDBCName")
      cellName = AdminControl.getCell()
      JAASConfigID = AdminConfig.getid("/Cell:"+cellName+"/Security:/JAASAuthData:/" )
      JAASDescription = props1.get("JAASDescription")
      JAASUserId = props1.get("JAASUserId")
      JAASPassword =  props1.get("JAASPassword")
      JAASAttr = [["alias", JAASAlias], ["description", JAASDescription], ["userId", JAASUserId], ["password", JAASPassword]]
      existingJAASList = AdminConfig.getid("/Cell:"+cellName+"/Security:/JAASAuthData:/" )
      
      #Tidy up list and remove blank lines
      JAASItems=existingJAASList.splitlines();
      print "INFO: Looping through Existing JAAS Alias"
      updateJAASFlag="false"
      for JAASItem in JAASItems:
         print JAASItem
         existingJAASAlias = AdminConfig.showAttribute(JAASItem,"alias")
         print "INFO: ExistingJAASAlias=%s" % existingJAASAlias
         if (cmp(existingJAASAlias, JAASAlias) == 0):
            print "INFO: JAASAuthInfo Exists, Updating Alias:"+existingJAASAlias+" ......"
            AdminConfig.modify(JAASItem, JAASAttr )
            print "     Modified!"
            updateJAASFlag = "true"
            #Exit the foor loop, now we have updated our match
            break 
         #end if
      #end For
      if (cmp(updateJAASFlag, "false") == 0):
         print "INFO: Creating new JAASAuthInfo Alias: "+JAASAlias+" login/password ......"
         security = AdminConfig.getid("/Cell:"+cellName+"/Security:/" )
         print "security=%s" % security
         AdminConfig.create("JAASAuthData", security, JAASAttr )
         print "INFO: J2C Authentication Created Successfully!"
      #end if
   
#-------------------------------------------------------------------------
# Save Configuration
#-------------------------------------------------------------------------
      print "Saving configuration..."
      AdminConfig.save()
      print "Complete!"
#-------------------------------------------------------------
# Load properties File
#-------------------------------------------------------------	
   def loadproperties(self):
      
      print "------load properties %s " % self.fullPropsPath
      properties = util.Properties()
      source = javaio.FileInputStream(fullPropsPath)
      bis = javaio.BufferedInputStream(source)
      props = util.Properties()
      props.load(bis)
      print "Properties file has been loaded"
      return props
#-------------------------------------------------------------
# Main entry point
#-------------------------------------------------------------	
fullPropsPath = sys.argv[0]
print "fullPropsPath=%s" % fullPropsPath
dsObj = JDBCUtil(fullPropsPath)
props1=dsObj.loadproperties()
dsObj.J2CAuthentication (props1)