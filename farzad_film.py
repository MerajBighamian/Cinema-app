n=int(input())
film_true=[]
if n>=1 and n<=10:
    for i in range(0,n):
        film=input()
        if len(film)<1000:
            film_true.append(film)
    for film_order in film_true:
        film_ordered=film_order.title()
        print(film_ordered)
