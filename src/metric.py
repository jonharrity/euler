

import time
import traceback


class Metric():
    
    
    def __init__(self, algs, reps=1):
        count = 0
        
        for alg in algs: 
            count += 1     
            timecard = []
            print('[%s] executing %s:' % (count, alg))
            for i in range(reps):
                try:
                    alg_start = time.time() * 1000
                    alg()
                    alg_end = time.time() * 1000
                except Exception as e:
                    alg_end = time.time() * 1000
                    print(traceback.format_exc())
                    print('>Exception [%s] raised' % e)
                finally:
                    alg_duration = alg_end - alg_start
                
                if reps <= 1:
                    print('>total time (miliseconds): %s \n' % alg_duration)
                else:
                    timecard.append(alg_duration)
                    
            if reps > 1:
                print('-Stats for %s repetitions in miliseconds-' % reps)
                print('Mean execution time: %s' % (sum(timecard) / reps))
                print('Median execution time: %s\n' % (sorted(timecard)[int(reps/2)]))
