import unittest

'''
Given a sequence of events, return the best sequence to do such that dependencies aren't conflicting.
Example:
A->B->C->F->G
Z->B->F->P
A->B->Z->C->F->P->G (There are multiple valid combinations.)

'''
def best_sequence(sequence_graph):
    best_sequence = []
 
    while sequence_graph:
        events_with_dependencies = get_events_with_dependencies(sequence_graph)
        events_wo_dependencies = get_events_wo_dependencies(events_with_dependencies, sequence_graph)
 
        for event in events_wo_dependencies:
            best_sequence.append(event)
            del sequence_graph[event] #this mutates the existing dictionary 
 
    return best_sequence

def get_events_with_dependencies(graph):
    events_with_dependecies = set()
    for event in graph:
        events_with_dependecies = events_with_dependecies.union(set(graph[event]))
    return events_with_dependecies
 
def get_events_wo_dependencies(events, graph):
    events_wo_dependencies = set()
 
    for event in graph:
        if not event in events:
            events_wo_dependencies.add(event)
 
    return events_wo_dependencies


if __name__ == '__main__':
	graph = {
        'A' : ['B'],
        'B' : ['C','F','P'],
        'C' : ['F'],
        'F' : ['G'],
        'P' : [],
        'G' : []
        }
	print(best_sequence(graph))



