voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    f=open('voting_record_dump109.txt')
    mylist=list(f)
    current=[]
    for line in mylist:
        current=current+[line.split()]
    for x in range(len(current)):
        for y in range((len(current[x])-3)):
            current[x][y+3]=int(current[x][y+3])
    voting_dict={current[x][0]:current[x][3:] for x in range(len(current))}	
    return voting_dict
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    a=voting_dict[sen_a]
    b=voting_dict[sen_b]
    dot_product=sum([a[x]*b[x] for x in range(len(a))])
    return dot_product


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    a=voting_dict[sen]   #lista wynikow dla senatora "sen"
    long=len(a)          #dlugosc listy wynikow
    current=-long        #min wartosc iloczynu z innym senatorem
    similar=sen          #nazwisko podobnego senatora - na poczatek sen 
    for name in voting_dict.keys():
        if name!=sen:
            dot=policy_compare(name,sen,voting_dict)
            #if dot==current:
            #    similar=similar+{name}
            if dot>current:
                current=dot
                similar=name
    return similar
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    a=voting_dict[sen]   #lista wynikow dla senatora "sen"
    long=len(a)          #dlugosc listy wynikow
    current=long        #min wartosc iloczynu z innym senatorem
    similar=sen          #nazwisko podobnego senatora - na poczatek sen 
    for name in voting_dict.keys():
        if name!=sen:
            dot=policy_compare(name,sen,voting_dict)
            #if dot==current:
            #    similar=similar+{name}
            if dot<current:
                current=dot
                similar=name
    return similar
    
    

## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    current=0
    for name in sen_set:
        dot=policy_compare(sen,name, voting_dict)
        current=current+dot
    av=current/len(sen_set)
    return av

most_average_Democrat = 'Biden' # give the last name (or code that computes the last name)
    
	
    #senator_set={voting_data[x].split()[0] for x in range(len(voting_data)) if voting_data[x].split()[1]=='D'}
    #current=-46
    #for name in a.keys():
	 #   av=find_average_similarity(name,senator_set,a)
	 #   if av>current:
	 #       current=av
	 #       demokrat=name
	 
	 
	 
# Task 7
#there was a huge problem here - dont use constatnt like "Clinon" in function -> line 172!
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    long=len(voting_dict[list(sen_set)[0]])
    current=[]
    #current=[0*x for x in range(long)]
    #for name in sen_set:
    #   for num in range(long):
     #       current[num-1]=current[num-1]+voting_dict[name][num-1]
    #av=[x/long for x in current]
    for num in range(long):
        current=current+[sum([voting_dict[name][num] for name in sen_set])]
    av=[x/len(sen_set) for x in current]
    return av
average_Democrat_record = find_average_record({voting_data[x].split()[0] for x in range(len(voting_data)) if voting_data[x].split()[1]=='D'}, create_voting_dict())


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    names=[]
    similar=[[],[]]
    current=[len(x) for x in voting_dict.values()][0]
    for name1 in voting_dict.keys():
        names=names+[name1]
        for name2 in voting_dict.keys():
            if not name2 in names:
                dot=policy_compare(name1,name2,voting_dict)
            #if dot==current:
            #    similar=similar+{name}
                if dot<current:
                    current=dot
                    similar[0]=name1
                    similar[1]=name2
    return similar
