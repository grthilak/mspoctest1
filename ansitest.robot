*** settings ***
library  Impansible
library  Collections
library  OperatingSystem

*** test cases ***
test 1
        ${x}=   Setup  192.168.0.10
                log  ${x}
        ${y}=   get from dictionary  ${x}   ansible_facts
        ${h}=   get from dictionary  ${y}   ansible_hostname
        ${z}=   get from dictionary  ${y}   ansible_distribution
                Should be Equal  ${z}  cisco
                Should Contain   ${h}  tester
