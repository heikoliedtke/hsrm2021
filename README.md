# hsrm2021
Update for hsrm2022 session
Lets do something really crazy this year
Examples for HSRM 2022

# startup1.cfg
- install nginx
- install git
- create a static html page on the fly


# startup2.cfg
- install nginx
- install git
- copy a html file from a GCP cloud bucket. The name of the cloud bucket needs to adopted to your setup
- hsrm.html needs to be copied in the bucket first


# container01
- Dockerfile
    - FROM ubuntu
    - install nginx
    - copy hsrm to web server home
    - start nginx
- hsrm.html

# container02
- Dockerfile
- Flask Webapp