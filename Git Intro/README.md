# Git Introduction
This project will guide you through some of the more common features of Git that are used for project development. More specifically, we will be focusing on remotes, pushing/pulling, and branches.

## Remotes
In Git, remotes allow access to modify or pull from other repositories. Let's start by creating a new repository for your future projects on your Github account.

1. On the main page, click the plus icon on the upper left hand corner and click "new repository."
2. Create a name for the repository and set the status to public. You don't need to worry about READMEs or .gitignore.
3. Type the following commands in a new folder on your local machine. This will be the folder where you store your projects:
    1. `git init`
    2. `git branch -M main`
    3. `git remote add origin <REPO-URL>`

Type `git remote` to list out the current remotes associated with your repository. You should see "origin." This is an alias that refers to the original repository where the project was created. These provide us with a shorthand way to refer to other repositories when we want to work with them. While "origin" allows us to work with your personal project repository, you can add additional remotes to interact with other repositories. What we want to do now is add a remote to this repository to pull updates to the starter code for future projects.

1. In your repository, type `git remote add starter https://github.com/devbali/sp-22-plextech-fswd-intro-projects.git`. This will add a remote from which you will be able to pull your starter code from. You should now see a new remote with `git remote`.
2. Now we want to pull this README (along with any other starter code that may be present) into your project repository. Type `git pull starter main`.

You should now be able to see the starter code that we currently have available. For the rest of this project, we will be working in the "Git Intro" project folder. Type `git log` and save a screenshot in this folder.

Click [here](https://www.atlassian.com/git/tutorials/syncing#) for more information on remotes.

## Pushing/Pulling
When working on projects, you are going to be constantly pushing and pulling code to update/get updates from your repos. Let's push the screenshot that we just created to our repository.
A "commit" is a list of changes that is stored by git. Committing only affects your local Git record.
1. Type `git add Git\ Intro/<IMAGE-NAME>` to stage the file.
2. Type `git commit -m "image added"` to commit your change.
3. Type `git push origin main` to push your changes to the main branch.

Now when you navigate to the repository on your Github, you should see all the starter code along with your screenshot in the "Git Intro" project folder. If your friend wanted to work with you on a project (like a [group project](https://github.com/devbali/sp-22-plextech-fswd-group-projects)), they would need to `git pull` the changes whenever you update the repository on your end to avoid any major merge conflicts.

Click the links for more information on [pushing](https://www.atlassian.com/git/tutorials/syncing/git-push) and [pulling](https://www.atlassian.com/git/tutorials/syncing/git-pull)

## Branching
Typically when you are working on a larger project with multiple developers, you will be working on a separate branch specific to the feature that you are responsible for. This allows for independent lines of development, as new additions can be made to the main repository without pushing unfinished code from another feature. Let's use this feature for the last part of this project.

Suppose one of your project partners created `foo.py` with a function that prints "Foo" if the input is a multiple of 3 and "Bar" otherwise. However, you found that the function only works with positive numbers up to 30. Your job is to fix this bug while your partner is working on another feature.

1. Create and checkout a new branch with `git checkout -b bug-fix`. If you type `git branch` you should see your new branch with a * next to it to indicate that is your current working branch.
2. Fix the function in `foo.py` so that it works as intended.
3. Add and commit your changes.
4. Type `git push origin bug-fix` to push your changes to the new branch that you created.

You've fixed the bug in the code, but now what? These changes are still in your bug-fix branch, while the issue is still not resolved on main. What we want to do is merge the fixes in our current branch into the main branch of our repository. We can do so through a pull request.

1. On your Github repository, click on "pull requests" and then "new pull request." Select your bug-fix branch as the compare branch and click "create pull request" (make sure main is the base branch). Here, reviewers can comment on the changes that you've made and approve the pull request before it gets merged into the main codebase.
2. Click "merge pull request" and confirm the merge.

Now you should be able to see your changes on main.

Click [here](https://www.atlassian.com/git/tutorials/using-branches) for more information on branching.

## Conclusion

*Submission info and other stuff