while True:
    number = input('������� ������������ ����� ������ ������: ')
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print('���, ��� ����� ����������!')
        else:
            print('���, ��� ����� �� ����������(')
        break
    else:
        print('������ ������������ ����� ������, ���������� ��� ���)')
