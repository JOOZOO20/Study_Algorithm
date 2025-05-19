T = int(input())
color=['red','orange','yellow','green','blue','purple']

for test_case in range(1, T + 1):
    input_color, output_color = input().split()
    index=color.index(input_color)

    if input_color == output_color:
        print('E')
        continue
    # +1 칸
    elif index==len(color)-1 and color[0]==output_color:
        print('A')
        continue
    elif index+1 <= len(color)-1 and color[index+1]==output_color:
        print('A')
        continue
    # -1칸
    elif index==0 and color[-1]==output_color:
        print('A')
        continue
    elif index-1>=0 and color[index-1]==output_color:
        print('A')
        continue
    # 정반대일때
    z = (index + 3) - len(color)
    if ((index+3) >= len(color)) and color[z] == output_color:
        print('C')
        continue
    elif index+3 <= len(color)-1 and color[index+3]==output_color:
        print('C')
        continue
    else:
        print('X')
        continue