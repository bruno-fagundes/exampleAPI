#!/bin/sh

# Menu and UI
menu(){
    dialog  \
        --title ''  \
        --menu ''  \
        0 0 0  \
		clean_py  'Remove todos os arquivos .pyc e as pastas __pycache__'
}

# Functions
clean_py(){
    # recursively removes all .pyc files and __pycache__ directories in the current directory
    find . |  \
    grep -E "(__pycache__|\.pyc$)" |  \
    xargs rm -rf
    dialog  \
        --title 'clean_py concluído'  \
        --msgbox 'Limpeza executada com sucesso!'  \
        6 40
}

# Script init
while : ; do
    resposta=$(
        dialog --stdout  \
            --title 'PORTAL SETUP'  \
            --menu 'Escolha uma opção:'  \
            0 0 0  \
            1 'Remove todos os arquivos .pyc e as pastas __pycache__'  \
            0 'Sair'
    )

    # Exit on press ESC
    [ $? -ne 0 ] && break

    case "$resposta" in
        1) clean_py ;;
        0) break ;;
    esac
done

clear
