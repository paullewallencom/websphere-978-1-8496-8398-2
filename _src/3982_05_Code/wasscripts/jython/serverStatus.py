import re;

#---------------------------------------------------------------------
# Name: serverStatus()
# Role: Display the status of the known servers
#---------------------------------------------------------------------
def serverStatus() :
  #-------------------------------------------------------------------
  # RegExp to extract the server, cell, and node name for each server
  #-------------------------------------------------------------------
  pat = re.compile( r'^(\w+)\(cells/(\w+)/nodes/(\w+)/servers\/\1.*\)$' );

  #-------------------------------------------------------------------
  # Retrieve the list of known servers
  # While building the list, compute the max length of each name
  #-------------------------------------------------------------------
  info   = [];
  maxLen = [ 0 ] * 3;

  #-------------------------------------------------------------------
  # For each server of the known servers
  #-------------------------------------------------------------------
  servers = AdminConfig.list( 'Server' ).splitlines();
  for server in servers :
    #-----------------------------------------------------------------
    # An Object Name will exist if the specified server is running
    #-----------------------------------------------------------------
    oName = AdminConfig.getObjectName( server );
    if oName != '' :
      status = 'running';
    else :
      status = 'stopped';
    #-----------------------------------------------------------------
    # Extract the server, cell, and node name
    # (match Object)
    #-----------------------------------------------------------------
    mObj = pat.match( server );
    if mObj :
      #---------------------------------------------------------------
      # Save the data, and see if the length of each field name is the
      # longest we have yet seen (i.e., maxLen[ i ])
      #---------------------------------------------------------------
      ( sName, cName, nName ) = mObj.groups();
      info.append( ( sName, cName, nName, status ) );
      for i in range( 3 ) :
        L = len( mObj.group( i + 1 ) );
        if L > maxLen[ i ] : maxLen[ i ] = L;

  #-------------------------------------------------------------------
  # Display the information
  #-------------------------------------------------------------------
  ( L0, L1, L2 ) = maxLen;
  ( sName, cName, nName, status ) = 'Server,Cell,Node,Status'.split( ',' );
  sName = sName.center( L0 );
  cName = cName.center( L1 );
  nName = nName.center( L2 );
  print '%(sName)s | %(cName)s | %(nName)s | %(status)s' % locals();
  print ( '-' * L0 ) + '-+-' + ( '-' * L1 ) + '-+-' + ( '-' * L2 ) + '-+--------';
  for scn in info :
    ( sName, cName, nName, status ) = scn;
    print '%-*s | %-*s | %-*s | %s' % ( L0, sName, L1, cName, L2, nName, status );
#----------------------------------------------------------------------
# Main Entry Point
#----------------------------------------------------------------------  
serverStatus()