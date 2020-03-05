# -*- coding: utf-8 -*-


def pack(capacity,tmp):

    itm_lst = []
    total_vol = 0
    prty = 0
    
    for it in tmp:
        if it['volume'] > capacity:
            pass
        elif it['volume'] <= capacity:
            total_vol += it['volume']
            itm_lst.append(it)
            capacity -= it['volume']
            prty += it['priority']
        elif capacity == 0:
            break
    
    print(prty,len(itm_lst))
    tmp2 = sorted(itm_lst,key=lambda x:x['entered'])
    for t in tmp2:
        print(t['item'])

if __name__ =='__main__':
    test_case = int(input())
    for t in range(test_case):
        its = []
        num_items, capacity = [int(x) for x in input().split()]
        ent_num = 0
        for n in range(num_items):
            lis_dict = {}
            item, vol, pri = input().split()
            vol = int(vol)
            pri = int(pri)
            lis_dict['item'] = item
            lis_dict['volume'] = vol
            lis_dict['priority'] = pri
            lis_dict['entered'] = ent_num
            its.append(lis_dict)
            tmp = sorted(its,key=lambda x:x['priority'],reverse=True)
            ent_num += 1
        pack(capacity,tmp)
        

##NOT PASSED##
        


