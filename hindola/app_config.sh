#!/bin/bash

#echo "Please enter Database User Name:"
#read us
#echo "Please enter Database Password:"
#read pass
#echo "Please enter Database Name:"
#read dbname
#echo "Please enter Database Host Address:"
#read dbhost

#echo "Please enter App Host IP:"
#read apphost

#env DB_USER ${us}
#env DB_PASS ${pass}
#env DB_NAME ${dbname}
#env DB_HOST ${dbhost}

#env APP_HOST ${apphost}

sed -i 's@socket = io.connect("[[:digit:]]\+\.[[:digit:]]\+\.[[:digit:]]\+\.[[:digit:]]\+@socket = io.connect("'"${apphost}"'@g' /main/myproject/templates/annotationtool.html
sed -i 's@socket1 = io.connect("[[:digit:]]\+\.[[:digit:]]\+\.[[:digit:]]\+\.[[:digit:]]\+@socket1 = io.connect("'"${apphost}"'@g' /main/myproject/templates/annotationtool.html
