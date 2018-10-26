rank = "J"

#if(type(rank) == int):   
#    self.rank = rank
if(type(rank) == str):
    rank_dict = {1:"A",11:"J",12:"Q",13:"K"}
    for k, v in rank_dict.items():
        if rank in v:
            print(k)


