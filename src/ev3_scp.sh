#!/bin/sh
echo "Ola, escolha uma das opcoes abaixo:"
echo "0 - Acessar ev3 por ssh"
echo "1 - Copiar arquivo para o ev3"
echo "2 - Puxar arquivo do ev3"
echo "3 - Nada"
read USER_OPTION
echo

EV3_ADDR_SCP="robot@ev3dev.local:"
EV3_ADDR_SSH="robot@ev3dev.local"

if [ $USER_OPTION = 3 ]; then
    exit
    elif [ $USER_OPTION = 0 ]; then
        ssh EV3_ADDR_SSH  
    elif [ $USER_OPTION = 1 ]; then
        echo "Escreva o nome do arquivo (com diretorio, se necessario):"
        read FILE_NAME
        scp $FILE_NAME $EV3_ADDR_SCP
    elif [ $USER_OPTION = 2 ]; then
        echo "Escreva o nome do arquivo (com diretorio, se necessario):"
        read FILE_NAME
        EV3_ADDR_SCP="$EV3_ADDR_SCP/$FILE_NAME"
        scp $EV3_ADDR_SCP .
        echo "Salvo no seu diretorio atual"
    else
        echo "ERROU!
fi