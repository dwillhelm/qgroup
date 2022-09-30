
"""
Because of the VASP licence, we can't store POTCAR files on the repo. 

However, we might have code that needs to automate the import or creation of POTCARs.

We can address this by using a config file to pass a users path/to/potcars so that they can be found by our code without the need to add specific files or paths to the repo

However, we need to track the config file, but not the contents - see this link for more information https://compiledsuccessfully.dev/git-skip-worktree/



"""
