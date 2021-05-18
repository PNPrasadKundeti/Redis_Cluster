import redis  r = redis.Redis(    host=104.197.91.98',    port=6379)i=1while(i < 101):    r.rpush('demolist', i)    i += 1#Print out the values from 1 - 100  print(r.lrange('demolist', 0, -1))
