from random import randint, choice

def get_times(data_dic, buses):
    ''' input: dict of all time data
        output: List[tuples]  tuple->(bus number: str, time:float)
    '''
    ans = []
    for bus_i in buses:
        bus = str(bus_i) # change bus number from int to string
        rand_num = randint(0, 2) # choose random number from 0, 1, 2 
        if rand_num == 0:
            ans.append((bus, data_dic[bus])) # return local KCL time if rand_num is zero
            continue
        if rand_num == 2:
            ans.append((bus, choice(data_dic['KVLtime']))) # use random choice() function choose a KVL time ir rand_num is two
            continue
        bus_key = bus + '->' # the bus_key is used for finding key of Ohms time
        KCL_times = [data_dic[k] for k in data_dic.keys() if bus_key in k] # generate a list that stores all Ohms times
        ans.append((bus, min(KCL_times))) # store min Ohms time

    return ans