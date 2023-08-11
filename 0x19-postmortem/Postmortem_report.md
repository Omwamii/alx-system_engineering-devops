# Postmorterm Report

## Empty response from the server

### Incident report on [ apache2 empty response from server ](https://github.com/Omwamii/alx-system_engineering-devops/tree/master/0x0D-web_stack_debugging_0)
![Insert laughs] (https://www.agileanalytics.cloud/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fzensoftwaresite-media-zen-platform%2Fpreview_picture_807aa64858%2Fpreview_picture_807aa64858.webp&w=750&q=75)


### Summary
On june 2023 after installing apache service on webserver on a docker container, on testing the server on localhost using curl utility, the server returned an empty response error.
`curl 0:8080`
— curl: (52) Empty reply from server


#### Timeline

- **09:30 EAT** - Empty response when trying to access apache through tomcat’s port
- **09:35 EAT** - checking apache status
- **09:38 EAT** - Apache not running, checking /var/logs/apache2/error.log
- **09:45 EAT** - Error log error: Could not reliably determine the server's fully qualified domain name
- **09:50 EAT** - check journalctl to get conclusive problem statement by running `sudo journalctl -u apache2.service --since today --no-pager`
- **10:15 EAT** - Checking /etc/apache2/apache2.conf settings revealed that the conf file settings lacked a ServerName directive
- **10:20 EAT** - setting a ServerName directive on conf file
- **10:22 EAT** - Restarting apache server
- **10:25 EAT** - checking status of apache
- **10:28 EAT** - curl localhost
- **10:30 EAT** - Server is now running and the default apache webpage is being returned

#### Root Cause and Resolution

The issue was the configuration file needed to be completely configured. The *ServerName* directive had not been set, so the server did not have a specific domain name to bind to (For a user to query). Since I was querying my localhost I had to explicitly set the localhost as the ServerName in the /etc/apache2/apache2.conf
‘ServerName’ 127.0.0.1 and on saving and curling again, the default Apache page was returned, showing that the service was running correctly

#### Corrective and Preventive Measures

- Configuration files should be tested after any changes made on application configurations for example for Apache, `sudo apachectl configtest` and nginx `sudo nginx -t` for the nginx web server

