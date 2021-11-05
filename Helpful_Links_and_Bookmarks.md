# Helpful Links and Files

## Github Guides
https://guides.github.com/  
https://guides.github.com/features/mastering-markdown/

## gitignore of large files  
  
Not possible to put in .gitignore file, but search for names of big files and add them to gitignore with this function:  

```
find . -size +1G | sed 's|^\./||g' | cat >> .gitignore;
```
OR  
````
find . -size +1G -printf '%P\n' >> .gitignore;
````

## Running Anaconda Env as default in VSCode
https://medium.com/analytics-vidhya/efficient-way-to-activate-conda-in-vscode-ef21c4c231f2  
https://medium.com/@udiyosovzon/how-to-activate-conda-environment-in-vs-code-ce599497f20d

## Upgrade Packages from requirements.txt file
https://stackoverflow.com/questions/24764549/upgrade-python-packages-from-requirements-txt-using-pip-command


## Git
### Define UserName and UserEmail
https://linuxize.com/post/how-to-configure-git-username-and-email/
### Deleting Git Branch
https://linuxize.com/post/how-to-delete-local-and-remote-git-branch/

## Docker
### Setting up and Downloading Docker
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
https://linuxhint.com/install_configure_docker_ubuntu/

## Keras

### Saving Models (H5 Files as well)
https://www.tensorflow.org/guide/keras/save_and_serialize


## Pip Requirements

### Creating Pip Requirements
https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

### Upgrade all packages 
https://github.com/simion/pip-upgrader
