from xml.dom import minidom

# this file reads nagios statusfile.xml 
# can be used to generate data into a custom host overview page
# read only data
# Author: Marcos Lopez - 2007 

doc = minidom.parse('/home/user/dev/portal/sys/nagios/remote_output/statusfile.xml')

host_status = doc.getElementsByTagName('hoststatus')
service_status = doc.getElementsByTagName('servicestatus')


hosts_list=[]
service_list=[]
# loop through <hoststatus> elements list
for host in host_status:
  
  # go through <attributes> list foreach host (<hoststatus><servicestatus>)
  x_list=[]
  for x in host.getElementsByTagName('attribute'):

    # attribute-element in attributes list
    if not type(x.firstChild).__name__ == 'NoneType':
      attribname = str(x.getAttribute('name'))
      val = str(x.firstChild.data)
      if attribname == 'host_name' or attribname == 'current_state':
        
        strs = '%s = %s' % (attribname, val)
        happ = {'attribute':attribname,
            'value':val
        }
            
        x_list.append(happ)


  hosts_list.append(x_list)



        

for host in service_status:
  # go through <attributes> list foreach host (<hoststatus><servicestatus>)
  x_list=[]
  for x in host.getElementsByTagName('attribute'):
    # attribute-element in attributes list
    
    if not type(x.firstChild).__name__ == 'NoneType':
      attribname = str(x.getAttribute('name'))
      val = str(x.firstChild.data)
      if attribname == 'host_name' or attribname == 'current_state' or attribname == 'check_command' or attribname == 'plugin_output':

        strs = '%s = %s' % (attribname, val)
        happ = {
            'attribute':attribname,
            'value':val,
            'plugin_output':,
            'check_command':,
        }
        x_list.append(happ)


  service_list.append(x_list)

      

    

    
