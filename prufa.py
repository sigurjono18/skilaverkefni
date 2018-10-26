rank = 1

rank_dict = {1:"A",11:"J",12:"Q",13:"K"}
if rank >= 2 or rank <= 10:
    rank = str(rank)
        
if rank in rank_dict:
    rank2 = rank_dict[rank]

print(rank2)