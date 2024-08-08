class Lecture:
    @classmethod
    def convert_time(cls, _time):
        split_time = _time.split(':')
        return int(split_time[0])*60 + int(split_time[1])
    def __init__(self, topic, start_time, duration):
        self.topic, self.start_time, self.duration = topic, start_time, duration
        self.start = self.convert_time(start_time)
        self.finish = self.start + self.convert_time(duration)

class Conference:
    def __init__(self):
        self._list = []
    def add(self, lecture):
        time_is_busy = False
        for s in self._list:
            test = range(max(s.start,lecture.start), min(s.finish,lecture.finish)+1, 1)
            if len(test)>1:
                time_is_busy = True
                break
        if not time_is_busy:
            self._list.append(lecture)
        else:
            raise ValueError('Провести выступление в это время невозможно')
    def total(self):
        res = 0
        for r in self._list:
            res = res + (r.finish - r.start)
        h = res // 60
        m = res % 60
        return f'{h:02}:{m:02}'
    def longest_lecture(self):
        _max = max(self._list, key=lambda x: x.finish - x.start,)
        _res = _max.finish - _max.start
        h = _res // 60
        m = _res % 60
        return f'{h:02}:{m:02}'
    def longest_break(self):
        order_list = sorted(self._list, key=lambda x: x.start)
        _break, _tmp_finish, _res = 0, None, 0
        for o in order_list:
            if _tmp_finish is None:
                _tmp_finish = o.finish
                continue
            else:
                _res = o.start - _tmp_finish
                if _res > _break or _break is None:
                    _break = _res
                _tmp_finish = o.finish
        h = _break // 60
        m = _break % 60
        return f'{h:02}:{m:02}'




