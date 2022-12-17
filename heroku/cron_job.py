from crontab import CronTab
 
my_cron = CronTab(user='TheDevilCoder')
print(my_cron)
job = my_cron.new(command='python3 C:\Workspace\django\src\api.py')
job.second.every(5)
 
my_cron.write()
