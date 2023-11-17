def get_a(*args, **kwargs):
        summ = sum(list(args))
        if kwargs['a'] == "+":
            return summ
        else:
        # print(args, kwargs)
            def b(*args, **kwargs):
                kwargs['summ'] += kwargs['b']
                return kwargs['summ']        
            return b(**kwargs, summ = summ)
        

print(get_a(1,123,23,a='-',b=13239487392847,c=[1,2,3]))
