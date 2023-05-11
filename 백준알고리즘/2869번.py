#BOJ_2869번_달팽이는 올라가고 싶다.
day, night, height = map(int, input().split())

height-=night
if (height%(day-night)>0):
    print(height//(day-night)+1)
else:
    print(height//(day-night))