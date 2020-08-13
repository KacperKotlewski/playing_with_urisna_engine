from datetime import datetime, timedelta 

class Deltatime():
    def __init__(self):
        self.time = datetime.now() 

    def Get(self):
        time_d = (datetime.now() - self.time)
        time_d_ms  = time_d / timedelta(milliseconds=1)
        return time_d_ms

    def Set(self):
        self.time = datetime.now()
    
    def Update(self):
        dt = self.Get()
        self.Set()
        return dt

    def __call__(self):
        return self.Update()

class Tick():
    def __init__(self, ms_per_tick=1000):
        self.dt = Deltatime()
        self.mspt = ms_per_tick
    
    def Set_ms_per_tick(self, val):
        self.mspt = val

    def Check(self):
        if self.dt.Get() >= self.mspt:
            self.dt()
            return True
        return False

    def __call__(self):
        return self.Check()
