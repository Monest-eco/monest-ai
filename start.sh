#!/bin/bash

allPackages=(python3 python3-pip)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    for package in ${allPackages[@]}; do
        echo -e "\e[31mChecking $package version"
        if (dpkg-query -W $package >/dev/null) then
            echo -e "\e[32m$package OK"
        else
            echo -e "Installing $package"
            sudo apt-get --yes install $package
        fi
    done
elif [[ "$OSTYPE" == "darwin"* ]]; then
    for package in ${allPackages[@]}; do
        echo -e "\e[31mChecking $package version"
        if (pkgutil --pkgs | grep $package >/dev/null) then
            echo -e "\e[32m$package OK"
        else
            echo -e "Installing $package"
            brew install $package
        fi
    done
fi
allPipPackages=(tensorflow pandas numpy matplotlib)
for package in ${allPipPackages[@]}; do
    if (pip list | grep $package &> /dev/null) then
        echo -e "\e[32m$package OK"
    else
        echo -e "\e[31mInstalling $package"
        pip install $package &> /dev/null
    fi
done
echo -e "\e[39m"
python3 src/main.py