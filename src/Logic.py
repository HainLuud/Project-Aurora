import functions, pathlib

class Logic():
    
    def __init__(self):
        self.scriptPath = pathlib.Path(__file__).parent.absolute()

        # Documentation: https://apscheduler.readthedocs.io/en/v3.6.3/index.html
        from apscheduler.schedulers.background import BackgroundScheduler
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        
        # idAndJob = {jobID : Job obj}
        self.idAndJob = {}

        # printableRules = {jobID : display text}
        self.printableRules = {}

        # jobIDsAndRows = {job.id : row}
        self.jobIDsAndRows = {}

        self.populateMapsFromConf()
    
    def populateMapsFromConf(self):
        import os.path, json, functions
        print("Exists", os.path.exists("conf.json"))
        if (os.path.exists(os.path.join(self.scriptPath, "conf.json"))):
            with open(os.path.join(self.scriptPath, "conf.json"), "r") as f:
                jobs = json.load(f)['jobs']
            
            # Add jobs to scheduler
            for job in jobs:
                if (job['type'] == "cron"):
                    self.addJob(job['id'], job['type'], job['row'], firstLoad=True, day=job['day'], hour=job['hour'], minute=job['minute'])
                else:
                    self.addJob(job['id'], job['type'], job['row'], firstLoad=True, freqMeasure=job['freqMeasure'], freqValue=job['freqValue'])


        else: 
            with open(os.path.join(self.scriptPath, "conf.json"), "w") as f:
                data = {
                        'jobs': [{
                                    'id' : '0',
                                    'type' : 'interval',
                                    'freqMeasure' : 'minutes',
                                    'freqValue' : 45, 
                                    'printableText' : 'ID: 0\t\tNotify me every 45 minutes',
                                    'row' : 0
                                }
                        ]
                }
                json.dump(data, f)

                schedJob = self.scheduler.add_job(functions.checkForecast, 'interval', id='0', minutes=45, kwargs={"scheduler":self.scheduler})
                # Populate dictionaries
                self.idAndJob['0'] = schedJob
                self.printableRules['0'] = 'ID: 0\t\tNotify me every 45 minutes'
                self.jobIDsAndRows['0'] = 0


    def addJobToJson(self, id, jobType, printableText, row, freqMeasure=None, freqValue=None, day=None, hour=None, minute=None):
        import json, os
        with open(os.path.join(self.scriptPath, "conf.json"), "r") as f:
            data = json.load(f)

        with open(os.path.join(self.scriptPath, "conf.json"), "w") as f:
            
            if (jobType == 'cron'):
                data['jobs'].append(
                   {
                        'id' : id,
                        'type' : jobType,
                        'day' : day,
                        'hour' : 45,
                        'minute' : minute, 
                        'printableText' : printableText,
                        'row' : row
                    } 
                )

            else:
                 data['jobs'].append(
                   {
                        'id' : id,
                        'type' : jobType,
                        'freqMeasure' : freqMeasure,
                        'freqValue' : freqValue, 
                        'printableText' : printableText,
                        'row' : row
                    } 
                )
            f.truncate()
            json.dump(data, f)
    
    
    def addJob(self, id, jobType, row, firstLoad=False, freqMeasure=None, freqValue=None, day=None, hour=None, minute=None):
        
        if (jobType == "cron"):

            schedJob = self.scheduler.add_job(functions.checkForecast, 'cron', id=id, 
            day_of_week=day[:3].lower(), hour=hour, minute=minute, kwargs={"scheduler":self.scheduler})

            printableText = "ID: {}\t\tNotify me on {} at {}:{}".format(id, day, hour, minute)
        
        else:
            if (freqMeasure == "hours"):
                schedJob = self.scheduler.add_job(functions.checkForecast, 'interval', id=id, hours=freqValue, kwargs={"scheduler":self.scheduler})
            elif (freqMeasure == "minutes"):
                schedJob = self.scheduler.add_job(functions.checkForecast, 'interval', id=id, minutes=freqValue, kwargs={"scheduler":self.scheduler})
            else:
                schedJob = self.scheduler.add_job(functions.checkForecast, 'interval', id=id, seconds=freqValue, kwargs={"scheduler":self.scheduler})
            
            printableText = "ID: {}\t\tNotify me every {} {}".format(id, freqValue, freqMeasure)

        
        self.jobIDsAndRows[id] = row
        self.idAndJob[id] = schedJob
        self.printableRules[id] = printableText

        if (not firstLoad):
            self.addJobToJson(id, jobType, printableText, row, freqMeasure=freqMeasure, freqValue=freqValue, day=day, hour=hour, minute=minute)

        return printableText

    def deleteJobFromJson(self, id):
        import json, os
        with open(os.path.join(self.scriptPath, "conf.json"), "r") as f:
            data = json.load(f)

        toRemoveIndex = 0
        
        for i, job in enumerate(data['jobs']):
            if (job['row'] == self.jobIDsAndRows[id]):
                toRemoveIndex = i
            if (job['row'] > self.jobIDsAndRows[id]):
                job['row'] -= 1
        
        del data['jobs'][toRemoveIndex]

        with open(os.path.join(self.scriptPath, "conf.json"), "w") as f:
            json.dump(data, f)


    def deleteRule(self, id, lastIndex):
        self.scheduler.remove_job(id)
        self.deleteJobFromJson(id)

        if (self.jobIDsAndRows[id] != lastIndex):
            for job in self.scheduler.get_jobs():
                if int(self.jobIDsAndRows[job.id]) > int(self.jobIDsAndRows[id]):
                    self.jobIDsAndRows[job.id] -= 1
        
        del self.jobIDsAndRows[id]
        del self.idAndJob[id]
        del self.printableRules[id]

