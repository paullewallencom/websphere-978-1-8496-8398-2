#install the application
deployEAR="/root/was8book/deploy/HRListerEAR.ear"
appName="HRListerEAR"
attr="-appname " + appName + " "
AdminApp.install(deployEAR, "["+attr+"]" );
#save
AdminConfig.save();