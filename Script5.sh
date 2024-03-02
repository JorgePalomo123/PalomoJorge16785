#!/bin/bash
#
for pagina in $(cat paginas)
do
#	echo -e "$pagina \n"
	salidas=$(curl -s -I "$pagina" | sed -n '1p' | tail -1 | awk '{print $3" " $4}' | rev | cut -c3- | rev)
	if [ -z "$salida" ]
	then
		echo $pagina "Fail"
	else	
		echo $pagina "OK"
	fi
done
