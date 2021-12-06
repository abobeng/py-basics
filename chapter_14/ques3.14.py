class Time :
    def __init__(self, sec) :
        self. sec=sec

    def convert_to_minutes (self) :
        return '{} : {} minute'. format (self.sec//60, self.sec%60)

    def convert_to_hour (self) :
        return '( :.2f} hour'. format (self. sec/3600)

print (a.convert_to_minutes () )
print (a.convert_to_hour () )