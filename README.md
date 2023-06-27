# PROJECT_SETUP
setup files and stuff to start quickly new project, it will be more enhance by time and my experiences...

### this is like it works:  
vzor:  

```git
adamaanna@MacBook-Air-uzivatela-Adam project_Setup % python3 projectSetUp.py  
Enter the project directory: "/Users/adamaanna/documents/www"  
Enter the project name: "hahaha"  
Project structure created successfully!  
```

I execute following commands to create this folder, first i write "python3 projectSetUo.py" command, that call my Python file where is function to create this magic. Then terminal ask me to specific folder to save and then name of creating folder, and that it for now

*P.S.: don't worry, folder assets will be create on Github when you put there some data*


**P.S.: little help:**

**How to solve this problem of "! [rejected] master -> master (fetch first)"**

->this way->
```git   
git fetch origin main  
git merge  main  
git fetch origin main:tmp  
git rebase tmp  
git push origin HEAD:main  
git branch -D tmp  
```

## *Now everything works well. smile (((((:*
