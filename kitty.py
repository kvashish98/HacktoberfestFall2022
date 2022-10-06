states=['C','S','H','VH']
happiness='C'
percepts=['bump','clap']
position=11

def returnAction(percept,happiness):
    if percept=='clap':
        if states.index(happiness)>1:
            return ['walk']
        else:
            return ['meow','walk']
        
    elif percept=='pet':
        if states.index(happiness)>1:
            return ['purr']
        else:
            return ['purr','meow']

    elif percept=='bump':
        if states.index(happiness)==3:
            return ['blink','stop']
        else:
            return ['meow', 'walk', 'stop']

def stateUpdate(position,percepts,happiness,states):
    for percept in percepts:
        add=0
        actions=[]
        for i in returnAction(percept,happiness):
            if i=='meow' or i=='purr' or i=='blink' or i=='stop' or i=='start':
                position+=0
            elif i=='walk':
                if position-1>-1:
                    position-=1
            actions.append(i)
            
        if percept=='clap':
            add=1
        elif percept=='pet':
            add=2
        elif percept=='bump':
            add=-1

        if states.index(happiness)+add>3:
            happiness='VH'
        elif states.index(happiness)+add<0:
            happiness='C'
        else:
            happiness=states[states.index(happiness)+add]
     

        print(percept,actions, [position,happiness])

stateUpdate(position,percepts,happiness,states)
  
        
