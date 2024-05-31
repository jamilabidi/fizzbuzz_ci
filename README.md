# fizzbuzz_ci
context: for studying purpose a bottle_app is develop on a local computer and each time test are run Ok the bottle app will be published on Python anywhere
stack : (nb : aprevious script shell version was first created but is no longer used) / python/ pythonanywhere API/ github


1/ create a python anywhere account and initiate a web app
2/ add a ssh access key to the github repo from the newly created server
3/ clone the git repo 
4/ get the id and credential for the pythonanywher API and modify the script on your local computer adequatly
5/ it is assume that on your local computer your are also connected to the git hub repo
6/ Principle: 
  when you trigger the script from your local computer ( script should be indicated in your gitignore as well)
    - the test will be run
    - if they all pass : commit and push to the distant repo
    - send a command to the remote pythonanywhere to pull from the repo 
    - reupload the site
